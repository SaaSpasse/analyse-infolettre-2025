# Prompt pour la prochaine session Claude Code

## Contexte

Je veux construire une mini web app de visualisation de données pour la dernière infolettre de l'année 2025 de SaaSpasse.

L'app présente une rétrospective analytique des 49 éditoriaux publiés en 2025 : stats, thèmes, name drops, linguistique, mood, scènes d'ouverture, angles morts.

## Fichiers de référence

Tout est dans `/Users/francoislanthiernadeau/Claude Code/saaspasse-2025-retrospective/` :

1. **data.json** — Toutes les données structurées (stats, thèmes, mentions, etc.)
2. **NOTES.md** — Contexte projet, corrections à appliquer, blagues à inclure, charte couleurs
3. **visualisations.md** — Maquettes ASCII des visualisations suggérées

## Charte de couleurs SaaSpasse

- Dark: `#070A26`
- Purple: `#853DFF`
- Light Purple: `#AD80FF`
- Cream: `#ECEBF1`
- Card backgrounds: Purple Wash `#F0E8FF`, Teal Wash `#E0FFF7`, Gold Wash `#FFF8E0`, Rose Wash `#FFF0F3`

## Points importants

1. **Slider interactif** pour le temps de frappe (ajuster WPM, voir le temps changer)
2. **Blagues à inclure** — Voir NOTES.md pour les one-liners
3. **Disclaimers** — Voir NOTES.md pour les corrections et notes
4. **Design** — Frank a une commande custom pour éviter le "AI slop". Lui demander avant de commencer.

## Stack probable

- shadcn/ui pour les composants
- Tailwind CSS avec les couleurs SaaSpasse
- Charts avec recharts ou autre lib compatible shadcn
- Probablement déployé sur Netlify

## Pour commencer

```bash
cd "/Users/francoislanthiernadeau/Claude Code/saaspasse-2025-retrospective"
```

Puis lire les 3 fichiers pour avoir tout le contexte.

Demander à Frank quelle commande de design il voulait utiliser.
