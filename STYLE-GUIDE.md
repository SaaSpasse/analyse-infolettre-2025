# Style Guide — Neo-Brutalist Web Design

Guide de style pour créer des applications web avec une esthétique **neo-brutalist / retro-tech**. Ce document est conçu pour être partagé avec un AI ou un développeur pour appliquer ce style à un nouveau projet.

---

## Philosophie du design

- **Neo-brutalist** : Ombres dures décalées, bordures épaisses, pas de border-radius
- **Retro-tech** : Typographie monospace pour les données, grain de texture vintage
- **Contrastes forts** : Fonds pastels avec bordures sombres
- **Interactivité visible** : Les éléments cliquables réagissent avec des micro-animations

---

## Variables CSS à définir

Définir ces variables dans `:root` selon le schéma de couleur de l'application :

```css
:root {
  /* Couleurs principales - À PERSONNALISER */
  --dark: #000000;           /* Texte, bordures, ombres */
  --accent: #0066FF;         /* Couleur accent principale */
  --accent-light: #66AAFF;   /* Accent secondaire (hover, etc.) */
  --background: #F5F5F5;     /* Fond de page */

  /* Fonds de cartes pastels - À PERSONNALISER */
  --wash-1: #E8F0FF;         /* Pastel primaire */
  --wash-2: #E0FFF7;         /* Pastel secondaire */
  --wash-3: #FFF8E0;         /* Pastel tertiaire */
  --wash-4: #FFF0F3;         /* Pastel quaternaire */

  /* Ombres - Ne pas modifier */
  --shadow: 4px 4px 0px var(--dark);
  --shadow-sm: 2px 2px 0px var(--dark);
}
```

---

## Typographie

### Fonts Google à importer

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;700&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
```

### Usage

| Font | Poids | Usage |
|------|-------|-------|
| **Space Grotesk** | 400, 500, 700 | Titres, corps de texte, UI générale |
| **Space Mono** | 400, 700 | Labels, stats, données, éléments techniques |

### Hiérarchie des tailles

```css
h1 {
  font-family: 'Space Grotesk', sans-serif;
  font-size: clamp(2rem, 6vw, 3.5rem);
  font-weight: 700;
  line-height: 1.1;
}

h2 {
  font-family: 'Space Grotesk', sans-serif;
  font-size: clamp(1.5rem, 4vw, 2rem);
  font-weight: 700;
}

h3 {
  font-family: 'Space Grotesk', sans-serif;
  font-size: 1.1rem;
  font-weight: 700;
}

body {
  font-family: 'Space Grotesk', sans-serif;
  line-height: 1.6;
}

.mono {
  font-family: 'Space Mono', monospace;
}

/* Labels et petits textes techniques */
.label {
  font-family: 'Space Mono', monospace;
  font-size: 12px;
  text-transform: uppercase;
}
```

---

## Composants

### Reset de base

```css
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  background-color: var(--background);
  color: var(--dark);
}
```

### Card (composant principal)

```css
.card {
  background: white;
  border: 3px solid var(--dark);
  box-shadow: var(--shadow);
  padding: 24px;
  margin-bottom: 20px;
  /* PAS de border-radius */
}

/* Variantes avec fonds colorés */
.card.wash-1 { background: var(--wash-1); }
.card.wash-2 { background: var(--wash-2); }
.card.wash-3 { background: var(--wash-3); }
.card.wash-4 { background: var(--wash-4); }
```

### Boutons

```css
.btn {
  font-family: 'Space Mono', monospace;
  font-size: 12px;
  padding: 8px 16px;
  background: white;
  border: 2px solid var(--dark);
  box-shadow: var(--shadow-sm);
  cursor: pointer;
  transition: all 0.1s;
}

.btn:hover {
  background: var(--accent);
  color: white;
  transform: translate(1px, 1px);
  box-shadow: 1px 1px 0px var(--dark);
}

.btn:active {
  transform: translate(2px, 2px);
  box-shadow: none;
}

.btn:focus-visible {
  outline: 3px solid var(--accent);
  outline-offset: 2px;
}
```

### Stat Box (pour afficher des métriques)

```css
.stat-box {
  background: white;
  border: 3px solid var(--dark);
  box-shadow: var(--shadow);
  padding: 20px;
  text-align: center;
}

.stat-number {
  font-size: 2.5rem;
  font-weight: 700;
  color: var(--accent);
  line-height: 1;
}

.stat-label {
  font-family: 'Space Mono', monospace;
  font-size: 12px;
  margin-top: 8px;
  text-transform: uppercase;
}
```

### Input Range (slider)

```css
input[type="range"] {
  width: 100%;
  height: 12px;
  -webkit-appearance: none;
  background: white;
  border: 2px solid var(--dark);
  cursor: pointer;
}

input[type="range"]::-webkit-slider-thumb {
  -webkit-appearance: none;
  width: 24px;
  height: 24px;
  background: var(--accent);
  border: 2px solid var(--dark);
  cursor: pointer;
}
```

### Bar Chart (barres horizontales)

```css
.bar-row {
  display: flex;
  align-items: center;
  gap: 12px;
}

.bar-label {
  width: 140px;
  font-family: 'Space Mono', monospace;
  font-size: 12px;
  flex-shrink: 0;
}

.bar-track {
  flex: 1;
  height: 28px;
  background: white;
  border: 2px solid var(--dark);
}

.bar-fill {
  height: 100%;
  background: var(--accent);
  transition: width 0.5s ease-out;
}

.bar-value {
  font-family: 'Space Mono', monospace;
  font-size: 12px;
  width: 50px;
  text-align: right;
}
```

### Note boxes (alertes, disclaimers)

```css
/* Note informative */
.note-box {
  background: var(--wash-2);
  border: 2px solid var(--dark);
  padding: 12px 16px;
  font-size: 13px;
  display: flex;
  align-items: flex-start;
  gap: 8px;
}

/* Disclaimer / Warning */
.disclaimer {
  background: var(--wash-4);
  border: 2px dashed var(--dark);
  padding: 12px 16px;
  font-size: 13px;
  display: flex;
  align-items: flex-start;
  gap: 8px;
}

/* Citation / Blague */
.quote-box {
  background: var(--wash-3);
  border: 3px solid var(--dark);
  box-shadow: var(--shadow);
  padding: 20px;
  font-style: italic;
  display: flex;
  align-items: flex-start;
  gap: 12px;
}
```

### Tooltip

```css
.tooltip-trigger {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 18px;
  height: 18px;
  background: var(--dark);
  color: white;
  border-radius: 50%;
  font-size: 11px;
  font-weight: 700;
  cursor: help;
  position: relative;
}

.tooltip-trigger:hover .tooltip-content {
  display: block;
}

.tooltip-content {
  display: none;
  position: absolute;
  bottom: 100%;
  left: 50%;
  transform: translateX(-50%);
  background: var(--dark);
  color: white;
  padding: 8px 12px;
  border-radius: 4px;
  font-size: 12px;
  font-weight: 400;
  white-space: nowrap;
  margin-bottom: 8px;
  z-index: 1000;
}

.tooltip-content::after {
  content: "";
  position: absolute;
  top: 100%;
  left: 50%;
  transform: translateX(-50%);
  border: 6px solid transparent;
  border-top-color: var(--dark);
}
```

---

## Layout

### Container

```css
.container {
  max-width: 900px;
  margin: 0 auto;
  padding: 0 20px;
}
```

### Sections

```css
section {
  padding: 60px 0;
  border-bottom: 3px solid var(--dark);
}
```

### Grilles responsives

```css
/* Grille 2 colonnes */
.grid-2 {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 20px;
}

/* Grille 3 colonnes */
.grid-3 {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 16px;
}

/* Stats grid (3 colonnes) */
.stats-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 16px;
}

/* Responsive : passer à 1 colonne sur mobile */
@media (max-width: 600px) {
  .grid-2,
  .grid-3,
  .stats-grid {
    grid-template-columns: 1fr;
  }
}
```

### Navigation sticky

```css
nav {
  position: sticky;
  top: 0;
  background: var(--background);
  border-bottom: 3px solid var(--dark);
  padding: 12px 0;
  z-index: 100;
}

nav .container {
  display: flex;
  gap: 8px;
  overflow-x: auto;
  scrollbar-width: none;
}

/* Dégradé de fade sur le scroll horizontal */
nav .container::after {
  content: "";
  position: sticky;
  right: 0;
  min-width: 40px;
  background: linear-gradient(to left, var(--background), transparent);
  pointer-events: none;
}
```

---

## Effets spéciaux

### Texture grain (overlay)

Ajouter une texture de grain vintage sur toute la page :

```css
body::before {
  content: "";
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  pointer-events: none;
  opacity: 0.12;
  z-index: 1000;
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 400 400' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)'/%3E%3C/svg%3E");
}
```

### Liens

```css
a {
  color: var(--accent);
  text-decoration: none;
}

a:hover {
  text-decoration: underline;
}
```

---

## Icônes

Utiliser **Lucide Icons** pour les icônes :

```html
<script src="https://unpkg.com/lucide@latest"></script>
```

Usage :
```html
<i data-lucide="star"></i>
<script>lucide.createIcons();</script>
```

---

## Charts (Chart.js)

Si besoin de graphiques, utiliser Chart.js avec ce style :

```html
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
```

Configuration recommandée pour matcher le style :

```javascript
const chartConfig = {
  // Couleurs à adapter selon votre palette
  borderColor: 'var(--dark)',
  backgroundColor: 'var(--accent)',

  // Options globales
  options: {
    plugins: {
      legend: {
        labels: {
          font: {
            family: "'Space Mono', monospace",
            size: 12
          }
        }
      }
    },
    scales: {
      x: {
        ticks: {
          font: {
            family: "'Space Mono', monospace",
            size: 11
          }
        },
        grid: {
          color: '#E0E0E0'
        }
      },
      y: {
        ticks: {
          font: {
            family: "'Space Mono', monospace",
            size: 11
          }
        },
        grid: {
          color: '#E0E0E0'
        }
      }
    }
  }
};
```

Wrapper pour les charts :

```css
.chart-wrapper {
  background: white;
  border: 3px solid var(--dark);
  box-shadow: var(--shadow);
  padding: 20px;
}
```

---

## Checklist d'implémentation

Quand tu appliques ce style à une nouvelle app :

1. [ ] Définir le schéma de couleurs dans `:root`
2. [ ] Importer les fonts Google (Space Grotesk + Space Mono)
3. [ ] Appliquer le reset CSS de base
4. [ ] Ajouter la texture grain sur le body
5. [ ] Utiliser les composants card avec bordures 3px et shadow
6. [ ] Styliser les boutons avec l'effet de translation au hover
7. [ ] Utiliser Space Mono pour tout ce qui est données/stats
8. [ ] Pas de border-radius (sauf tooltips)
9. [ ] Sections séparées par des bordures 3px
10. [ ] Grilles responsives avec breakpoint à 600px

---

## Exemples de palettes de couleurs

### Palette "Electric Blue"
```css
--dark: #0A1628;
--accent: #0066FF;
--accent-light: #66AAFF;
--background: #F0F4F8;
--wash-1: #E0EAFF;
--wash-2: #E0FFF4;
--wash-3: #FFF8E0;
--wash-4: #FFE0E8;
```

### Palette "Forest Green"
```css
--dark: #1A2E1A;
--accent: #2D8B4E;
--accent-light: #5CBC7A;
--background: #F4F8F4;
--wash-1: #E0F5E8;
--wash-2: #E8F0FF;
--wash-3: #FFF8E0;
--wash-4: #FFE8F0;
```

### Palette "Warm Coral"
```css
--dark: #2A1A1A;
--accent: #E85A4F;
--accent-light: #FF8A80;
--background: #FDF8F6;
--wash-1: #FFE8E5;
--wash-2: #E5FFF8;
--wash-3: #FFF5E0;
--wash-4: #F0E8FF;
```

---

*Ce guide est générique et réutilisable. Adapter les couleurs selon l'identité visuelle de chaque projet.*
