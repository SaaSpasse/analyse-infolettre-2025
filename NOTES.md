# SaaSpasse 2025 — Rétrospective Éditoriale

## Contexte du projet

**Objectif** : Créer une mini web app de visualisation de données qui analyse les 49 éditoriaux de l'infolettre SaaSpasse publiés en 2025.

**Destination** : La dernière infolettre de l'année 2025.

**Source des données** : `/Users/francoislanthiernadeau/Claude Code/posts-infolettre/editoriaux/2025-*.md`

---

## Disclaimer à mettre en en-tête

> Cette analyse porte uniquement sur le contenu éditorial de l'infolettre SaaSpasse, excluant les sections promotionnelles et nouvelles en fin d'édito.

---

## Notes éditoriales importantes (de Frank)

### Corrections à appliquer

1. **Phil Lehoux** et **Phil Genois** sont deux personnes distinctes
   - Phil Lehoux = fondateur de Missive
   - Phil Genois (ou Philippe Genois) = fondateur d'InputKit

2. **Jean Gab Crevier** — PAS de trait d'union entre Jean et Gab

3. **SaaSpasse** — Retirer du palmarès des entreprises mentionnées (narcissique)

4. **Coveo** — Ne pas inclure s'il n'est pas dans les éditoriaux (seulement dans posts-complets)

### Blagues à inclure

1. **Name drops - VCs** : "Ils ne sont pas sur ma cap table, faque ils ne sont pas dans mon top 10."

2. **Phil Lehoux vs Nassim Taleb** : "Phil Lehoux a battu Nassim Taleb. Let that sink in."

3. **Top 3 personnes** : Ajouter disclaimer — "Le top 3 ressort beaucoup car impliqués dans la conférence SaaSpasse. Plusieurs éditos étaient sur la conf."

### Notes techniques

1. **Stack AI** : Ajouter une note que la majorité migre vers Claude Code, et voice dictation migré vers Monologue

2. **Slider temps de frappe** : L'app doit avoir un slider interactif pour changer le WPM et voir le temps changer en conséquence

### Insights pour 2026 (à intégrer)

- Plus de contenu sur go-to-market, ventes, croissance
- On ralentit pas sur l'AI

---

## Structure de la web app suggérée

### Sections principales

1. **Hero / Stats globales**
   - 49 éditoriaux
   - 66 762 mots
   - Slider temps de frappe
   - Équivalent en pages de livre

2. **Thèmes & Obsessions**
   - Palmarès des sujets (bar chart)
   - Courbe AI par mois
   - Saisonnalité des thèmes

3. **Name Drop Alert**
   - Top personnes (avec disclaimers/blagues)
   - Top entreprises/produits
   - Stack AI
   - Blague VCs

4. **Linguistique**
   - Niveau de lecture (gauge)
   - Ratio franglais
   - Palmarès expressions québécoises (avec emojis feuille d'érable)
   - Mots signature

5. **Mood-o-mètre**
   - Courbe de vibe par mois
   - Légende des pics et creux
   - Moments émotionnels marquants

6. **Scènes d'ouverture**
   - Types de hooks (pie chart ou bar)
   - Lieux/situations (avec emojis)
   - Mises en scène mémorables (carrousel ou quotes)

7. **Angles morts**
   - Ce qu'on a bien couvert
   - Ce qu'on a ignoré
   - Section autocritique
   - Pistes 2026

---

## Charte de couleurs SaaSpasse

**Primaires:**
| Nom | Hex | Usage |
|-----|-----|-------|
| Dark | `#070A26` | Texte, borders |
| Purple | `#853DFF` | Accent principal |
| Light Purple | `#AD80FF` | Accent secondaire |
| Cream | `#ECEBF1` | Background |

**Backgrounds cards:**
| Nom | Hex |
|-----|-----|
| Purple Wash | `#F0E8FF` |
| Teal Wash | `#E0FFF7` |
| Gold Wash | `#FFF8E0` |
| Rose Wash | `#FFF0F3` |

---

## Tech stack suggérée

- **Framework** : À déterminer (Frank a une commande de design custom)
- **Charts** : shadcn/ui + recharts ou autre lib compatible
- **Styling** : Tailwind CSS avec les couleurs SaaSpasse
- **Hosting** : Probablement Netlify (déjà utilisé pour d'autres projets)

---

## Fichiers dans ce dossier

- `data.json` — Toutes les données structurées pour la web app
- `NOTES.md` — Ce fichier (contexte, notes éditoriales, structure)

---

## Pour la prochaine session

1. Lire ce fichier NOTES.md pour le contexte
2. Lire data.json pour les données
3. Demander à Frank la commande de design qu'il voulait utiliser
4. Construire la web app avec les visualisations

---

## Commande pour démarrer

```bash
cd "/Users/francoislanthiernadeau/Claude Code/saaspasse-2025-retrospective"
```
