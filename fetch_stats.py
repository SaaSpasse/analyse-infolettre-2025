#!/usr/bin/env python3
"""
Script pour récupérer les stats de popularité des posts beehiiv 2025.
Utilise la config existante de posts-infolettre.
"""

import os
import sys
import json
from pathlib import Path
from datetime import datetime

try:
    import requests
except ImportError:
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "requests", "-q"])
    import requests

# Config depuis posts-infolettre
CONFIG_FILE = Path.home() / "Claude Code" / "posts-infolettre" / ".beehiiv_config.json"

def load_config():
    if not CONFIG_FILE.exists():
        print(f"Config manquante: {CONFIG_FILE}")
        sys.exit(1)
    with open(CONFIG_FILE) as f:
        return json.load(f)

def get_headers(api_key):
    return {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

def list_all_posts(config, year=2025):
    """Récupère tous les posts de l'année."""
    all_posts = []
    page = 1

    while True:
        url = f"https://api.beehiiv.com/v2/publications/{config['publication_id']}/posts"
        params = {
            "limit": 50,
            "status": "confirmed",
            "order_by": "publish_date",
            "direction": "desc",
            "page": page,
            "expand[]": "stats"
        }

        response = requests.get(url, headers=get_headers(config['api_key']), params=params)
        response.raise_for_status()

        data = response.json()
        posts = data.get('data', [])

        if not posts:
            break

        for post in posts:
            publish_date = post.get('publish_date')
            if isinstance(publish_date, int):
                dt = datetime.fromtimestamp(publish_date)
            else:
                continue

            # Filtrer par année
            if dt.year < year:
                return all_posts  # On a dépassé l'année cible
            if dt.year == year:
                # Seulement les éditoriaux (audience=both)
                if post.get('audience') == 'both':
                    all_posts.append(post)

        page += 1
        if page > 20:  # Safety limit
            break

    return all_posts

def get_post_stats(config, post_id):
    """Récupère les stats détaillées d'un post."""
    url = f"https://api.beehiiv.com/v2/publications/{config['publication_id']}/posts/{post_id}/stats"

    response = requests.get(url, headers=get_headers(config['api_key']))

    if response.status_code == 404:
        # Endpoint peut ne pas exister, essayer aggregate
        return None

    response.raise_for_status()
    return response.json().get('data')

def main():
    config = load_config()
    print("Récupération des posts 2025...")

    posts = list_all_posts(config, year=2025)
    print(f"Trouvé {len(posts)} éditoriaux en 2025")

    results = []

    for post in posts:
        publish_date = post.get('publish_date')
        if isinstance(publish_date, int):
            date_str = datetime.fromtimestamp(publish_date).strftime('%Y-%m-%d')
        else:
            date_str = str(publish_date)[:10]

        # Stats de base incluses dans le post
        stats = post.get('stats', {})

        result = {
            "id": post.get('id'),
            "title": post.get('title'),
            "slug": post.get('slug'),
            "date": date_str,
            "url": post.get('web_url', f"https://saaspasse.beehiiv.com/p/{post.get('slug')}"),
            "email_stats": {
                "recipients": stats.get('email', {}).get('recipients', 0),
                "delivered": stats.get('email', {}).get('delivered', 0),
                "opens": stats.get('email', {}).get('opens', 0),
                "unique_opens": stats.get('email', {}).get('unique_opens', 0),
                "open_rate": stats.get('email', {}).get('open_rate', 0),
                "clicks": stats.get('email', {}).get('clicks', 0),
                "unique_clicks": stats.get('email', {}).get('unique_clicks', 0),
                "click_rate": stats.get('email', {}).get('click_rate', 0),
            },
            "web_stats": {
                "views": stats.get('web', {}).get('views', 0),
                "clicks": stats.get('web', {}).get('clicks', 0),
            }
        }

        # Score de popularité composite
        email = result['email_stats']
        web = result['web_stats']

        # Formule: unique_opens * 1 + unique_clicks * 5 + web_views * 0.5
        # Pondéré pour valoriser l'engagement (clicks) plus que les opens
        popularity_score = (
            email.get('unique_opens', 0) * 1 +
            email.get('unique_clicks', 0) * 5 +
            web.get('views', 0) * 0.5
        )
        result['popularity_score'] = popularity_score

        results.append(result)
        print(f"  {date_str} | {post.get('title')[:40]} | score: {popularity_score:.0f}")

    # Trier par popularité
    results.sort(key=lambda x: x['popularity_score'], reverse=True)

    # Sauvegarder
    output_file = Path(__file__).parent / "posts_stats_2025.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    print(f"\nSauvegardé dans {output_file}")

    # Top 10
    print("\n=== TOP 10 par popularité ===")
    for i, post in enumerate(results[:10], 1):
        print(f"{i}. {post['title'][:50]} (score: {post['popularity_score']:.0f})")
        print(f"   Opens: {post['email_stats']['unique_opens']} | Clicks: {post['email_stats']['unique_clicks']} | Web: {post['web_stats']['views']}")

if __name__ == "__main__":
    main()
