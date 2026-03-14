# Claude Design System — Comprehensive Codex Instructions

> **What this is:** A complete design system reference for building web applications and interfaces that embody the Claude/Anthropic visual language. This document serves as Codex instructions — a structured set of rules, patterns, and production-ready code that any AI coding assistant can follow to produce pixel-perfect, brand-consistent output.
>
> **Design DNA:** Warm, humanistic, editorially refined. Serif typography, sand-and-cream surfaces, rust-orange accents, multi-layer shadows, generous whitespace, and restrained elegance. Inspired by the claude.ai product interface and Anthropic's brand identity as designed by Geist agency.
>
> **Not this:** Cold blue tech. Purple gradients. Glass morphism. Inter/Roboto/Arial. Hyper-futuristic. Flashy.

---

## 0. How to Use This Document (Codex Instructions)

### 0.1 Mandatory Rules

When building any interface using the Claude Design System, Codex **must**:

1. **Read the relevant skills first** — before writing any code, examine `/mnt/skills/public/frontend-design/SKILL.md` and `/mnt/skills/examples/brand-guidelines/SKILL.md` for complementary guidance.
2. **Always use design tokens** — never hardcode colors, spacing, radii, shadows, or font sizes. Reference the CSS custom properties defined in Sections 2.2–2.7.
3. **Always pair serif + sans-serif** — the Claude system uses serif typography for body content and sans-serif for UI chrome. Never use only one or the other.
4. **Always include accessibility** — every interactive element must have visible focus states, ARIA labels, sufficient contrast (WCAG AA), and reduced-motion fallbacks.
5. **Always provide light and dark mode** — every component must work in both modes using the token system.
6. **Warm over cold** — when in doubt between a cool and warm variant of any design decision, choose warm. This is the foundational Claude aesthetic principle.

### 0.2 Anti-Patterns (Never Do This)

These patterns conflict with the Claude Design System and must be avoided:

| Anti-Pattern | Why It Fails | Claude Alternative |
|---|---|---|
| Inter, Roboto, Arial as body font | Generic "AI slop" aesthetic | Use Lora (serif) or Tiempos-style fallback |
| Purple gradients on white | Overused AI cliché | Use sand/cream backgrounds with rust-orange accents |
| Glass morphism / backdrop-filter blur | Conflicts with Claude's solid, warm surfaces | Use multi-layer shadow depth system |
| Uniform rounded corners everywhere | Lazy, unfocused design | Use the Claude radius scale (intentional variation) |
| Cold blue as primary action color | Contradicts warm brand DNA | Use rust-orange (#d97757) as primary accent |
| Centered everything | Lacks editorial tension | Use left-aligned body with selective center moments |
| System fonts / monospace for body | Undermines editorial character | Serif body, sans-serif UI, monospace only for code |
| Dense, cramped layouts | Contradicts generous whitespace philosophy | Use the Claude spacing scale with ample breathing room |

### 0.3 Quick Reference

| I need to... | Go to... |
|---|---|
| Set up colors, fonts, spacing | Section 2 (Visual Foundation) |
| Build the CSS architecture | Section 3 (CSS Implementation) |
| Animate an entrance or transition | Section 4 (Animation & Motion) |
| Build a specific component | Section 5 (Component Library) |
| Build form elements | Section 6 (Form Elements) |
| Lay out a page | Section 7 (Layout Patterns) |
| Handle interactions | Section 8 (Interaction Patterns) |
| Use icons | Section 9 (Icon System) |
| Make it responsive / mobile webapp | Section 10 (Responsive & Mobile Webapp Standards) |
| Optimize performance | Section 11 (Performance Guidelines) |
| Check accessibility | Section 12 (Accessibility Checklist) |
| Quick do's and don'ts | Section 13 (Do's and Don'ts) |
| Choose a tech stack | Section 14 (Technology Stack) |
| Handle component states | Section 15 (State Patterns) |
| Show notifications/toasts | Section 16 (Toast / Notification) |
| Animate page transitions | Section 17 (View Transitions) |
| Compose layouts correctly | Section 18 (Composition Rules) |
| Name things consistently | Section 19 (Naming Conventions) |
| Organize files | Section 20 (File Structure) |
| Use utility classes | Section 21 (Utility Classes) |
| Check browser support | Section 22 (Browser Support Matrix) |
| Start from a page template | Section 23 (Page Templates) |
| Bootstrap a new project | Section 24 (Quick Start Guide) |
| Choose fonts wisely | Section 25 (Typography Reference) |
| Work with color theory | Section 26 (Color Theory & Palette Design) |

### 0.4 Design Thinking Pre-Flight

Before building any page, Codex must answer these five questions:

**1. Purpose** — What does the user accomplish on this page? (Not "what does it show" but "what does the user *do*".)

**2. Content Hierarchy** — What is the primary content? Secondary? Tertiary? The Claude system uses generous whitespace to create visual hierarchy rather than aggressive sizing differences.

**3. Hero Moment** — Every page should have ONE memorable visual element: a beautifully typeset heading, an elegant card composition, a signature animation. Not everything at once.

**4. Motion Story** — Plan a single orchestrated entrance sequence using staggered delays. Content should flow in naturally, like turning a page in a well-designed book. Never scatter random animations.

**5. Warmth Check** — Does this feel warm and human? Or cold and mechanical? If it feels like a SaaS dashboard from 2020, start over.

**Anti-patterns in composition:**
- Centering every element (creates visual monotony)
- Uniform spacing everywhere (lacks rhythm)
- Card-heavy layouts with identical styling (looks like a template)
- No whitespace hierarchy (everything feels equally important)
- Stock illustration style (undermines editorial authenticity)

---

## 1. Design Philosophy & Core Principles

### 1.1 The Claude Aesthetic

The Claude Design System is the visual expression of Anthropic's mission: **building AI that is helpful, harmless, and honest.** The design reflects these values through warmth, clarity, and restraint.

Named after Claude Shannon, the father of information theory, Claude bridges mathematical rigor with human warmth. The visual system does the same — it is technically precise but never cold, structured but never rigid, refined but never pretentious.

**Core aesthetic pillars:**

1. **Warmth** — Sand, cream, and parchment backgrounds replace sterile white. Rust-orange accents replace cold blue. Serif typography replaces mechanical sans-serif. Every surface feels like paper, not plastic.

2. **Editorial Refinement** — The design borrows from book typography and magazine layouts. Generous margins, careful type hierarchy, pull-quotes, and asymmetric compositions create a reading experience, not a clicking experience.

3. **Restrained Elegance** — Less is more, but nothing is lazy. Every pixel serves a purpose. Shadows are multi-layered and realistic. Borders are barely-there wisps. Animations are unhurried and confident.

4. **Human-Centered Clarity** — Information is presented the way a thoughtful human would present it: clearly, in order of importance, with enough breathing room to think. The interface never rushes the user.

5. **Scientific Authenticity** — Beneath the warmth is rigorous structure. The spacing scale is mathematical. The color system is systematic. The type hierarchy is precise. Good design is invisible engineering.

### 1.2 Design Principles

1. **Warm Surfaces, Cool Content** — Backgrounds are warm and inviting (sand, cream, off-white). Content sits on these warm surfaces with clear contrast. The warmth comes from the environment, not from the content itself.

2. **Serif for Soul, Sans-Serif for Structure** — Body text, headings, and narrative content use serif typefaces to convey humanity and editorial quality. UI elements (buttons, labels, navigation, metadata) use clean sans-serif for functional clarity.

3. **Shadow as Depth** — The Claude system uses multi-layer box shadows instead of borders or color fills to create visual hierarchy. Shadows are soft, warm-tinted, and physically realistic — as if elements are paper floating above a surface.

4. **Whitespace as Content** — Generous whitespace is not empty space. It is an active design element that creates rhythm, hierarchy, and breathing room. The Claude system errs toward too much whitespace rather than too little.

5. **One Accent, Many Neutrals** — The rust-orange accent (#d97757) is the only "loud" color. Everything else is a neutral: sand, cream, charcoal, gray. This creates a signature that is instantly recognizable without being overwhelming.

6. **Progressive Disclosure** — Complex information is revealed gradually, never dumped. Sections unfold. Details expand. The interface guides the eye step by step.

### 1.3 Visual Layers

The Claude Design System uses a clear visual hierarchy through depth:

```
┌─────────────────────────────────────┐
│  LAYER 4: Overlays & Dialogs       │  ← Modals, popovers, command palettes
├─────────────────────────────────────┤
│  LAYER 3: Interactive Chrome       │  ← Navigation, sidebars, toolbars
├─────────────────────────────────────┤
│  LAYER 2: Elevated Surfaces        │  ← Cards, panels, dropdowns
├─────────────────────────────────────┤
│  LAYER 1: Content Surface          │  ← The main reading/working area
├─────────────────────────────────────┤
│  LAYER 0: Canvas                   │  ← The warm background behind everything
└─────────────────────────────────────┘
```

Each layer gets progressively elevated through shadows:
- **Layer 0 (Canvas):** The warmest, lowest surface. No shadow. `var(--color-canvas)`
- **Layer 1 (Content Surface):** Where text lives. Subtle shadow or no shadow. `var(--color-surface)`
- **Layer 2 (Elevated):** Cards and panels. Medium multi-layer shadow. `var(--color-surface-elevated)`
- **Layer 3 (Chrome):** Navigation and toolbars. Stronger shadow + border. `var(--color-chrome)`
- **Layer 4 (Overlay):** Modals and dialogs. Heavy shadow + scrim. `var(--color-overlay)`

---

## 2. Visual Foundation

### 2.1 Design Tokens Overview

All visual values are stored as CSS custom properties. Codex must never hardcode raw values — always reference tokens.

### 2.2 Color System

```css
:root {
  /* ============================================
     CLAUDE DESIGN SYSTEM — Color Tokens
     ============================================ */

  /* Canvas & Surface — the warm foundation */
  --color-canvas:             #f3f1ea;  /* Warm sand — the page itself */
  --color-surface:            #faf9f5;  /* Off-white cream — content areas */
  --color-surface-elevated:   #ffffff;  /* Pure white — elevated cards */
  --color-chrome:             #faf9f5;  /* Sidebar, nav backgrounds */
  --color-overlay:            #ffffff;  /* Modal/dialog surfaces */

  /* Text — charcoal, never pure black */
  --color-text-primary:       #141413;  /* Near-black — body text */
  --color-text-secondary:     #5c5b57;  /* Dark gray — secondary text */
  --color-text-tertiary:      #8b8983;  /* Medium gray — metadata, captions */
  --color-text-disabled:      #b0aea5;  /* Muted — disabled states */
  --color-text-inverse:       #faf9f5;  /* Light text on dark backgrounds */

  /* Accent — the signature rust-orange */
  --color-accent:             #d97757;  /* Primary accent — CTAs, links, active states */
  --color-accent-hover:       #c4613f;  /* Darker on hover */
  --color-accent-active:      #a84f2f;  /* Darkest on press */
  --color-accent-subtle:      #f5e6de;  /* Very light tint — backgrounds, badges */
  --color-accent-text:        #b85a3a;  /* Accent color with guaranteed text contrast */

  /* Secondary Accents — used sparingly */
  --color-blue:               #6a9bcc;  /* Informational, links in dark mode */
  --color-blue-subtle:        #e0ecf4;  /* Info backgrounds */
  --color-green:              #788c5d;  /* Success, positive states */
  --color-green-subtle:       #e5ead8;  /* Success backgrounds */
  --color-red:                #c44d3d;  /* Error, destructive actions */
  --color-red-subtle:         #f5dbd7;  /* Error backgrounds */
  --color-amber:              #c49132;  /* Warning states */
  --color-amber-subtle:       #f5ecd3;  /* Warning backgrounds */

  /* Borders — barely-there wisps */
  --color-border:             #e8e6dc;  /* Default border — very subtle */
  --color-border-strong:      #d0cec4;  /* Emphasized borders */
  --color-border-interactive: #b0aea5;  /* Input borders, dividers */
  --color-border-focus:       #d97757;  /* Focus ring color */

  /* Scrim & Backdrop */
  --color-scrim:              rgba(20, 20, 19, 0.50);  /* Modal backdrop */
  --color-highlight:          rgba(217, 119, 87, 0.08); /* Text selection, hover bg */
}

/* ==========================================
   DARK MODE
   ========================================== */
@media (prefers-color-scheme: dark) {
  :root {
    /* Canvas & Surface — warm dark, not cold */
    --color-canvas:             #1a1918;  /* Warm near-black */
    --color-surface:            #242320;  /* Dark warm gray */
    --color-surface-elevated:   #2e2d29;  /* Elevated dark */
    --color-chrome:             #1f1e1b;  /* Sidebar dark */
    --color-overlay:            #2e2d29;  /* Modal dark */

    /* Text — warm white, never pure white */
    --color-text-primary:       #ece9e1;  /* Warm white */
    --color-text-secondary:     #b0aea5;  /* Warm gray */
    --color-text-tertiary:      #8b8983;  /* Muted */
    --color-text-disabled:      #5c5b57;  /* Dim */
    --color-text-inverse:       #141413;  /* Dark text on light bg */

    /* Accent — slightly brighter for dark backgrounds */
    --color-accent:             #e08b6d;  /* Lighter rust-orange */
    --color-accent-hover:       #eaa189;  /* Lighter still on hover */
    --color-accent-active:      #d97757;  /* Back to standard on press */
    --color-accent-subtle:      rgba(217, 119, 87, 0.15);
    --color-accent-text:        #e8a58e;  /* Guaranteed contrast on dark */

    /* Secondary Accents — adjusted for dark */
    --color-blue:               #8cb4d8;
    --color-blue-subtle:        rgba(106, 155, 204, 0.15);
    --color-green:              #9aad7d;
    --color-green-subtle:       rgba(120, 140, 93, 0.15);
    --color-red:                #d96a5c;
    --color-red-subtle:         rgba(196, 77, 61, 0.15);
    --color-amber:              #d4a54e;
    --color-amber-subtle:       rgba(196, 145, 50, 0.15);

    /* Borders */
    --color-border:             rgba(255, 255, 255, 0.08);
    --color-border-strong:      rgba(255, 255, 255, 0.15);
    --color-border-interactive: rgba(255, 255, 255, 0.20);
    --color-border-focus:       #e08b6d;

    /* Scrim */
    --color-scrim:              rgba(0, 0, 0, 0.65);
    --color-highlight:          rgba(224, 139, 109, 0.12);
  }
}
```

### 2.3 Typography

The Claude typographic system pairs **serif** for soul with **sans-serif** for structure.

**Brand Fonts (commercial):**
- Headlines/Body: **Tiempos** (Klim Type Foundry) — warm, literary serif
- UI/Labels: **Styrene** (Commercial Type) — geometric, slightly quirky sans-serif

**Web Equivalents (free, Google Fonts):**
- Headlines/Body: **Lora** — warm, brushed serif with excellent screen readability
- UI/Labels: **Poppins** — geometric sans-serif with friendly personality
- Code: **Fira Code** or **JetBrains Mono** — with ligatures

```css
:root {
  /* Font Families */
  --font-serif:      'Lora', 'Tiempos Text', Georgia, 'Times New Roman', serif;
  --font-sans:       'Poppins', 'Styrene A', -apple-system, BlinkMacSystemFont, sans-serif;
  --font-mono:       'Fira Code', 'JetBrains Mono', 'SF Mono', 'Cascadia Code', monospace;

  /* Font loading — Google Fonts import */
  /* @import url('https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,400;0,500;0,600;0,700;1,400;1,500&family=Poppins:wght@300;400;500;600;700&family=Fira+Code:wght@400;500&display=swap'); */

  /* Type Scale — modular (1.250 ratio, "Major Third") */
  --text-xs:         0.64rem;    /* 10.24px — fine print */
  --text-sm:         0.8rem;     /* 12.8px — captions, metadata */
  --text-base:       1rem;       /* 16px — body text */
  --text-md:         1.125rem;   /* 18px — lead paragraphs */
  --text-lg:         1.25rem;    /* 20px — section intros */
  --text-xl:         1.563rem;   /* 25px — h4 */
  --text-2xl:        1.953rem;   /* 31.25px — h3 */
  --text-3xl:        2.441rem;   /* 39px — h2 */
  --text-4xl:        3.052rem;   /* 48.8px — h1 */
  --text-5xl:        3.815rem;   /* 61px — hero display */

  /* Line Heights */
  --leading-tight:   1.2;   /* Headings */
  --leading-snug:    1.35;  /* Subheadings, large text */
  --leading-normal:  1.6;   /* Body text — generous for readability */
  --leading-relaxed: 1.75;  /* Long-form reading */
  --leading-loose:   2.0;   /* Spacious, editorial */

  /* Letter Spacing */
  --tracking-tight:   -0.02em;  /* Large headings */
  --tracking-normal:   0;       /* Body */
  --tracking-wide:     0.02em;  /* Small caps, labels */
  --tracking-wider:    0.05em;  /* Uppercase UI labels */
  --tracking-widest:   0.1em;   /* All-caps section labels */

  /* Font Weights */
  --weight-regular:  400;
  --weight-medium:   500;
  --weight-semibold: 600;
  --weight-bold:     700;
}
```

**Typography Rules:**

| Element | Font | Size | Weight | Leading | Tracking | Color |
|---------|------|------|--------|---------|----------|-------|
| Hero Display | Serif | --text-5xl | 700 | --leading-tight | --tracking-tight | --color-text-primary |
| H1 | Serif | --text-4xl | 700 | --leading-tight | --tracking-tight | --color-text-primary |
| H2 | Serif | --text-3xl | 600 | --leading-tight | --tracking-tight | --color-text-primary |
| H3 | Serif | --text-2xl | 600 | --leading-snug | normal | --color-text-primary |
| H4 | Sans | --text-xl | 600 | --leading-snug | normal | --color-text-primary |
| Body | Serif | --text-base | 400 | --leading-normal | normal | --color-text-primary |
| Body Lead | Serif | --text-md | 400 | --leading-relaxed | normal | --color-text-secondary |
| Caption | Sans | --text-sm | 400 | --leading-normal | --tracking-wide | --color-text-tertiary |
| Overline | Sans | --text-xs | 600 | --leading-normal | --tracking-widest | --color-text-tertiary |
| Button Label | Sans | --text-sm | 500 | 1 | --tracking-wide | (varies) |
| Input | Serif | --text-base | 400 | --leading-normal | normal | --color-text-primary |
| Code | Mono | --text-sm | 400 | --leading-relaxed | normal | --color-text-primary |

### 2.4 Spacing System

The Claude spacing system uses an 4px base with a balanced scale:

```css
:root {
  /* Spacing Scale — 4px base */
  --space-0:    0;
  --space-1:    0.25rem;   /* 4px */
  --space-2:    0.5rem;    /* 8px */
  --space-3:    0.75rem;   /* 12px */
  --space-4:    1rem;      /* 16px */
  --space-5:    1.25rem;   /* 20px */
  --space-6:    1.5rem;    /* 24px */
  --space-8:    2rem;      /* 32px */
  --space-10:   2.5rem;    /* 40px */
  --space-12:   3rem;      /* 48px */
  --space-16:   4rem;      /* 64px */
  --space-20:   5rem;      /* 80px */
  --space-24:   6rem;      /* 96px */
  --space-32:   8rem;      /* 128px */
  --space-40:   10rem;     /* 160px */

  /* Semantic Spacing */
  --gap-inline:     var(--space-2);   /* Between inline elements */
  --gap-stack:      var(--space-4);   /* Between stacked elements */
  --gap-section:    var(--space-16);  /* Between page sections */
  --padding-card:   var(--space-6);   /* Card internal padding */
  --padding-page:   var(--space-8);   /* Page edge padding */
  --padding-section: var(--space-12); /* Section vertical padding */
}
```

**Spacing Philosophy:** The Claude system is generous. When debating between two spacing values, always choose the larger one. Breathing room is a feature, not waste.

### 2.5 Border Radius

```css
:root {
  /* Radius Scale */
  --radius-none:   0;
  --radius-xs:     2px;    /* Barely rounded — code blocks, small badges */
  --radius-sm:     4px;    /* Subtle — inputs, small buttons */
  --radius-md:     8px;    /* Default — cards, medium components */
  --radius-lg:     12px;   /* Prominent — large cards, panels */
  --radius-xl:     16px;   /* Feature cards, hero elements */
  --radius-2xl:    24px;   /* Pills, large feature panels */
  --radius-full:   9999px; /* Circular — avatars, badges, toggles */
}
```

**Radius Philosophy:** Claude's radii are subtler than most modern systems. The design avoids aggressively rounded "pillowy" components. Slight rounding humanizes sharp edges without becoming cartoonish.

### 2.6 Shadow System

Shadows are the primary depth mechanism in the Claude Design System. They replace borders and background fills as the main way to show elevation.

```css
:root {
  /* Shadow Scale — warm-tinted, multi-layer */
  --shadow-xs:     0 1px 2px rgba(20, 20, 19, 0.04);
  --shadow-sm:     0 1px 3px rgba(20, 20, 19, 0.06),
                   0 1px 2px rgba(20, 20, 19, 0.04);
  --shadow-md:     0 4px 6px rgba(20, 20, 19, 0.05),
                   0 2px 4px rgba(20, 20, 19, 0.03),
                   0 1px 2px rgba(20, 20, 19, 0.02);
  --shadow-lg:     0 10px 15px rgba(20, 20, 19, 0.06),
                   0 4px 6px rgba(20, 20, 19, 0.04),
                   0 2px 4px rgba(20, 20, 19, 0.02);
  --shadow-xl:     0 20px 25px rgba(20, 20, 19, 0.08),
                   0 8px 10px rgba(20, 20, 19, 0.04),
                   0 4px 6px rgba(20, 20, 19, 0.02);
  --shadow-2xl:    0 25px 50px rgba(20, 20, 19, 0.12),
                   0 12px 24px rgba(20, 20, 19, 0.06);

  /* Specialty Shadows */
  --shadow-card:   var(--shadow-md);
  --shadow-dropdown: var(--shadow-lg);
  --shadow-modal:  var(--shadow-2xl);
  --shadow-button: 0 1px 2px rgba(20, 20, 19, 0.06),
                   0 1px 3px rgba(20, 20, 19, 0.08);
  --shadow-button-hover: 0 2px 4px rgba(20, 20, 19, 0.08),
                         0 4px 8px rgba(20, 20, 19, 0.06);
  --shadow-input:  0 1px 2px rgba(20, 20, 19, 0.04) inset;
  --shadow-focus:  0 0 0 3px rgba(217, 119, 87, 0.25);

  /* Glow (for accent elements in dark mode) */
  --shadow-accent-glow: 0 0 20px rgba(217, 119, 87, 0.15),
                         0 0 8px rgba(217, 119, 87, 0.10);
}

@media (prefers-color-scheme: dark) {
  :root {
    --shadow-xs:     0 1px 2px rgba(0, 0, 0, 0.20);
    --shadow-sm:     0 1px 3px rgba(0, 0, 0, 0.30),
                     0 1px 2px rgba(0, 0, 0, 0.20);
    --shadow-md:     0 4px 6px rgba(0, 0, 0, 0.30),
                     0 2px 4px rgba(0, 0, 0, 0.20),
                     0 1px 2px rgba(0, 0, 0, 0.15);
    --shadow-lg:     0 10px 15px rgba(0, 0, 0, 0.35),
                     0 4px 6px rgba(0, 0, 0, 0.25),
                     0 2px 4px rgba(0, 0, 0, 0.15);
    --shadow-xl:     0 20px 25px rgba(0, 0, 0, 0.40),
                     0 8px 10px rgba(0, 0, 0, 0.25),
                     0 4px 6px rgba(0, 0, 0, 0.15);
    --shadow-2xl:    0 25px 50px rgba(0, 0, 0, 0.50),
                     0 12px 24px rgba(0, 0, 0, 0.30);

    --shadow-accent-glow: 0 0 30px rgba(224, 139, 109, 0.20),
                           0 0 12px rgba(224, 139, 109, 0.15);
  }
}
```

**Shadow Philosophy:** Claude shadows are warm (tinted with `rgba(20, 20, 19, ...)` not cold `rgba(0, 0, 0, ...)`). They use multiple layers for realism — a large diffuse shadow + a small sharp shadow + a contact shadow, mimicking real paper hovering above a desk.

### 2.7 Z-Index Scale

```css
:root {
  --z-below:       -1;
  --z-base:        0;
  --z-raised:      10;
  --z-dropdown:    100;
  --z-sticky:      200;
  --z-sidebar:     300;
  --z-header:      400;
  --z-overlay:     500;
  --z-modal:       600;
  --z-popover:     700;
  --z-toast:       800;
  --z-tooltip:     900;
  --z-max:         9999;
}
```

### 2.8 Animation Tokens

```css
:root {
  /* Duration */
  --duration-instant: 0ms;
  --duration-fast:    100ms;
  --duration-normal:  200ms;
  --duration-slow:    350ms;
  --duration-slower:  500ms;
  --duration-slowest: 800ms;

  /* Easing — Claude uses gentle, confident curves */
  --ease-default:    cubic-bezier(0.25, 0.1, 0.25, 1.0);  /* Smooth decel */
  --ease-in:         cubic-bezier(0.4, 0, 1, 1);            /* Accelerate */
  --ease-out:        cubic-bezier(0, 0, 0.2, 1);            /* Decelerate */
  --ease-in-out:     cubic-bezier(0.4, 0, 0.2, 1);          /* Balanced */
  --ease-spring:     cubic-bezier(0.34, 1.56, 0.64, 1);     /* Slight bounce */
  --ease-editorial:  cubic-bezier(0.16, 1, 0.3, 1);         /* Fast start, gentle land */

  /* Stagger — for sequential element reveals */
  --stagger-step:    60ms;
}
```

---

## 3. CSS Implementation

### 3.1 Base Reset & Foundation

```css
/* Claude Design System — Base */
@import url('https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,400;0,500;0,600;0,700;1,400;1,500&family=Poppins:wght@300;400;500;600;700&family=Fira+Code:wght@400;500&display=swap');

*,
*::before,
*::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

html {
  font-size: 16px;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-rendering: optimizeLegibility;
  scroll-behavior: smooth;
  color-scheme: light dark;
}

body {
  font-family: var(--font-serif);
  font-size: var(--text-base);
  font-weight: var(--weight-regular);
  line-height: var(--leading-normal);
  color: var(--color-text-primary);
  background-color: var(--color-canvas);
  min-height: 100dvh;
}

/* Selection color — warm accent */
::selection {
  background-color: var(--color-highlight);
  color: var(--color-text-primary);
}

/* Focus visible — the signature orange ring */
:focus-visible {
  outline: 2px solid var(--color-border-focus);
  outline-offset: 2px;
  border-radius: var(--radius-sm);
}

/* Smooth scroll respects reduced-motion */
@media (prefers-reduced-motion: reduce) {
  html { scroll-behavior: auto; }
  *,
  *::before,
  *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}
```

### 3.2 Typography Styles

```css
/* Headings — Serif by default */
h1, h2, h3 {
  font-family: var(--font-serif);
  color: var(--color-text-primary);
  letter-spacing: var(--tracking-tight);
  line-height: var(--leading-tight);
}

h4, h5, h6 {
  font-family: var(--font-sans);
  color: var(--color-text-primary);
  line-height: var(--leading-snug);
}

h1 { font-size: var(--text-4xl); font-weight: var(--weight-bold); }
h2 { font-size: var(--text-3xl); font-weight: var(--weight-semibold); }
h3 { font-size: var(--text-2xl); font-weight: var(--weight-semibold); }
h4 { font-size: var(--text-xl); font-weight: var(--weight-semibold); }
h5 { font-size: var(--text-lg); font-weight: var(--weight-medium); }
h6 { font-size: var(--text-md); font-weight: var(--weight-medium); }

/* Body text */
p {
  font-family: var(--font-serif);
  font-size: var(--text-base);
  line-height: var(--leading-normal);
  color: var(--color-text-primary);
  max-width: 65ch; /* Optimal reading line length */
}

/* Lead paragraph */
.text-lead {
  font-size: var(--text-md);
  line-height: var(--leading-relaxed);
  color: var(--color-text-secondary);
}

/* Small / metadata text */
small, .text-sm {
  font-family: var(--font-sans);
  font-size: var(--text-sm);
  line-height: var(--leading-normal);
  color: var(--color-text-tertiary);
}

/* Overline label */
.overline {
  font-family: var(--font-sans);
  font-size: var(--text-xs);
  font-weight: var(--weight-semibold);
  letter-spacing: var(--tracking-widest);
  text-transform: uppercase;
  color: var(--color-text-tertiary);
}

/* Links */
a {
  color: var(--color-accent-text);
  text-decoration: underline;
  text-decoration-color: rgba(217, 119, 87, 0.30);
  text-underline-offset: 3px;
  text-decoration-thickness: 1px;
  transition: color var(--duration-fast) var(--ease-default),
              text-decoration-color var(--duration-fast) var(--ease-default);
}

a:hover {
  color: var(--color-accent-hover);
  text-decoration-color: var(--color-accent-hover);
}

/* Code */
code {
  font-family: var(--font-mono);
  font-size: 0.875em;
  padding: 0.15em 0.4em;
  background: var(--color-highlight);
  border-radius: var(--radius-xs);
  color: var(--color-text-primary);
}

pre {
  font-family: var(--font-mono);
  font-size: var(--text-sm);
  line-height: var(--leading-relaxed);
  background: var(--color-surface-elevated);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-md);
  padding: var(--space-4);
  overflow-x: auto;
}

pre code {
  background: none;
  padding: 0;
  border-radius: 0;
}

/* Blockquote — editorial pull-quote style */
blockquote {
  font-family: var(--font-serif);
  font-size: var(--text-lg);
  font-style: italic;
  line-height: var(--leading-relaxed);
  color: var(--color-text-secondary);
  border-left: 3px solid var(--color-accent);
  padding-left: var(--space-6);
  margin: var(--space-8) 0;
}
```

### 3.3 Accessibility Fallbacks

```css
/* High contrast mode */
@media (prefers-contrast: high) {
  :root {
    --color-text-primary:    #000000;
    --color-text-secondary:  #1a1a1a;
    --color-border:          #333333;
    --color-border-strong:   #000000;
    --color-accent:          #b84a2d;
    --shadow-card:           0 0 0 2px #333333;
  }
}

/* Forced colors (Windows High Contrast) */
@media (forced-colors: active) {
  * {
    border-color: CanvasText !important;
  }
  .card,
  .button {
    border: 1px solid CanvasText;
  }
}

/* Reduced motion — disable all animations */
@media (prefers-reduced-motion: reduce) {
  .animate-in,
  .stagger-in > * {
    opacity: 1 !important;
    transform: none !important;
  }
}
```

---

## 4. Animation & Motion

### 4.1 Motion Philosophy

Claude animations are **unhurried and confident**. They borrow from editorial design: pages turn, content fades in like ink appearing on paper, elements settle into place with the weight of real objects.

**Rules:**
1. **One orchestrated entrance per page** — stagger-reveal the main content groups. Don't animate every element individually.
2. **No bouncing** — Claude motion is elegant, not playful. The `--ease-editorial` curve (fast start, gentle land) is the default.
3. **Short durations** — most transitions are 200-350ms. Only page-level entrances use 500ms+.
4. **Opacity + translate only** — avoid scale, rotate, or other transforms that feel "techie". Content should feel like it's fading in and settling, not flying in.
5. **Respect reduced-motion** — always wrap animations in `@media (prefers-reduced-motion: no-preference)`.

### 4.2 Core Animations

```css
/* Fade in from below — the workhorse entrance */
@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(12px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

/* Fade in — no movement, just appear */
@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}

/* Slide in from left — sidebar, panel entrance */
@keyframes slideInLeft {
  from {
    opacity: 0;
    transform: translateX(-16px);
  }
  to {
    opacity: 1;
    transform: translateX(0);
  }
}

/* Settle — slight downward movement, like paper landing */
@keyframes settle {
  from {
    opacity: 0;
    transform: translateY(-4px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

/* Scale in — for modals, dialogs */
@keyframes scaleIn {
  from {
    opacity: 0;
    transform: scale(0.95);
  }
  to {
    opacity: 1;
    transform: scale(1);
  }
}

/* Application classes */
@media (prefers-reduced-motion: no-preference) {
  .animate-in {
    animation: fadeInUp var(--duration-slow) var(--ease-editorial) both;
  }

  .animate-fade {
    animation: fadeIn var(--duration-normal) var(--ease-default) both;
  }

  .animate-slide-left {
    animation: slideInLeft var(--duration-slow) var(--ease-editorial) both;
  }

  .animate-settle {
    animation: settle var(--duration-normal) var(--ease-out) both;
  }

  .animate-scale {
    animation: scaleIn var(--duration-slow) var(--ease-spring) both;
  }
}
```

### 4.3 Stagger System

```css
/* Stagger — apply to parent, children auto-delay */
@media (prefers-reduced-motion: no-preference) {
  .stagger-in > * {
    opacity: 0;
    animation: fadeInUp var(--duration-slow) var(--ease-editorial) both;
  }

  .stagger-in > *:nth-child(1) { animation-delay: 0ms; }
  .stagger-in > *:nth-child(2) { animation-delay: calc(var(--stagger-step) * 1); }
  .stagger-in > *:nth-child(3) { animation-delay: calc(var(--stagger-step) * 2); }
  .stagger-in > *:nth-child(4) { animation-delay: calc(var(--stagger-step) * 3); }
  .stagger-in > *:nth-child(5) { animation-delay: calc(var(--stagger-step) * 4); }
  .stagger-in > *:nth-child(6) { animation-delay: calc(var(--stagger-step) * 5); }
  .stagger-in > *:nth-child(7) { animation-delay: calc(var(--stagger-step) * 6); }
  .stagger-in > *:nth-child(8) { animation-delay: calc(var(--stagger-step) * 7); }

  /* Cap at 8 — beyond this, just appear */
  .stagger-in > *:nth-child(n+9) {
    animation-delay: calc(var(--stagger-step) * 8);
  }
}
```

### 4.4 Hover & Interaction Transitions

```css
/* Card hover — subtle lift */
.card {
  transition: box-shadow var(--duration-normal) var(--ease-default),
              transform var(--duration-normal) var(--ease-default);
}
.card:hover {
  box-shadow: var(--shadow-lg);
  transform: translateY(-2px);
}

/* Button hover */
.button {
  transition: background-color var(--duration-fast) var(--ease-default),
              box-shadow var(--duration-fast) var(--ease-default),
              transform var(--duration-fast) var(--ease-default);
}
.button:hover {
  box-shadow: var(--shadow-button-hover);
  transform: translateY(-1px);
}
.button:active {
  transform: translateY(0);
  box-shadow: var(--shadow-xs);
}

/* Link underline expand */
.link-animated {
  text-decoration: none;
  background-image: linear-gradient(var(--color-accent), var(--color-accent));
  background-size: 0% 1px;
  background-position: left bottom;
  background-repeat: no-repeat;
  transition: background-size var(--duration-slow) var(--ease-editorial);
}
.link-animated:hover {
  background-size: 100% 1px;
}
```

---

## 5. Component Library

### 5.1 Card

The card is the fundamental content container in the Claude Design System.

```css
.card {
  background: var(--color-surface-elevated);
  border-radius: var(--radius-lg);
  padding: var(--padding-card);
  box-shadow: var(--shadow-card);
  border: 1px solid var(--color-border);
  transition: box-shadow var(--duration-normal) var(--ease-default),
              transform var(--duration-normal) var(--ease-default);
}

.card:hover {
  box-shadow: var(--shadow-lg);
  transform: translateY(-2px);
}

/* Card without hover effect — for static content */
.card--static {
  composes: card;
  cursor: default;
}
.card--static:hover {
  box-shadow: var(--shadow-card);
  transform: none;
}

/* Accent-bordered card */
.card--accent {
  border-left: 3px solid var(--color-accent);
}

/* Flush card — no padding (for images, custom layouts) */
.card--flush {
  padding: 0;
}

/* Card sections */
.card__header {
  padding-bottom: var(--space-4);
  border-bottom: 1px solid var(--color-border);
  margin-bottom: var(--space-4);
}

.card__body {
  /* No specific styles — inherits card padding */
}

.card__footer {
  padding-top: var(--space-4);
  border-top: 1px solid var(--color-border);
  margin-top: var(--space-4);
  display: flex;
  align-items: center;
  justify-content: flex-end;
  gap: var(--space-3);
}

.card__title {
  font-family: var(--font-serif);
  font-size: var(--text-xl);
  font-weight: var(--weight-semibold);
  color: var(--color-text-primary);
  line-height: var(--leading-snug);
  margin: 0;
}

.card__description {
  font-family: var(--font-serif);
  font-size: var(--text-base);
  color: var(--color-text-secondary);
  line-height: var(--leading-normal);
  margin-top: var(--space-2);
}

.card__meta {
  font-family: var(--font-sans);
  font-size: var(--text-sm);
  color: var(--color-text-tertiary);
  display: flex;
  align-items: center;
  gap: var(--space-2);
}
```

```html
<article class="card" role="article">
  <div class="card__header">
    <span class="overline">Research Paper</span>
    <h3 class="card__title">Constitutional AI: Harmlessness from AI Feedback</h3>
    <p class="card__description">An approach to training AI systems to be helpful and harmless without relying on human labels for harmlessness.</p>
  </div>
  <div class="card__body">
    <p>We present a method for training a harmless AI assistant...</p>
  </div>
  <div class="card__footer">
    <span class="card__meta">Dec 2022</span>
    <a href="#" class="button button--secondary">Read more</a>
  </div>
</article>
```

### 5.2 Button

```css
/* Base button — all variants inherit from this */
.button {
  font-family: var(--font-sans);
  font-size: var(--text-sm);
  font-weight: var(--weight-medium);
  letter-spacing: var(--tracking-wide);
  line-height: 1;
  padding: var(--space-3) var(--space-5);
  border-radius: var(--radius-md);
  border: 1px solid transparent;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: var(--space-2);
  text-decoration: none;
  transition: background-color var(--duration-fast) var(--ease-default),
              box-shadow var(--duration-fast) var(--ease-default),
              transform var(--duration-fast) var(--ease-default),
              border-color var(--duration-fast) var(--ease-default);
}

.button:focus-visible {
  outline: 2px solid var(--color-border-focus);
  outline-offset: 2px;
}

.button:disabled {
  opacity: 0.5;
  cursor: not-allowed;
  pointer-events: none;
}

/* Primary — filled with accent */
.button--primary {
  background-color: var(--color-accent);
  color: white;
  box-shadow: var(--shadow-button);
}

.button--primary:hover {
  background-color: var(--color-accent-hover);
  box-shadow: var(--shadow-button-hover);
  transform: translateY(-1px);
}

.button--primary:active {
  background-color: var(--color-accent-active);
  transform: translateY(0);
  box-shadow: var(--shadow-xs);
}

/* Secondary — outlined */
.button--secondary {
  background-color: transparent;
  color: var(--color-text-primary);
  border-color: var(--color-border-strong);
}

.button--secondary:hover {
  background-color: var(--color-highlight);
  border-color: var(--color-border-interactive);
}

.button--secondary:active {
  background-color: var(--color-accent-subtle);
}

/* Ghost — no border, minimal */
.button--ghost {
  background-color: transparent;
  color: var(--color-text-secondary);
}

.button--ghost:hover {
  background-color: var(--color-highlight);
  color: var(--color-text-primary);
}

/* Destructive */
.button--destructive {
  background-color: var(--color-red);
  color: white;
  box-shadow: var(--shadow-button);
}

.button--destructive:hover {
  background-color: #b3413a;
  box-shadow: var(--shadow-button-hover);
  transform: translateY(-1px);
}

/* Sizes */
.button--sm {
  font-size: var(--text-xs);
  padding: var(--space-2) var(--space-3);
}

.button--lg {
  font-size: var(--text-base);
  padding: var(--space-4) var(--space-8);
  border-radius: var(--radius-lg);
}

/* Icon button — square */
.button--icon {
  padding: var(--space-3);
  aspect-ratio: 1;
}
```

### 5.3 Navigation Bar

```css
.navbar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: var(--space-3) var(--space-6);
  background: var(--color-chrome);
  border-bottom: 1px solid var(--color-border);
  position: sticky;
  top: 0;
  z-index: var(--z-header);
  min-height: 56px;
}

.navbar__brand {
  display: flex;
  align-items: center;
  gap: var(--space-3);
  text-decoration: none;
  color: var(--color-text-primary);
}

.navbar__brand-name {
  font-family: var(--font-sans);
  font-size: var(--text-lg);
  font-weight: var(--weight-semibold);
  letter-spacing: var(--tracking-tight);
}

.navbar__nav {
  display: flex;
  align-items: center;
  gap: var(--space-1);
  list-style: none;
}

.navbar__link {
  font-family: var(--font-sans);
  font-size: var(--text-sm);
  font-weight: var(--weight-medium);
  color: var(--color-text-secondary);
  text-decoration: none;
  padding: var(--space-2) var(--space-3);
  border-radius: var(--radius-md);
  transition: color var(--duration-fast) var(--ease-default),
              background-color var(--duration-fast) var(--ease-default);
}

.navbar__link:hover {
  color: var(--color-text-primary);
  background-color: var(--color-highlight);
}

.navbar__link--active {
  color: var(--color-accent-text);
  background-color: var(--color-accent-subtle);
}

.navbar__actions {
  display: flex;
  align-items: center;
  gap: var(--space-2);
}
```

### 5.4 Sidebar

```css
.sidebar {
  width: 280px;
  min-width: 280px;
  background: var(--color-chrome);
  border-right: 1px solid var(--color-border);
  display: flex;
  flex-direction: column;
  height: 100dvh;
  position: sticky;
  top: 0;
  overflow-y: auto;
  z-index: var(--z-sidebar);
  padding: var(--space-4) var(--space-3);
}

.sidebar__section {
  margin-bottom: var(--space-6);
}

.sidebar__section-title {
  font-family: var(--font-sans);
  font-size: var(--text-xs);
  font-weight: var(--weight-semibold);
  letter-spacing: var(--tracking-widest);
  text-transform: uppercase;
  color: var(--color-text-tertiary);
  padding: var(--space-2) var(--space-3);
  margin-bottom: var(--space-1);
}

.sidebar__item {
  display: flex;
  align-items: center;
  gap: var(--space-3);
  padding: var(--space-2) var(--space-3);
  border-radius: var(--radius-md);
  font-family: var(--font-sans);
  font-size: var(--text-sm);
  color: var(--color-text-secondary);
  text-decoration: none;
  cursor: pointer;
  transition: background-color var(--duration-fast) var(--ease-default),
              color var(--duration-fast) var(--ease-default);
}

.sidebar__item:hover {
  background-color: var(--color-highlight);
  color: var(--color-text-primary);
}

.sidebar__item--active {
  background-color: var(--color-accent-subtle);
  color: var(--color-accent-text);
  font-weight: var(--weight-medium);
}
```

### 5.5 Badge

```css
.badge {
  font-family: var(--font-sans);
  font-size: var(--text-xs);
  font-weight: var(--weight-medium);
  letter-spacing: var(--tracking-wide);
  padding: var(--space-1) var(--space-2);
  border-radius: var(--radius-full);
  display: inline-flex;
  align-items: center;
  gap: var(--space-1);
  line-height: 1;
  white-space: nowrap;
}

.badge--default {
  background: var(--color-border);
  color: var(--color-text-secondary);
}

.badge--accent {
  background: var(--color-accent-subtle);
  color: var(--color-accent-text);
}

.badge--success {
  background: var(--color-green-subtle);
  color: var(--color-green);
}

.badge--error {
  background: var(--color-red-subtle);
  color: var(--color-red);
}

.badge--warning {
  background: var(--color-amber-subtle);
  color: var(--color-amber);
}

.badge--info {
  background: var(--color-blue-subtle);
  color: var(--color-blue);
}
```

### 5.6 Avatar

```css
.avatar {
  width: 40px;
  height: 40px;
  border-radius: var(--radius-full);
  overflow: hidden;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
  background: var(--color-accent-subtle);
  color: var(--color-accent-text);
  font-family: var(--font-sans);
  font-weight: var(--weight-semibold);
  font-size: var(--text-sm);
}

.avatar--sm { width: 32px; height: 32px; font-size: var(--text-xs); }
.avatar--lg { width: 56px; height: 56px; font-size: var(--text-lg); }
.avatar--xl { width: 80px; height: 80px; font-size: var(--text-2xl); }

.avatar img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

/* Avatar group — overlapping */
.avatar-group {
  display: flex;
}

.avatar-group .avatar {
  border: 2px solid var(--color-surface-elevated);
  margin-left: -8px;
}

.avatar-group .avatar:first-child {
  margin-left: 0;
}
```

### 5.7 Divider

```css
.divider {
  border: 0;
  border-top: 1px solid var(--color-border);
  margin: var(--space-6) 0;
}

.divider--subtle {
  border-color: var(--color-border);
  opacity: 0.5;
}

.divider--strong {
  border-color: var(--color-border-strong);
}

/* Divider with text */
.divider--text {
  display: flex;
  align-items: center;
  gap: var(--space-4);
  color: var(--color-text-tertiary);
  font-family: var(--font-sans);
  font-size: var(--text-xs);
  letter-spacing: var(--tracking-wider);
  text-transform: uppercase;
}

.divider--text::before,
.divider--text::after {
  content: '';
  flex: 1;
  border-top: 1px solid var(--color-border);
}
```

### 5.8 Modal / Dialog

```css
/* Scrim backdrop */
.modal-scrim {
  position: fixed;
  inset: 0;
  background: var(--color-scrim);
  z-index: var(--z-modal);
  display: flex;
  align-items: center;
  justify-content: center;
  padding: var(--space-6);
  animation: fadeIn var(--duration-normal) var(--ease-default) both;
}

.modal {
  background: var(--color-overlay);
  border-radius: var(--radius-xl);
  box-shadow: var(--shadow-modal);
  width: 100%;
  max-width: 520px;
  max-height: 85dvh;
  overflow-y: auto;
  animation: scaleIn var(--duration-slow) var(--ease-spring) both;
}

.modal__header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: var(--space-5) var(--space-6);
  border-bottom: 1px solid var(--color-border);
}

.modal__title {
  font-family: var(--font-serif);
  font-size: var(--text-xl);
  font-weight: var(--weight-semibold);
  color: var(--color-text-primary);
}

.modal__close {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 36px;
  height: 36px;
  border-radius: var(--radius-md);
  border: none;
  background: transparent;
  color: var(--color-text-tertiary);
  cursor: pointer;
  transition: background-color var(--duration-fast) var(--ease-default);
}

.modal__close:hover {
  background: var(--color-highlight);
  color: var(--color-text-primary);
}

.modal__body {
  padding: var(--space-6);
}

.modal__footer {
  display: flex;
  align-items: center;
  justify-content: flex-end;
  gap: var(--space-3);
  padding: var(--space-4) var(--space-6);
  border-top: 1px solid var(--color-border);
}
```

### 5.9 Tooltip

```css
.tooltip {
  position: relative;
}

.tooltip__content {
  position: absolute;
  bottom: calc(100% + 8px);
  left: 50%;
  transform: translateX(-50%);
  background: var(--color-text-primary);
  color: var(--color-text-inverse);
  font-family: var(--font-sans);
  font-size: var(--text-xs);
  font-weight: var(--weight-medium);
  padding: var(--space-2) var(--space-3);
  border-radius: var(--radius-md);
  white-space: nowrap;
  pointer-events: none;
  opacity: 0;
  z-index: var(--z-tooltip);
  transition: opacity var(--duration-fast) var(--ease-default);
}

.tooltip:hover .tooltip__content,
.tooltip:focus-within .tooltip__content {
  opacity: 1;
}

/* Arrow */
.tooltip__content::after {
  content: '';
  position: absolute;
  top: 100%;
  left: 50%;
  transform: translateX(-50%);
  border: 4px solid transparent;
  border-top-color: var(--color-text-primary);
}
```

---

## 6. Form Elements

### 6.1 Text Input

```css
.input-group {
  display: flex;
  flex-direction: column;
  gap: var(--space-2);
}

.input-label {
  font-family: var(--font-sans);
  font-size: var(--text-sm);
  font-weight: var(--weight-medium);
  color: var(--color-text-primary);
}

.input-label--required::after {
  content: ' *';
  color: var(--color-red);
}

.input {
  font-family: var(--font-serif);
  font-size: var(--text-base);
  line-height: var(--leading-normal);
  color: var(--color-text-primary);
  background: var(--color-surface-elevated);
  border: 1px solid var(--color-border-interactive);
  border-radius: var(--radius-md);
  padding: var(--space-3) var(--space-4);
  box-shadow: var(--shadow-input);
  transition: border-color var(--duration-fast) var(--ease-default),
              box-shadow var(--duration-fast) var(--ease-default);
  width: 100%;
}

.input::placeholder {
  color: var(--color-text-disabled);
}

.input:hover {
  border-color: var(--color-border-strong);
}

.input:focus {
  outline: none;
  border-color: var(--color-border-focus);
  box-shadow: var(--shadow-focus);
}

.input--error {
  border-color: var(--color-red);
}

.input--error:focus {
  box-shadow: 0 0 0 3px rgba(196, 77, 61, 0.25);
}

.input-hint {
  font-family: var(--font-sans);
  font-size: var(--text-xs);
  color: var(--color-text-tertiary);
}

.input-error-message {
  font-family: var(--font-sans);
  font-size: var(--text-xs);
  color: var(--color-red);
}
```

```html
<div class="input-group">
  <label class="input-label input-label--required" for="email">Email address</label>
  <input class="input" type="email" id="email" placeholder="you@example.com" aria-required="true" />
  <span class="input-hint">We'll never share your email.</span>
</div>
```

### 6.2 Textarea

```css
.textarea {
  composes: input;
  min-height: 120px;
  resize: vertical;
  line-height: var(--leading-relaxed);
}
```

### 6.3 Select

```css
.select {
  composes: input;
  appearance: none;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' height='16' viewBox='0 0 24 24' fill='none' stroke='%235c5b57' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpolyline points='6 9 12 15 18 9'/%3E%3C/svg%3E");
  background-repeat: no-repeat;
  background-position: right var(--space-3) center;
  padding-right: var(--space-10);
  cursor: pointer;
}
```

### 6.4 Checkbox

```css
.checkbox-group {
  display: flex;
  align-items: flex-start;
  gap: var(--space-3);
  cursor: pointer;
}

.checkbox {
  appearance: none;
  width: 18px;
  height: 18px;
  border: 1.5px solid var(--color-border-interactive);
  border-radius: var(--radius-xs);
  background: var(--color-surface-elevated);
  cursor: pointer;
  flex-shrink: 0;
  margin-top: 2px;
  transition: background-color var(--duration-fast) var(--ease-default),
              border-color var(--duration-fast) var(--ease-default);
}

.checkbox:checked {
  background-color: var(--color-accent);
  border-color: var(--color-accent);
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='12' viewBox='0 0 24 24' fill='none' stroke='white' stroke-width='3' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpolyline points='20 6 9 17 4 12'/%3E%3C/svg%3E");
  background-position: center;
  background-repeat: no-repeat;
}

.checkbox:focus-visible {
  box-shadow: var(--shadow-focus);
}

.checkbox-label {
  font-family: var(--font-serif);
  font-size: var(--text-base);
  color: var(--color-text-primary);
  line-height: var(--leading-normal);
}
```

### 6.5 Radio

```css
.radio {
  appearance: none;
  width: 18px;
  height: 18px;
  border: 1.5px solid var(--color-border-interactive);
  border-radius: var(--radius-full);
  background: var(--color-surface-elevated);
  cursor: pointer;
  flex-shrink: 0;
  margin-top: 2px;
  transition: border-color var(--duration-fast) var(--ease-default);
}

.radio:checked {
  border-color: var(--color-accent);
  border-width: 5px;
}

.radio:focus-visible {
  box-shadow: var(--shadow-focus);
}
```

### 6.6 Toggle / Switch

```css
.toggle {
  appearance: none;
  width: 44px;
  height: 24px;
  border-radius: var(--radius-full);
  background: var(--color-border-interactive);
  cursor: pointer;
  position: relative;
  flex-shrink: 0;
  transition: background-color var(--duration-normal) var(--ease-default);
}

.toggle::after {
  content: '';
  position: absolute;
  width: 20px;
  height: 20px;
  border-radius: var(--radius-full);
  background: white;
  top: 2px;
  left: 2px;
  box-shadow: var(--shadow-sm);
  transition: transform var(--duration-normal) var(--ease-spring);
}

.toggle:checked {
  background: var(--color-accent);
}

.toggle:checked::after {
  transform: translateX(20px);
}

.toggle:focus-visible {
  box-shadow: var(--shadow-focus);
}
```

### 6.7 Search Input

```css
.search {
  position: relative;
}

.search__icon {
  position: absolute;
  left: var(--space-3);
  top: 50%;
  transform: translateY(-50%);
  color: var(--color-text-tertiary);
  pointer-events: none;
  width: 18px;
  height: 18px;
}

.search__input {
  composes: input;
  padding-left: var(--space-10);
}

.search__clear {
  position: absolute;
  right: var(--space-2);
  top: 50%;
  transform: translateY(-50%);
  background: none;
  border: none;
  color: var(--color-text-tertiary);
  cursor: pointer;
  padding: var(--space-1);
  border-radius: var(--radius-sm);
}

.search__clear:hover {
  color: var(--color-text-primary);
  background: var(--color-highlight);
}
```

---

## 7. Layout Patterns

### 7.1 Page Container

```css
.page {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 var(--padding-page);
}

.page--narrow {
  max-width: 720px; /* Long-form reading */
}

.page--wide {
  max-width: 1400px; /* Dashboards */
}

.page--full {
  max-width: none; /* Full bleed */
}
```

### 7.2 App Shell (Sidebar + Main)

```css
.app-shell {
  display: flex;
  min-height: 100dvh;
}

.app-shell__sidebar {
  /* Uses .sidebar component */
  flex-shrink: 0;
}

.app-shell__main {
  flex: 1;
  min-width: 0; /* Prevent flex overflow */
  overflow-y: auto;
}

.app-shell__content {
  max-width: 960px;
  margin: 0 auto;
  padding: var(--space-8) var(--padding-page);
}

/* Collapsed sidebar for mobile */
@media (max-width: 768px) {
  .app-shell {
    flex-direction: column;
  }
  .app-shell__sidebar {
    width: 100%;
    min-width: auto;
    height: auto;
    position: relative;
    border-right: none;
    border-bottom: 1px solid var(--color-border);
  }
}
```

### 7.3 Grid System

```css
.grid {
  display: grid;
  gap: var(--space-6);
}

.grid--2  { grid-template-columns: repeat(2, 1fr); }
.grid--3  { grid-template-columns: repeat(3, 1fr); }
.grid--4  { grid-template-columns: repeat(4, 1fr); }
.grid--auto-fill {
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
}

@media (max-width: 768px) {
  .grid--2,
  .grid--3,
  .grid--4 {
    grid-template-columns: 1fr;
  }
}

@media (min-width: 769px) and (max-width: 1024px) {
  .grid--3,
  .grid--4 {
    grid-template-columns: repeat(2, 1fr);
  }
}
```

### 7.4 Stack & Cluster

```css
/* Stack — vertical spacing */
.stack {
  display: flex;
  flex-direction: column;
  gap: var(--gap-stack);
}

.stack--sm   { gap: var(--space-2); }
.stack--lg   { gap: var(--space-8); }
.stack--xl   { gap: var(--space-12); }

/* Cluster — horizontal wrapping */
.cluster {
  display: flex;
  flex-wrap: wrap;
  gap: var(--space-3);
  align-items: center;
}

.cluster--between {
  justify-content: space-between;
}

.cluster--end {
  justify-content: flex-end;
}
```

### 7.5 Section Pattern

```css
.section {
  padding: var(--padding-section) 0;
}

.section + .section {
  border-top: 1px solid var(--color-border);
}

.section__header {
  margin-bottom: var(--space-8);
}

.section__title {
  font-family: var(--font-serif);
  font-size: var(--text-3xl);
  font-weight: var(--weight-semibold);
  color: var(--color-text-primary);
}

.section__subtitle {
  font-family: var(--font-serif);
  font-size: var(--text-md);
  color: var(--color-text-secondary);
  margin-top: var(--space-2);
  max-width: 60ch;
}
```

---

## 8. Interaction Patterns

### 8.1 Hover States

All interactive elements must have visible hover feedback:
- **Cards:** Elevated shadow + subtle translateY(-2px)
- **Buttons:** Color shift + shadow increase + translateY(-1px)
- **Links:** Underline color intensifies or animates
- **List items:** Background highlight (`--color-highlight`)
- **Icons:** Opacity change (0.6 → 1.0) or color shift

### 8.2 Focus States

Every focusable element must show the Claude focus ring:

```css
:focus-visible {
  outline: 2px solid var(--color-border-focus);
  outline-offset: 2px;
  border-radius: var(--radius-sm);
}
```

The orange focus ring is a signature Claude pattern — it matches the accent color and provides strong visibility.

### 8.3 Active / Pressed States

```css
/* Button press — settles down */
.button:active {
  transform: translateY(0);
  box-shadow: var(--shadow-xs);
}

/* Card press */
.card:active {
  transform: translateY(0);
  box-shadow: var(--shadow-sm);
}
```

### 8.4 Loading States

```css
/* Skeleton loading — warm shimmer */
.skeleton {
  background: linear-gradient(
    90deg,
    var(--color-border) 25%,
    var(--color-surface) 50%,
    var(--color-border) 75%
  );
  background-size: 200% 100%;
  animation: skeleton-shimmer 1.5s ease-in-out infinite;
  border-radius: var(--radius-sm);
}

@keyframes skeleton-shimmer {
  0% { background-position: 200% 0; }
  100% { background-position: -200% 0; }
}

.skeleton--text {
  height: 1em;
  width: 80%;
  margin-bottom: var(--space-2);
}

.skeleton--title {
  height: 1.5em;
  width: 60%;
  margin-bottom: var(--space-3);
}

.skeleton--avatar {
  width: 40px;
  height: 40px;
  border-radius: var(--radius-full);
}

/* Spinner — for button loading */
.spinner {
  width: 18px;
  height: 18px;
  border: 2px solid transparent;
  border-top-color: currentColor;
  border-radius: var(--radius-full);
  animation: spin 600ms linear infinite;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}
```

### 8.5 Empty States

```css
.empty-state {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  padding: var(--space-16) var(--space-8);
  color: var(--color-text-tertiary);
}

.empty-state__icon {
  font-size: 48px;
  margin-bottom: var(--space-4);
  opacity: 0.4;
}

.empty-state__title {
  font-family: var(--font-serif);
  font-size: var(--text-xl);
  font-weight: var(--weight-semibold);
  color: var(--color-text-secondary);
  margin-bottom: var(--space-2);
}

.empty-state__description {
  font-family: var(--font-serif);
  font-size: var(--text-base);
  color: var(--color-text-tertiary);
  max-width: 40ch;
  margin-bottom: var(--space-6);
}
```

---

## 9. Icon System

### 9.1 Icon Guidelines

The Claude Design System uses **Lucide** icons as the default icon set. Lucide icons are clean, consistent, and have the right weight for the Claude aesthetic — not too heavy, not too thin.

**Icon sizing:**
```css
:root {
  --icon-sm:    16px;
  --icon-md:    20px;
  --icon-lg:    24px;
  --icon-xl:    32px;
}
```

**Rules:**
1. Icons use `currentColor` so they inherit text color.
2. Stroke width: 1.5px (Lucide default) for body icons, 2px for nav/action icons.
3. Always pair icons with text labels in navigation. Icon-only is acceptable only for well-known actions (close, search, settings).
4. Add `aria-hidden="true"` to decorative icons, `aria-label` to functional icons.

### 9.2 Icon Wrapper

```css
.icon {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
  color: currentColor;
}

.icon--sm { width: var(--icon-sm); height: var(--icon-sm); }
.icon--md { width: var(--icon-md); height: var(--icon-md); }
.icon--lg { width: var(--icon-lg); height: var(--icon-lg); }
.icon--xl { width: var(--icon-xl); height: var(--icon-xl); }

.icon--muted { color: var(--color-text-tertiary); }
.icon--accent { color: var(--color-accent); }
```

---

## 10. Responsive Behavior & Mobile Webapp Standards

This section covers everything needed to transform a Claude-styled desktop interface into a mobile-native-feeling webapp. It goes well beyond breakpoints — it defines how navigation, composition, interaction, and the entire UX should adapt for touch-first, small-screen environments.

### 10.1 Breakpoints

```css
:root {
  /* Mobile-first breakpoints — use min-width in media queries */
  /* xs:   0       — Small phones (default, no query needed) */
  /* sm:   640px   — Large phones, small tablets in portrait */
  /* md:   768px   — Tablets in portrait */
  /* lg:   1024px  — Tablets in landscape, small desktops */
  /* xl:   1280px  — Standard desktops */
  /* 2xl:  1536px  — Large screens */
}

/* Usage: always mobile-first, NEVER desktop-down */
/* ✅ Correct: */
@media (min-width: 768px) { /* tablet+ styles */ }

/* ❌ Wrong: */
@media (max-width: 767px) { /* mobile overrides */ }
```

**Design at three widths, test at five:**
- Design: Mobile (375px), Tablet (768px), Desktop (1280px)
- Test: 320px, 375px, 768px, 1024px, 1440px

### 10.2 Responsive Typography

```css
/* Fluid headings — clamp between mobile and desktop sizes */
h1 {
  font-size: clamp(var(--text-3xl), 5vw + 1rem, var(--text-5xl));
}

h2 {
  font-size: clamp(var(--text-2xl), 3vw + 1rem, var(--text-3xl));
}

h3 {
  font-size: clamp(var(--text-xl), 2vw + 0.5rem, var(--text-2xl));
}

/* Body stays FIXED — never scale body text with viewport */
p { font-size: var(--text-base); } /* Always 16px. Period. */

/* CRITICAL: Never go below 16px for body text on mobile.
   iOS will zoom into <16px inputs, breaking your layout. */
```

### 10.3 Mobile Viewport & Safe Areas

```css
/* Viewport setup */
html {
  /* Use dvh for full-height layouts — accounts for mobile browser chrome */
  min-height: 100dvh;
}

/* Safe areas for notched/Dynamic Island devices */
body {
  padding-left: env(safe-area-inset-left);
  padding-right: env(safe-area-inset-right);
}

/* Bottom elements MUST respect home indicator */
.bottom-bar,
.bottom-nav,
.chat-input,
.sheet__footer,
.fab {
  padding-bottom: max(var(--space-4), env(safe-area-inset-bottom));
}

/* Top elements respect Dynamic Island / status bar */
.mobile-header {
  padding-top: max(var(--space-3), env(safe-area-inset-top));
}
```

```html
<!-- Required viewport meta — NEVER include user-scalable=no -->
<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover" />

<!-- viewport-fit=cover enables safe area insets for edge-to-edge layout -->
<!-- NEVER use user-scalable=no — it's an accessibility violation -->
```

### 10.4 Touch & Interaction

#### 10.4.1 Touch Targets

```css
/* WCAG 2.5.8: minimum 44×44px for ALL interactive elements */
.touch-target {
  min-width: 44px;
  min-height: 44px;
}

/* Invisible hit area expansion (when visual size must be smaller) */
.touch-expand {
  position: relative;
}
.touch-expand::after {
  content: '';
  position: absolute;
  inset: -8px; /* Expand hit area by 8px in all directions */
}

/* Minimum gap between adjacent touch targets: 8px */
.touch-row {
  display: flex;
  gap: max(var(--space-2), 8px);
}
```

#### 10.4.2 Tap States

On touch devices, `:hover` doesn't exist the same way. Use `:active` for immediate feedback:

```css
/* Remove hover delay on touch — use active instead */
@media (hover: none) and (pointer: coarse) {
  .card:hover {
    /* Disable desktop hover effect on touch */
    box-shadow: var(--shadow-card);
    transform: none;
  }

  .card:active {
    /* Instant tap feedback */
    background: var(--color-highlight);
    transform: scale(0.98);
    transition-duration: var(--duration-fast);
  }

  .button:active {
    transform: scale(0.96);
    transition-duration: var(--duration-fast);
  }

  .sidebar__item:active,
  .navbar__link:active {
    background: var(--color-highlight);
  }
}

/* Disable tap highlight on iOS/Android */
* {
  -webkit-tap-highlight-color: transparent;
}
```

#### 10.4.3 Gesture Patterns

```css
/* Swipeable container — horizontal scroll with snap */
.swipe-row {
  display: flex;
  gap: var(--space-4);
  overflow-x: auto;
  scroll-snap-type: x mandatory;
  -webkit-overflow-scrolling: touch;
  scrollbar-width: none; /* Hide scrollbar on Firefox */
  padding: var(--space-2) var(--padding-page);
}

.swipe-row::-webkit-scrollbar {
  display: none; /* Hide scrollbar on Webkit */
}

.swipe-row > * {
  scroll-snap-align: start;
  flex-shrink: 0;
}

/* Pull-to-refresh visual indicator */
.pull-indicator {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 0;
  overflow: hidden;
  transition: height var(--duration-normal) var(--ease-default);
  color: var(--color-text-tertiary);
}

.pull-indicator.is-pulling {
  height: 60px;
}

.pull-indicator .spinner {
  width: 24px;
  height: 24px;
}
```

**Gesture rules for the Claude system:**
1. **Swipe left/right** — Use only for carousel/tab switching. Never for delete (use explicit button).
2. **Pull down** — Pull-to-refresh is acceptable in list/feed views.
3. **Long press** — Use for contextual menus. Always provide a visible menu button as alternative.
4. **Pinch** — Only for images/maps. Never for UI scaling.
5. **Edge swipe** — Reserved by the OS. Never override.

### 10.5 Navigation Transformations

On mobile, desktop navigation patterns must fundamentally change.

#### 10.5.1 Sidebar → Drawer

The desktop sidebar becomes an off-canvas drawer on mobile:

```css
/* Desktop: visible sidebar */
@media (min-width: 769px) {
  .sidebar {
    width: 280px;
    min-width: 280px;
    position: sticky;
    top: 0;
    height: 100dvh;
  }
}

/* Mobile: off-canvas drawer */
@media (max-width: 768px) {
  .sidebar {
    position: fixed;
    top: 0;
    left: 0;
    width: 85vw;
    max-width: 320px;
    height: 100dvh;
    z-index: var(--z-overlay);
    transform: translateX(-100%);
    transition: transform var(--duration-slow) var(--ease-editorial);
    box-shadow: none;
  }

  .sidebar.is-open {
    transform: translateX(0);
    box-shadow: var(--shadow-2xl);
  }

  /* Scrim behind drawer */
  .sidebar-scrim {
    position: fixed;
    inset: 0;
    background: var(--color-scrim);
    z-index: calc(var(--z-overlay) - 1);
    opacity: 0;
    pointer-events: none;
    transition: opacity var(--duration-slow) var(--ease-default);
  }

  .sidebar-scrim.is-visible {
    opacity: 1;
    pointer-events: auto;
  }
}
```

```html
<!-- Mobile header with hamburger trigger -->
<header class="mobile-header">
  <button class="button button--ghost button--icon" aria-label="Open menu" data-drawer-trigger>
    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
      <line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="18" x2="21" y2="18"/>
    </svg>
  </button>
  <span class="mobile-header__title">Claude</span>
  <button class="button button--ghost button--icon" aria-label="New conversation">
    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
      <line x1="12" y1="5" x2="12" y2="19"/><line x1="5" y1="12" x2="19" y2="12"/>
    </svg>
  </button>
</header>
```

```css
.mobile-header {
  display: none; /* Hidden on desktop */
}

@media (max-width: 768px) {
  .mobile-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: var(--space-2) var(--space-3);
    padding-top: max(var(--space-2), env(safe-area-inset-top));
    background: var(--color-chrome);
    border-bottom: 1px solid var(--color-border);
    position: sticky;
    top: 0;
    z-index: var(--z-header);
    min-height: 48px;
  }

  .mobile-header__title {
    font-family: var(--font-sans);
    font-size: var(--text-lg);
    font-weight: var(--weight-semibold);
    color: var(--color-text-primary);
  }
}
```

#### 10.5.2 Bottom Tab Bar

For apps with 3–5 top-level sections, replace the sidebar with a bottom tab bar:

```css
.bottom-nav {
  display: none; /* Hidden on desktop */
}

@media (max-width: 768px) {
  .bottom-nav {
    display: flex;
    align-items: center;
    justify-content: space-around;
    position: fixed;
    bottom: 0;
    left: 0;
    right: 0;
    z-index: var(--z-header);
    background: var(--color-chrome);
    border-top: 1px solid var(--color-border);
    padding: var(--space-2) 0;
    padding-bottom: max(var(--space-2), env(safe-area-inset-bottom));
  }

  .bottom-nav__item {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 2px;
    padding: var(--space-1) var(--space-3);
    border-radius: var(--radius-md);
    color: var(--color-text-tertiary);
    text-decoration: none;
    font-family: var(--font-sans);
    font-size: 10px;
    font-weight: var(--weight-medium);
    letter-spacing: var(--tracking-wide);
    min-width: 44px;
    min-height: 44px;
    justify-content: center;
    transition: color var(--duration-fast) var(--ease-default);
  }

  .bottom-nav__item:active {
    background: var(--color-highlight);
  }

  .bottom-nav__item--active {
    color: var(--color-accent-text);
  }

  .bottom-nav__item--active .bottom-nav__icon {
    color: var(--color-accent);
  }

  .bottom-nav__icon {
    width: 22px;
    height: 22px;
  }

  /* Reserve space for bottom nav so content doesn't hide behind it */
  .app-shell__main {
    padding-bottom: calc(64px + env(safe-area-inset-bottom));
  }
}
```

```html
<nav class="bottom-nav" aria-label="Main navigation">
  <a href="/" class="bottom-nav__item bottom-nav__item--active">
    <svg class="bottom-nav__icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
      <path d="M3 9l9-7 9 7v11a2 2 0 01-2 2H5a2 2 0 01-2-2z"/>
    </svg>
    Home
  </a>
  <a href="/search" class="bottom-nav__item">
    <svg class="bottom-nav__icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
      <circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/>
    </svg>
    Search
  </a>
  <a href="/history" class="bottom-nav__item">
    <svg class="bottom-nav__icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
      <circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/>
    </svg>
    History
  </a>
  <a href="/settings" class="bottom-nav__item">
    <svg class="bottom-nav__icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
      <circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.65 1.65 0 00.33 1.82l.06.06a2 2 0 010 2.83 2 2 0 01-2.83 0l-.06-.06a1.65 1.65 0 00-1.82-.33 1.65 1.65 0 00-1 1.51V21a2 2 0 01-4 0v-.09A1.65 1.65 0 009 19.4a1.65 1.65 0 00-1.82.33l-.06.06a2 2 0 01-2.83-2.83l.06-.06A1.65 1.65 0 004.68 15a1.65 1.65 0 00-1.51-1H3a2 2 0 010-4h.09A1.65 1.65 0 004.6 9a1.65 1.65 0 00-.33-1.82l-.06-.06a2 2 0 012.83-2.83l.06.06A1.65 1.65 0 009 4.68a1.65 1.65 0 001-1.51V3a2 2 0 014 0v.09a1.65 1.65 0 001 1.51 1.65 1.65 0 001.82-.33l.06-.06a2 2 0 012.83 2.83l-.06.06A1.65 1.65 0 0019.4 9a1.65 1.65 0 001.51 1H21a2 2 0 010 4h-.09a1.65 1.65 0 00-1.51 1z"/>
    </svg>
    Settings
  </a>
</nav>
```

#### 10.5.3 Top Navigation → Scrollable Tabs

Desktop horizontal nav with many items becomes scrollable tabs:

```css
@media (max-width: 768px) {
  .navbar__nav {
    overflow-x: auto;
    scroll-snap-type: x mandatory;
    -webkit-overflow-scrolling: touch;
    scrollbar-width: none;
    padding: 0 var(--space-4);
    gap: 0;
  }

  .navbar__nav::-webkit-scrollbar { display: none; }

  .navbar__link {
    scroll-snap-align: start;
    white-space: nowrap;
    flex-shrink: 0;
  }
}
```

### 10.6 Bottom Sheet

The bottom sheet is the mobile replacement for desktop modals, dropdowns, and contextual panels. It slides up from the bottom and can be dragged to dismiss.

```css
/* Bottom sheet — replaces modal on mobile */
.sheet-scrim {
  position: fixed;
  inset: 0;
  background: var(--color-scrim);
  z-index: var(--z-modal);
  opacity: 0;
  pointer-events: none;
  transition: opacity var(--duration-normal) var(--ease-default);
}

.sheet-scrim.is-visible {
  opacity: 1;
  pointer-events: auto;
}

.sheet {
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  z-index: var(--z-modal);
  background: var(--color-overlay);
  border-radius: var(--radius-xl) var(--radius-xl) 0 0;
  box-shadow: var(--shadow-2xl);
  max-height: 90dvh;
  overflow-y: auto;
  transform: translateY(100%);
  transition: transform var(--duration-slow) var(--ease-editorial);
}

.sheet.is-open {
  transform: translateY(0);
}

/* Drag handle */
.sheet__handle {
  display: flex;
  justify-content: center;
  padding: var(--space-3) 0 var(--space-1);
  cursor: grab;
}

.sheet__handle::after {
  content: '';
  width: 36px;
  height: 4px;
  border-radius: var(--radius-full);
  background: var(--color-border-strong);
}

.sheet__header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: var(--space-2) var(--space-5) var(--space-4);
}

.sheet__title {
  font-family: var(--font-sans);
  font-size: var(--text-lg);
  font-weight: var(--weight-semibold);
  color: var(--color-text-primary);
}

.sheet__body {
  padding: 0 var(--space-5) var(--space-5);
}

.sheet__footer {
  display: flex;
  gap: var(--space-3);
  padding: var(--space-4) var(--space-5);
  padding-bottom: max(var(--space-4), env(safe-area-inset-bottom));
  border-top: 1px solid var(--color-border);
}

.sheet__footer .button {
  flex: 1;
}
```

```html
<!-- Bottom sheet example -->
<div class="sheet-scrim is-visible" data-sheet-dismiss></div>
<div class="sheet is-open" role="dialog" aria-modal="true" aria-labelledby="sheet-title">
  <div class="sheet__handle" aria-hidden="true"></div>
  <div class="sheet__header">
    <h2 class="sheet__title" id="sheet-title">Share conversation</h2>
    <button class="button button--ghost button--icon" aria-label="Close">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
        <line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/>
      </svg>
    </button>
  </div>
  <div class="sheet__body">
    <p>Choose how you'd like to share this conversation.</p>
    <!-- Sheet content -->
  </div>
  <div class="sheet__footer">
    <button class="button button--secondary">Cancel</button>
    <button class="button button--primary">Share</button>
  </div>
</div>
```

**When to use bottom sheet vs. modal:**

| Context | Desktop | Mobile |
|---------|---------|--------|
| Confirmation dialogs | Modal (centered) | Bottom sheet |
| Form editing | Modal or inline | Bottom sheet (full-height) |
| Menus / option lists | Dropdown popover | Bottom sheet |
| Filters / sort | Side panel | Bottom sheet |
| Detail preview | Side panel or modal | Bottom sheet (peek, 50%) |

### 10.7 Component Transformations

How every major Claude component adapts for mobile:

#### 10.7.1 Cards

```css
@media (max-width: 640px) {
  .card {
    border-radius: 0;         /* Full-bleed on narrow phones */
    margin-left: calc(var(--padding-page) * -1);
    margin-right: calc(var(--padding-page) * -1);
    border-left: none;
    border-right: none;
  }

  /* Alternatively: keep rounded but reduce padding */
  .card--mobile-padded {
    border-radius: var(--radius-md);
    margin: 0;
    padding: var(--space-4);  /* Reduced from space-6 */
  }
}
```

#### 10.7.2 Grid → Stack

```css
@media (max-width: 768px) {
  .grid--2,
  .grid--3,
  .grid--4 {
    grid-template-columns: 1fr;
    gap: var(--space-4); /* Tighter gap on mobile */
  }

  /* Metric cards: 2-up on mobile instead of 4-up */
  .grid--metrics {
    grid-template-columns: repeat(2, 1fr);
    gap: var(--space-3);
  }
}

@media (max-width: 380px) {
  .grid--metrics {
    grid-template-columns: 1fr;
  }
}
```

#### 10.7.3 Table → Card List

Tables are unusable on narrow screens. Transform into stacked cards:

```css
@media (max-width: 768px) {
  .table--responsive thead {
    display: none; /* Hide column headers */
  }

  .table--responsive tbody tr {
    display: flex;
    flex-direction: column;
    padding: var(--space-4);
    border-bottom: 1px solid var(--color-border);
    gap: var(--space-2);
  }

  .table--responsive td {
    display: flex;
    justify-content: space-between;
    padding: 0;
    border: none;
  }

  /* Show column name as a label */
  .table--responsive td::before {
    content: attr(data-label);
    font-family: var(--font-sans);
    font-size: var(--text-xs);
    font-weight: var(--weight-semibold);
    color: var(--color-text-tertiary);
    text-transform: uppercase;
    letter-spacing: var(--tracking-wider);
    flex-shrink: 0;
    margin-right: var(--space-4);
  }
}
```

```html
<!-- Mark cells with data-label for mobile transformation -->
<tr>
  <td data-label="User">Jane Smith</td>
  <td data-label="Duration">4m 23s</td>
  <td data-label="Status"><span class="badge badge--success">Complete</span></td>
</tr>
```

#### 10.7.4 Modal → Bottom Sheet

```css
@media (max-width: 768px) {
  .modal-scrim {
    align-items: flex-end; /* Anchor to bottom */
    padding: 0;
  }

  .modal {
    max-width: 100%;
    max-height: 90dvh;
    border-radius: var(--radius-xl) var(--radius-xl) 0 0;
    animation: slideInUp var(--duration-slow) var(--ease-editorial) both;
  }

  .modal__footer {
    padding-bottom: max(var(--space-4), env(safe-area-inset-bottom));
  }

  .modal__footer .button {
    flex: 1; /* Full-width buttons on mobile */
  }
}
```

#### 10.7.5 Tooltips → Inline Hints

Tooltips don't work on touch. Replace with visible inline hints:

```css
@media (hover: none) and (pointer: coarse) {
  .tooltip__content {
    display: none !important; /* Disable hover tooltips */
  }

  /* Show as inline hint instead */
  .tooltip-mobile-hint {
    display: block;
    font-family: var(--font-sans);
    font-size: var(--text-xs);
    color: var(--color-text-tertiary);
    margin-top: var(--space-1);
  }
}

@media (hover: hover) {
  .tooltip-mobile-hint {
    display: none; /* Hide inline hint on desktop */
  }
}
```

### 10.8 Mobile Form Optimization

#### 10.8.1 Input Types

Always use the correct HTML input type to trigger the right mobile keyboard:

```html
<!-- Numeric keyboard -->
<input type="tel" inputmode="numeric" pattern="[0-9]*" />

<!-- Email keyboard (with @ key) -->
<input type="email" inputmode="email" autocomplete="email" />

<!-- URL keyboard (with .com key) -->
<input type="url" inputmode="url" />

<!-- Search (with return → "Search") -->
<input type="search" enterkeyhint="search" />

<!-- Decimal keyboard -->
<input type="text" inputmode="decimal" />

<!-- Next/Done on return key -->
<input enterkeyhint="next" />  <!-- Multi-field forms -->
<input enterkeyhint="done" />  <!-- Last field in form -->
<input enterkeyhint="send" />  <!-- Chat input -->
```

#### 10.8.2 Mobile Form Layout

```css
@media (max-width: 768px) {
  /* Stack all form fields vertically */
  .form-row {
    flex-direction: column;
  }

  /* Full-width inputs */
  .input,
  .select,
  .textarea {
    width: 100%;
    font-size: 16px; /* CRITICAL: prevents iOS zoom on focus */
  }

  /* Larger touch targets for checkboxes/radios */
  .checkbox,
  .radio {
    width: 22px;
    height: 22px;
  }

  .toggle {
    width: 52px;
    height: 28px;
  }

  .toggle::after {
    width: 24px;
    height: 24px;
  }

  /* Full-width buttons at bottom of forms */
  .form__actions {
    flex-direction: column;
  }

  .form__actions .button {
    width: 100%;
  }

  /* Primary action first on mobile (finger-accessible) */
  .form__actions .button--primary {
    order: -1;
  }
}
```

#### 10.8.3 Scroll Behavior on Focus

```css
/* When a mobile input receives focus, scroll it into view with padding */
@media (max-width: 768px) {
  .input:focus,
  .textarea:focus,
  .select:focus {
    scroll-margin-top: 100px; /* Space above input when scrolled into view */
    scroll-margin-bottom: 100px;
  }
}
```

### 10.9 Thumb Zone Design

On mobile, the bottom 40% of the screen is the "easy reach" zone for single-handed use. The top 20% is the "stretch" zone. Design accordingly.

```
┌─────────────────────┐
│   STRETCH ZONE      │  ← Titles, status info (read-only)
│   (hard to reach)   │
├─────────────────────┤
│                     │
│   NATURAL ZONE      │  ← Scrollable content
│   (comfortable)     │
│                     │
├─────────────────────┤
│  ★ EASY REACH ★     │  ← Primary actions, nav, input
│   (thumb-friendly)  │
└─────────────────────┘
```

**Rules for thumb-zone design:**
1. **Primary actions at the bottom** — CTAs, send buttons, navigation
2. **Content in the middle** — scrollable, readable
3. **Status & titles at the top** — read-only, infrequently tapped
4. **Never put destructive actions in the easy-reach zone** — "Delete" goes in menus or confirmations, not in the thumb zone
5. **FABs (Floating Action Buttons) go bottom-right** — dominant thumb position

```css
/* Floating Action Button */
.fab {
  position: fixed;
  bottom: calc(var(--space-6) + env(safe-area-inset-bottom));
  right: var(--space-6);
  z-index: var(--z-raised);
  width: 56px;
  height: 56px;
  border-radius: var(--radius-full);
  background: var(--color-accent);
  color: white;
  border: none;
  cursor: pointer;
  box-shadow: var(--shadow-lg);
  display: flex;
  align-items: center;
  justify-content: center;
  transition: transform var(--duration-fast) var(--ease-default),
              box-shadow var(--duration-fast) var(--ease-default);
}

.fab:active {
  transform: scale(0.92);
  box-shadow: var(--shadow-md);
}

/* If bottom-nav exists, lift FAB above it */
.has-bottom-nav .fab {
  bottom: calc(72px + env(safe-area-inset-bottom) + var(--space-4));
}
```

### 10.10 Container Queries

Container queries allow components to adapt based on their parent's size rather than the viewport. This is essential for components used in both sidebars and main content areas:

```css
/* Define containers */
.card-container {
  container-type: inline-size;
  container-name: card;
}

.content-area {
  container-type: inline-size;
  container-name: content;
}

/* Card adapts to its container, not the viewport */
@container card (max-width: 300px) {
  .card {
    padding: var(--space-3);
  }
  .card__title {
    font-size: var(--text-base);
  }
  .card__footer {
    flex-direction: column;
  }
}

@container card (min-width: 500px) {
  .card {
    display: grid;
    grid-template-columns: auto 1fr;
    gap: var(--space-6);
  }
}

/* Content area — adapt layout to available space */
@container content (max-width: 600px) {
  .section__header {
    text-align: left;
  }
  .grid--auto-fill {
    grid-template-columns: 1fr;
  }
}
```

### 10.11 PWA (Progressive Web App) Setup

To make the Claude-styled webapp installable and app-like on mobile:

```json
/* manifest.json */
{
  "name": "Your App Name",
  "short_name": "App",
  "start_url": "/",
  "display": "standalone",
  "background_color": "#f3f1ea",
  "theme_color": "#d97757",
  "orientation": "portrait-primary",
  "icons": [
    { "src": "/icons/icon-192.png", "sizes": "192x192", "type": "image/png" },
    { "src": "/icons/icon-512.png", "sizes": "512x512", "type": "image/png" },
    { "src": "/icons/icon-maskable-512.png", "sizes": "512x512", "type": "image/png", "purpose": "maskable" }
  ]
}
```

```html
<!-- PWA meta tags -->
<link rel="manifest" href="/manifest.json" />
<meta name="theme-color" content="#d97757" />

<!-- iOS-specific (Safari doesn't fully support manifest) -->
<meta name="apple-mobile-web-app-capable" content="yes" />
<meta name="apple-mobile-web-app-status-bar-style" content="default" />
<meta name="apple-mobile-web-app-title" content="Your App" />
<link rel="apple-touch-icon" href="/icons/icon-180.png" />

<!-- Splash screens for iOS -->
<link rel="apple-touch-startup-image" href="/splash/iphone.png" media="(device-width: 375px)" />
```

**PWA warm styling notes:**
- `background_color` must be `#f3f1ea` (sand canvas) — this shows while the app loads
- `theme_color` should be `#d97757` (accent) — this tints the OS status bar / title bar
- Status bar style: use `default` (dark text on light bar), not `black-translucent`

### 10.12 Mobile Spacing Adjustments

```css
@media (max-width: 768px) {
  :root {
    /* Tighten page-level spacing on mobile */
    --padding-page:    var(--space-4);   /* 32px → 16px */
    --padding-card:    var(--space-4);   /* 24px → 16px */
    --padding-section: var(--space-8);   /* 48px → 32px */
    --gap-section:     var(--space-10);  /* 64px → 40px */
  }
}

@media (max-width: 380px) {
  :root {
    /* Even tighter for very small phones */
    --padding-page:    var(--space-3);   /* 12px */
  }
}
```

### 10.13 Mobile Performance

1. **Reduce animations on mobile** — cut stagger cap from 8 to 4 items.
2. **Use `content-visibility: auto`** — on off-screen card lists and long scrollable sections.
3. **Lazy load below-fold content** — images, heavy components.
4. **Avoid fixed backgrounds** — they cause janky scroll on iOS.
5. **Minimize box-shadow complexity** — on mobile, use --shadow-sm/md max. Save --shadow-lg+ for desktop.

```css
/* Content visibility for long lists */
.card-list > .card {
  content-visibility: auto;
  contain-intrinsic-size: auto 200px;
}

/* Simpler shadows on mobile */
@media (max-width: 768px) {
  :root {
    --shadow-card: var(--shadow-sm);
    --shadow-dropdown: var(--shadow-md);
  }
}
```

### 10.14 Mobile Checklist

Before shipping any mobile view:

```
□ VIEWPORT
  □ Viewport meta tag present with viewport-fit=cover
  □ No user-scalable=no (accessibility violation)
  □ Safe area insets applied (top, bottom, left, right)
  □ Dynamic Island / notch area respected
  □ 100dvh used instead of 100vh for full-height layouts

□ TOUCH
  □ All interactive elements ≥ 44×44px touch targets
  □ Minimum 8px gap between adjacent touch targets
  □ No hover-dependent functionality (provide tap/active alternatives)
  □ Tap highlight disabled (webkit-tap-highlight-color: transparent)
  □ Active states provide immediate visual feedback
  □ No edge-swipe conflicts with OS gestures

□ NAVIGATION
  □ Sidebar converts to drawer (≤768px)
  □ Drawer has scrim backdrop
  □ Drawer closes on scrim tap and back button
  □ Bottom nav present for 3-5 section apps
  □ Bottom nav reserves safe area space
  □ Current section highlighted in bottom nav

□ LAYOUT
  □ Cards go full-bleed or reduce padding on narrow screens
  □ Grid collapses to single column (or 2-col for metrics)
  □ Tables transform to stacked card layout
  □ Modals become bottom sheets on mobile
  □ Tooltips become inline hints on touch devices
  □ Page padding reduces (space-8 → space-4)

□ FORMS
  □ Correct input types (email, tel, url, search)
  □ Correct inputmode attributes
  □ enterkeyhint set (next, done, send, search)
  □ Input font-size ≥ 16px (prevents iOS zoom)
  □ Buttons full-width in mobile forms
  □ Primary action button listed first (bottom/visible)

□ CONTENT
  □ Text readable without zooming (≥16px body)
  □ Headings scale down fluidly (clamp)
  □ Long content scrollable, not truncated
  □ Images responsive (max-width: 100%, height: auto)

□ PERFORMANCE
  □ Animations reduced/simplified on mobile
  □ Content-visibility applied to long lists
  □ Below-fold images lazy loaded
  □ No fixed background-attachment (causes jank on iOS)
  □ Shadow complexity reduced
  □ Touch event handling doesn't block scroll

□ PWA (if applicable)
  □ manifest.json present with correct theme/background colors
  □ Apple meta tags for iOS webapp support
  □ 192px + 512px + maskable icons
  □ Service worker registered for offline support
  □ Splash screen configured
```

---

## 11. Performance Guidelines

### 11.1 Font Loading

```html
<!-- Preconnect to Google Fonts -->
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />

<!-- Load fonts with display=swap to prevent FOIT -->
<link
  href="https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,400;0,500;0,600;0,700;1,400;1,500&family=Poppins:wght@300;400;500;600;700&family=Fira+Code:wght@400;500&display=swap"
  rel="stylesheet"
/>
```

### 11.2 CSS Performance

1. **Avoid `@import` for critical CSS** — inline the design tokens in `<style>` tags for first paint.
2. **Use `contain: layout` on cards and grid items** to isolate layout recalculations.
3. **Shadow transitions** — only transition `box-shadow` and `transform`, never animate `border` or `background` properties that trigger layout.
4. **Use `will-change: transform` sparingly** — only on elements currently being animated.

### 11.3 Animation Budget

Target: 60fps minimum. Budget per frame: 16.67ms.

- Max concurrent animations: 8 elements
- Stagger cap: 8 items (beyond 8, all appear together)
- Shadow transitions: keep to md/lg scale, avoid transitioning between none and 2xl
- Always use `transform` and `opacity` only for animations — they don't trigger reflow

---

## 12. Accessibility Checklist

Before shipping any page:

```
□ All text meets WCAG AA contrast (4.5:1 normal, 3:1 large)
□ All interactive elements have visible focus states (orange ring)
□ All form fields have associated <label> elements
□ All images have alt text (or aria-hidden if decorative)
□ All icons have aria-hidden="true" or aria-label
□ Page has correct heading hierarchy (h1 > h2 > h3, no skips)
□ Modals trap focus and return focus on close
□ Tab order follows visual order
□ Reduced-motion preference is respected (all animations disabled)
□ High-contrast mode provides readable alternatives
□ Touch targets are minimum 44x44px with ≥8px spacing
□ Color is never the sole indicator of state (always shape/icon/text too)
□ Screen reader testing passed (VoiceOver/NVDA/TalkBack)
□ No user-scalable=no on viewport meta
□ Mobile: no hover-only interactions (tap alternatives provided)
□ Mobile: drawer/sheet focus-trapped and dismissible via scrim + back
□ Mobile: bottom nav labels present (not icon-only)
```

---

## 13. Do's and Don'ts Quick Reference

**DO:**
- Use warm backgrounds (sand, cream, off-white)
- Use serif for body text, sans-serif for UI
- Use multi-layer shadows for elevation
- Use the rust-orange accent as the primary interactive color
- Use generous whitespace — err on the side of too much
- Use staggered entrance animations for content groups
- Use editorial composition — left-aligned body, asymmetric layouts
- Test in both light and dark mode
- Convert sidebar to drawer on mobile (≤768px)
- Use bottom sheets instead of modals on mobile
- Put primary actions in the thumb-friendly bottom zone
- Ensure all touch targets are ≥44×44px with ≥8px gaps
- Use correct input types (email, tel, url) for mobile keyboards
- Apply safe-area insets for notched/Dynamic Island devices
- Transform tables into stacked card lists on narrow screens
- Reduce spacing, shadows, and animation complexity on mobile

**DON'T:**
- Use pure white (#ffffff) as page background (use #faf9f5 or #f3f1ea)
- Use pure black (#000000) for text (use #141413)
- Use blue as the primary accent color
- Use glass morphism / backdrop-filter blur
- Use Inter, Roboto, or Arial for body text
- Use purple gradients anywhere
- Center everything
- Use more than 2 accent colors per page
- Animate with bounce/elastic easing
- Create dense, cramped layouts without breathing room
- Use icon-only navigation without labels
- Use `user-scalable=no` on the viewport meta (accessibility violation)
- Rely on hover-only interactions (they don't exist on touch)
- Use font-size below 16px for inputs (triggers iOS zoom)
- Put destructive actions in the thumb easy-reach zone
- Use fixed background-attachment on mobile (causes scroll jank)
- Show desktop tables on mobile (transform to card lists)

---

## 14. Technology Stack Recommendations

### 14.1 Vanilla HTML/CSS
Best for: Static sites, documentation, landing pages.
Use the CSS custom properties directly. No build step needed.

### 14.2 React + Tailwind
Best for: Web applications, dashboards, interactive tools.

```javascript
// tailwind.config.js — Claude Design System tokens
module.exports = {
  theme: {
    extend: {
      colors: {
        canvas:    '#f3f1ea',
        surface:   '#faf9f5',
        elevated:  '#ffffff',
        chrome:    '#faf9f5',
        accent: {
          DEFAULT: '#d97757',
          hover:   '#c4613f',
          active:  '#a84f2f',
          subtle:  '#f5e6de',
          text:    '#b85a3a',
        },
        text: {
          primary:   '#141413',
          secondary: '#5c5b57',
          tertiary:  '#8b8983',
          disabled:  '#b0aea5',
        },
        border: {
          DEFAULT: '#e8e6dc',
          strong:  '#d0cec4',
          interactive: '#b0aea5',
        },
        cblue: '#6a9bcc',
        cgreen: '#788c5d',
        cred: '#c44d3d',
        camber: '#c49132',
      },
      fontFamily: {
        serif: ['Lora', 'Georgia', 'Times New Roman', 'serif'],
        sans:  ['Poppins', '-apple-system', 'BlinkMacSystemFont', 'sans-serif'],
        mono:  ['Fira Code', 'JetBrains Mono', 'monospace'],
      },
      borderRadius: {
        xs:  '2px',
        sm:  '4px',
        md:  '8px',
        lg:  '12px',
        xl:  '16px',
        '2xl': '24px',
      },
      boxShadow: {
        card: '0 4px 6px rgba(20,20,19,0.05), 0 2px 4px rgba(20,20,19,0.03), 0 1px 2px rgba(20,20,19,0.02)',
        dropdown: '0 10px 15px rgba(20,20,19,0.06), 0 4px 6px rgba(20,20,19,0.04), 0 2px 4px rgba(20,20,19,0.02)',
        modal: '0 25px 50px rgba(20,20,19,0.12), 0 12px 24px rgba(20,20,19,0.06)',
      },
    },
  },
}
```

### 14.3 Next.js / App Router
Same Tailwind config. Use `next/font` for optimal font loading:

```javascript
import { Lora, Poppins, Fira_Code } from 'next/font/google';

const lora = Lora({ subsets: ['latin'], variable: '--font-serif' });
const poppins = Poppins({ subsets: ['latin'], weight: ['300','400','500','600','700'], variable: '--font-sans' });
const firaCode = Fira_Code({ subsets: ['latin'], variable: '--font-mono' });

// Apply to <html> className:
// `${lora.variable} ${poppins.variable} ${firaCode.variable}`
```

---

## 15. State Patterns

### 15.1 Component States

Every interactive component supports these states:

| State | Visual Treatment |
|-------|-----------------|
| Default | Base styling per component spec |
| Hover | Subtle background highlight, shadow increase, cursor: pointer |
| Focus | Orange focus ring (2px solid, 2px offset) |
| Active/Pressed | Slightly dimmed, transform removed, shadow reduced |
| Disabled | 50% opacity, cursor: not-allowed, no transitions |
| Loading | Spinner replaces label or skeleton shimmer |
| Error | Red border, red helper text, red icon |
| Success | Green indicator, optional checkmark icon |

### 15.2 Form Validation States

```css
/* Error state */
.input--error {
  border-color: var(--color-red);
}
.input--error:focus {
  box-shadow: 0 0 0 3px rgba(196, 77, 61, 0.25);
}

/* Success state */
.input--success {
  border-color: var(--color-green);
}
.input--success:focus {
  box-shadow: 0 0 0 3px rgba(120, 140, 93, 0.25);
}

/* Error/Success messages */
.field-message {
  font-family: var(--font-sans);
  font-size: var(--text-xs);
  display: flex;
  align-items: center;
  gap: var(--space-1);
  margin-top: var(--space-1);
}

.field-message--error { color: var(--color-red); }
.field-message--success { color: var(--color-green); }
```

### 15.3 Page-Level States

```css
/* Loading page — full skeleton */
.page-loading {
  pointer-events: none;
  opacity: 0.6;
}

/* Error page */
.page-error {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 60vh;
  text-align: center;
  padding: var(--space-8);
}

/* Offline indicator */
.offline-banner {
  background: var(--color-amber-subtle);
  color: var(--color-amber);
  font-family: var(--font-sans);
  font-size: var(--text-sm);
  font-weight: var(--weight-medium);
  text-align: center;
  padding: var(--space-2) var(--space-4);
}
```

---

## 16. Toast / Notification Component

```css
.toast-container {
  position: fixed;
  bottom: var(--space-6);
  right: var(--space-6);
  z-index: var(--z-toast);
  display: flex;
  flex-direction: column-reverse;
  gap: var(--space-3);
  pointer-events: none;
}

.toast {
  background: var(--color-surface-elevated);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow-lg);
  padding: var(--space-4) var(--space-5);
  display: flex;
  align-items: flex-start;
  gap: var(--space-3);
  max-width: 420px;
  min-width: 300px;
  pointer-events: auto;
  animation: slideInUp var(--duration-slow) var(--ease-spring) both;
}

@keyframes slideInUp {
  from {
    opacity: 0;
    transform: translateY(16px) scale(0.95);
  }
  to {
    opacity: 1;
    transform: translateY(0) scale(1);
  }
}

.toast__icon {
  flex-shrink: 0;
  width: 20px;
  height: 20px;
  margin-top: 2px;
}

.toast__content {
  flex: 1;
}

.toast__title {
  font-family: var(--font-sans);
  font-size: var(--text-sm);
  font-weight: var(--weight-semibold);
  color: var(--color-text-primary);
}

.toast__message {
  font-family: var(--font-sans);
  font-size: var(--text-sm);
  color: var(--color-text-secondary);
  margin-top: var(--space-1);
}

.toast__close {
  flex-shrink: 0;
  background: none;
  border: none;
  color: var(--color-text-tertiary);
  cursor: pointer;
  padding: var(--space-1);
  border-radius: var(--radius-sm);
}

.toast__close:hover {
  background: var(--color-highlight);
  color: var(--color-text-primary);
}

/* Variants */
.toast--success { border-left: 3px solid var(--color-green); }
.toast--success .toast__icon { color: var(--color-green); }

.toast--error { border-left: 3px solid var(--color-red); }
.toast--error .toast__icon { color: var(--color-red); }

.toast--warning { border-left: 3px solid var(--color-amber); }
.toast--warning .toast__icon { color: var(--color-amber); }

.toast--info { border-left: 3px solid var(--color-blue); }
.toast--info .toast__icon { color: var(--color-blue); }

@media (max-width: 640px) {
  .toast-container {
    left: var(--space-4);
    right: var(--space-4);
    bottom: var(--space-4);
  }
  .toast {
    max-width: none;
    min-width: auto;
  }
}
```

---

## 17. View Transitions

### 17.1 Native View Transitions API

```css
/* Opt-in to View Transitions */
@view-transition {
  navigation: auto;
}

/* Name transition targets */
.page-title { view-transition-name: page-title; }
.hero-image { view-transition-name: hero-image; }
.navbar     { view-transition-name: navbar; }

/* Custom animations for transitions */
::view-transition-old(page-title) {
  animation: fadeOut var(--duration-normal) var(--ease-default);
}

::view-transition-new(page-title) {
  animation: fadeInUp var(--duration-slow) var(--ease-editorial);
}

/* Crossfade for images */
::view-transition-old(hero-image) {
  animation: fadeOut var(--duration-slow) var(--ease-default);
}

::view-transition-new(hero-image) {
  animation: fadeIn var(--duration-slow) var(--ease-default);
}

/* Navbar persists — no animation */
::view-transition-old(navbar),
::view-transition-new(navbar) {
  animation: none;
}

@keyframes fadeOut {
  to { opacity: 0; }
}
```

### 17.2 Fallback Pattern

```javascript
// Feature detection for View Transitions
if (!document.startViewTransition) {
  // Fallback: simple CSS class-based transitions
  document.documentElement.classList.add('no-view-transitions');
}
```

```css
/* Fallback when View Transitions not supported */
.no-view-transitions .page-enter {
  animation: fadeInUp var(--duration-slow) var(--ease-editorial) both;
}
```

---

## 18. Composition Rules

### 18.1 Surface Stacking

Never place a card directly on another card. Always use the surface hierarchy:
- **Canvas → Surface → Elevated** is correct
- **Elevated → Elevated** is wrong (creates visual confusion)
- **Canvas → Elevated** is acceptable (skipping one level is fine)

### 18.2 Shadow Rules

1. Shadows increase as z-index increases — never use --shadow-xl on a low-z element.
2. Don't combine borders AND shadows on the same component unless it's a focus state.
3. Hover shadows should be exactly one step up from resting (md → lg, sm → md).

### 18.3 Color Composition

1. **One accent per view** — the rust-orange (#d97757) is your one accent. Never introduce competing accent hues.
2. **Semantic colors for state only** — green, red, amber are ONLY for success/error/warning. Never use them decoratively.
3. **Maximum two surface colors per section** — canvas + surface, or surface + elevated. Never all three visible simultaneously.

### 18.4 Typography Composition

1. **Serif headings → serif body** within content sections.
2. **Sans-serif** only for: labels, buttons, badges, metadata, navigation, overlines.
3. **Maximum two sizes per visual group** — a heading and a body. If you need a third, use weight or color instead of size.
4. **Line length** — body text never exceeds 65ch. Headings never exceed 25ch (break early for impact).

### 18.5 Spacing Composition

1. **Related items: small gap** (space-2 to space-4)
2. **Distinct groups: medium gap** (space-6 to space-8)
3. **Sections: large gap** (space-12 to space-16)
4. **The gap between label and input is always space-2**
5. **The gap between card sections is always space-4**
6. **Page padding is always space-8**

---

## 19. Naming Conventions

### 19.1 CSS Class Naming

The Claude Design System uses **BEM-lite** — Block, Element, Modifier, but without strict double-underscore/double-dash everywhere.

**Pattern:** `.block`, `.block__element`, `.block--modifier`

**Examples:**
```css
.card { }              /* Block */
.card__header { }      /* Element */
.card__title { }       /* Element */
.card--accent { }      /* Modifier */
.card--static { }      /* Modifier */
```

**Utility classes:** `.u-` prefix for utilities: `.u-text-center`, `.u-sr-only`

**State classes:** `is-` or `has-` prefix: `.is-active`, `.is-loading`, `.has-error`

**JavaScript hooks:** `[data-*]` attributes, never CSS classes: `[data-modal-trigger]`, `[data-tooltip]`

### 19.2 Token Naming

- Colors: `--color-[role]-[variant]` → `--color-accent-hover`
- Spacing: `--space-[scale]` → `--space-4`
- Typography: `--text-[scale]` → `--text-lg`, `--font-[family]` → `--font-serif`
- Shadows: `--shadow-[scale]` → `--shadow-md`, `--shadow-[component]` → `--shadow-card`
- Radii: `--radius-[scale]` → `--radius-lg`
- Z-index: `--z-[layer]` → `--z-modal`
- Animation: `--duration-[speed]` → `--duration-slow`, `--ease-[type]` → `--ease-editorial`

### 19.3 File Naming

```
styles/
  tokens.css          — Design tokens (custom properties)
  reset.css           — Base reset
  typography.css      — Type styles
  components/
    card.css
    button.css
    input.css
    modal.css
    toast.css
    ...
  layouts/
    app-shell.css
    grid.css
    page.css
  utilities.css       — Utility classes
  animations.css      — Keyframes and animation classes
```

---

## 20. File Structure

### 20.1 Project Structure

```
project/
├── public/
│   ├── fonts/            # Self-hosted fonts (Lora, Poppins, Fira Code)
│   └── images/
├── src/
│   ├── styles/
│   │   ├── tokens.css    # All CSS custom properties
│   │   ├── reset.css     # Base normalization
│   │   ├── global.css    # Base typography, links, etc.
│   │   ├── components/   # One CSS file per component
│   │   ├── layouts/      # Layout patterns
│   │   ├── utilities.css # Utility classes
│   │   └── animations.css
│   ├── components/       # UI components (React/Vue/etc.)
│   ├── layouts/          # Page layouts
│   ├── pages/            # Page compositions
│   └── lib/              # Utilities, hooks
├── .claude-design.json   # Optional: design system config
└── README.md
```

### 20.2 CSS Load Order

```html
<!-- 1. Tokens first — everything depends on these -->
<link rel="stylesheet" href="tokens.css" />
<!-- 2. Reset & base -->
<link rel="stylesheet" href="reset.css" />
<link rel="stylesheet" href="global.css" />
<!-- 3. Components -->
<link rel="stylesheet" href="components/card.css" />
<link rel="stylesheet" href="components/button.css" />
<!-- ... -->
<!-- 4. Layouts -->
<link rel="stylesheet" href="layouts/app-shell.css" />
<!-- 5. Utilities last (override power) -->
<link rel="stylesheet" href="utilities.css" />
<!-- 6. Animations -->
<link rel="stylesheet" href="animations.css" />
```

---

## 21. Utility Classes

```css
/* ============================================
   CLAUDE DESIGN SYSTEM — Utility Classes
   ============================================ */

/* --- Layout --- */
.u-flex          { display: flex; }
.u-flex-col      { display: flex; flex-direction: column; }
.u-flex-wrap     { flex-wrap: wrap; }
.u-flex-center   { display: flex; align-items: center; justify-content: center; }
.u-flex-between  { display: flex; align-items: center; justify-content: space-between; }
.u-flex-end      { display: flex; justify-content: flex-end; }
.u-items-start   { align-items: flex-start; }
.u-items-center  { align-items: center; }
.u-items-end     { align-items: flex-end; }
.u-grid          { display: grid; }
.u-inline-flex   { display: inline-flex; }
.u-block         { display: block; }
.u-inline        { display: inline; }
.u-w-full        { width: 100%; }
.u-max-w-prose   { max-width: 65ch; }
.u-max-w-sm      { max-width: 480px; }
.u-max-w-md      { max-width: 720px; }
.u-max-w-lg      { max-width: 960px; }
.u-max-w-xl      { max-width: 1200px; }

/* --- Spacing --- */
.u-gap-1   { gap: var(--space-1); }
.u-gap-2   { gap: var(--space-2); }
.u-gap-3   { gap: var(--space-3); }
.u-gap-4   { gap: var(--space-4); }
.u-gap-6   { gap: var(--space-6); }
.u-gap-8   { gap: var(--space-8); }

.u-p-0     { padding: 0; }
.u-p-2     { padding: var(--space-2); }
.u-p-4     { padding: var(--space-4); }
.u-p-6     { padding: var(--space-6); }
.u-p-8     { padding: var(--space-8); }

.u-px-4    { padding-left: var(--space-4); padding-right: var(--space-4); }
.u-px-6    { padding-left: var(--space-6); padding-right: var(--space-6); }
.u-px-8    { padding-left: var(--space-8); padding-right: var(--space-8); }
.u-py-4    { padding-top: var(--space-4); padding-bottom: var(--space-4); }
.u-py-8    { padding-top: var(--space-8); padding-bottom: var(--space-8); }
.u-py-12   { padding-top: var(--space-12); padding-bottom: var(--space-12); }
.u-py-16   { padding-top: var(--space-16); padding-bottom: var(--space-16); }

.u-m-auto  { margin: auto; }
.u-mx-auto { margin-left: auto; margin-right: auto; }
.u-mt-4    { margin-top: var(--space-4); }
.u-mt-8    { margin-top: var(--space-8); }
.u-mt-12   { margin-top: var(--space-12); }
.u-mb-4    { margin-bottom: var(--space-4); }
.u-mb-8    { margin-bottom: var(--space-8); }

/* --- Typography --- */
.u-font-serif    { font-family: var(--font-serif); }
.u-font-sans     { font-family: var(--font-sans); }
.u-font-mono     { font-family: var(--font-mono); }
.u-text-xs       { font-size: var(--text-xs); }
.u-text-sm       { font-size: var(--text-sm); }
.u-text-base     { font-size: var(--text-base); }
.u-text-lg       { font-size: var(--text-lg); }
.u-text-xl       { font-size: var(--text-xl); }
.u-text-2xl      { font-size: var(--text-2xl); }
.u-text-3xl      { font-size: var(--text-3xl); }
.u-weight-regular { font-weight: var(--weight-regular); }
.u-weight-medium  { font-weight: var(--weight-medium); }
.u-weight-semibold { font-weight: var(--weight-semibold); }
.u-weight-bold   { font-weight: var(--weight-bold); }
.u-italic        { font-style: italic; }
.u-uppercase     { text-transform: uppercase; letter-spacing: var(--tracking-widest); }
.u-text-left     { text-align: left; }
.u-text-center   { text-align: center; }
.u-text-right    { text-align: right; }
.u-truncate      { overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
.u-line-clamp-2  { display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden; }
.u-line-clamp-3  { display: -webkit-box; -webkit-line-clamp: 3; -webkit-box-orient: vertical; overflow: hidden; }

/* --- Colors --- */
.u-text-primary   { color: var(--color-text-primary); }
.u-text-secondary { color: var(--color-text-secondary); }
.u-text-tertiary  { color: var(--color-text-tertiary); }
.u-text-accent    { color: var(--color-accent-text); }
.u-bg-canvas      { background-color: var(--color-canvas); }
.u-bg-surface     { background-color: var(--color-surface); }
.u-bg-elevated    { background-color: var(--color-surface-elevated); }
.u-bg-accent      { background-color: var(--color-accent-subtle); }

/* --- Borders & Radius --- */
.u-border         { border: 1px solid var(--color-border); }
.u-border-strong  { border: 1px solid var(--color-border-strong); }
.u-border-bottom  { border-bottom: 1px solid var(--color-border); }
.u-border-top     { border-top: 1px solid var(--color-border); }
.u-rounded-none   { border-radius: 0; }
.u-rounded-sm     { border-radius: var(--radius-sm); }
.u-rounded-md     { border-radius: var(--radius-md); }
.u-rounded-lg     { border-radius: var(--radius-lg); }
.u-rounded-xl     { border-radius: var(--radius-xl); }
.u-rounded-full   { border-radius: var(--radius-full); }

/* --- Shadows --- */
.u-shadow-none    { box-shadow: none; }
.u-shadow-sm      { box-shadow: var(--shadow-sm); }
.u-shadow-md      { box-shadow: var(--shadow-md); }
.u-shadow-lg      { box-shadow: var(--shadow-lg); }
.u-shadow-xl      { box-shadow: var(--shadow-xl); }

/* --- Visibility & Interaction --- */
.u-sr-only {
  position: absolute; width: 1px; height: 1px;
  padding: 0; margin: -1px; overflow: hidden;
  clip: rect(0,0,0,0); white-space: nowrap; border: 0;
}
.u-hidden       { display: none !important; }
.u-visible      { visibility: visible; }
.u-invisible    { visibility: hidden; }
.u-pointer      { cursor: pointer; }
.u-no-pointer   { pointer-events: none; }
.u-overflow-hidden { overflow: hidden; }
.u-overflow-auto   { overflow: auto; }
.u-relative     { position: relative; }
.u-absolute     { position: absolute; }
.u-sticky       { position: sticky; }
.u-opacity-50   { opacity: 0.5; }
.u-opacity-75   { opacity: 0.75; }

/* --- Responsive visibility --- */
@media (max-width: 768px) {
  .u-hide-mobile { display: none !important; }
}
@media (min-width: 769px) {
  .u-hide-desktop { display: none !important; }
}
```

---

## 22. Browser Support Matrix

| Feature | Chrome/Edge | Safari | Firefox | Notes |
|---------|------------|--------|---------|-------|
| CSS Custom Properties | 49+ ✅ | 9.1+ ✅ | 31+ ✅ | Core dependency |
| `prefers-color-scheme` | 76+ ✅ | 12.1+ ✅ | 67+ ✅ | Dark mode |
| `prefers-reduced-motion` | 74+ ✅ | 10.1+ ✅ | 63+ ✅ | A11y animations |
| `prefers-contrast` | 96+ ✅ | 14.1+ ✅ | 101+ ✅ | High contrast |
| View Transitions API | 111+ ✅ | 18+ ✅ | ❌ | Progressive enhance |
| Container Queries | 105+ ✅ | 16+ ✅ | 110+ ✅ | Responsive components |
| `:has()` selector | 105+ ✅ | 15.4+ ✅ | 121+ ✅ | Parent selection |
| `color-scheme` | 81+ ✅ | 13+ ✅ | 96+ ✅ | System theme |
| `dvh` / `svh` units | 108+ ✅ | 15.4+ ✅ | 101+ ✅ | Viewport units |
| `@layer` | 99+ ✅ | 15.4+ ✅ | 97+ ✅ | CSS cascade |
| Scroll-driven animations | 115+ ✅ | ❌ | ❌ | Progressive enhance |
| `text-wrap: balance` | 114+ ✅ | 17.5+ ✅ | 121+ ✅ | Headline wrapping |
| CSS Nesting | 120+ ✅ | 17.2+ ✅ | 117+ ✅ | Write nested CSS |

### Feature Detection

```javascript
// JavaScript feature detection
const features = {
  viewTransitions: !!document.startViewTransition,
  containerQueries: CSS.supports('container-type', 'inline-size'),
  hasSelector: CSS.supports('selector(:has(*))'),
  scrollAnimations: CSS.supports('animation-timeline', 'scroll()'),
};

// Apply feature classes to <html>
Object.entries(features).forEach(([key, supported]) => {
  document.documentElement.classList.toggle(`has-${key}`, supported);
  document.documentElement.classList.toggle(`no-${key}`, !supported);
});
```

---

## 23. Page Templates

### 23.1 Template: Chat Interface (Claude-style)

The signature Claude layout — sidebar + conversational main area.

```html
<!DOCTYPE html>
<html lang="en" class="claude-ds">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Chat — Claude Design System</title>
  <!-- Font loading -->
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,400;0,500;0,600;0,700;1,400&family=Poppins:wght@400;500;600&family=Fira+Code:wght@400&display=swap" rel="stylesheet" />
</head>
<body>
  <div class="app-shell">
    <!-- Sidebar -->
    <aside class="sidebar" aria-label="Conversations">
      <div class="sidebar__header u-flex-between u-mb-4">
        <a href="/" class="navbar__brand">
          <span class="navbar__brand-name">Claude</span>
        </a>
        <button class="button button--ghost button--icon" aria-label="New conversation">
          <!-- Lucide: plus icon -->
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="12" y1="5" x2="12" y2="19"/><line x1="5" y1="12" x2="19" y2="12"/></svg>
        </button>
      </div>
      <div class="sidebar__section">
        <div class="sidebar__section-title">Today</div>
        <a href="#" class="sidebar__item sidebar__item--active">Design system conversation</a>
        <a href="#" class="sidebar__item">API integration help</a>
        <a href="#" class="sidebar__item">Research summary</a>
      </div>
      <div class="sidebar__section">
        <div class="sidebar__section-title">Yesterday</div>
        <a href="#" class="sidebar__item">Code review feedback</a>
        <a href="#" class="sidebar__item">Meeting notes draft</a>
      </div>
    </aside>

    <!-- Main chat area -->
    <main class="app-shell__main">
      <div class="chat-area" role="log" aria-label="Conversation">
        <div class="chat-area__messages">
          <!-- User message -->
          <div class="message message--user">
            <div class="message__content">
              <p>Can you help me understand how Constitutional AI works?</p>
            </div>
          </div>

          <!-- Assistant message -->
          <div class="message message--assistant stagger-in">
            <div class="message__avatar">
              <div class="avatar avatar--sm" style="background: var(--color-accent-subtle); color: var(--color-accent-text);">C</div>
            </div>
            <div class="message__content">
              <p>Constitutional AI is Anthropic's approach to training AI systems to be helpful and harmless...</p>
            </div>
          </div>
        </div>

        <!-- Input area -->
        <div class="chat-input">
          <div class="chat-input__container">
            <textarea class="chat-input__field" placeholder="Message Claude..." rows="1" aria-label="Your message"></textarea>
            <button class="button button--primary button--icon chat-input__send" aria-label="Send message">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="22" y1="2" x2="11" y2="13"/><polygon points="22 2 15 22 11 13 2 9 22 2"/></svg>
            </button>
          </div>
        </div>
      </div>
    </main>
  </div>
</body>
</html>
```

```css
/* Chat-specific styles */
.chat-area {
  display: flex;
  flex-direction: column;
  height: 100dvh;
}

.chat-area__messages {
  flex: 1;
  overflow-y: auto;
  padding: var(--space-8) var(--padding-page);
  max-width: 720px;
  margin: 0 auto;
  width: 100%;
}

.message {
  display: flex;
  gap: var(--space-4);
  margin-bottom: var(--space-8);
}

.message--user {
  justify-content: flex-end;
}

.message--user .message__content {
  background: var(--color-surface-elevated);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-lg) var(--radius-lg) var(--radius-xs) var(--radius-lg);
  padding: var(--space-4) var(--space-5);
  max-width: 85%;
  box-shadow: var(--shadow-sm);
}

.message--assistant .message__content {
  max-width: 85%;
}

.message__content p {
  font-family: var(--font-serif);
  font-size: var(--text-base);
  line-height: var(--leading-normal);
}

.chat-input {
  border-top: 1px solid var(--color-border);
  padding: var(--space-4) var(--padding-page);
  background: var(--color-surface);
}

.chat-input__container {
  max-width: 720px;
  margin: 0 auto;
  display: flex;
  align-items: flex-end;
  gap: var(--space-3);
  background: var(--color-surface-elevated);
  border: 1px solid var(--color-border-interactive);
  border-radius: var(--radius-xl);
  padding: var(--space-3) var(--space-4);
  box-shadow: var(--shadow-sm);
  transition: border-color var(--duration-fast) var(--ease-default),
              box-shadow var(--duration-fast) var(--ease-default);
}

.chat-input__container:focus-within {
  border-color: var(--color-border-focus);
  box-shadow: var(--shadow-focus);
}

.chat-input__field {
  flex: 1;
  border: none;
  outline: none;
  resize: none;
  font-family: var(--font-serif);
  font-size: var(--text-base);
  line-height: var(--leading-normal);
  color: var(--color-text-primary);
  background: transparent;
  min-height: 24px;
  max-height: 200px;
}

.chat-input__field::placeholder {
  color: var(--color-text-disabled);
}

.chat-input__send {
  border-radius: var(--radius-full);
  flex-shrink: 0;
}
```

### 23.2 Template: Settings Page

```html
<main class="page page--narrow u-py-12">
  <div class="stagger-in">
    <header class="section__header u-mb-8">
      <h1 class="section__title">Settings</h1>
      <p class="section__subtitle">Manage your account preferences and configuration.</p>
    </header>

    <!-- Profile Section -->
    <section class="card card--static u-mb-6">
      <h3 class="u-font-sans u-text-lg u-weight-semibold u-mb-4">Profile</h3>
      <div class="stack">
        <div class="input-group">
          <label class="input-label" for="name">Display name</label>
          <input class="input" type="text" id="name" value="Des" />
        </div>
        <div class="input-group">
          <label class="input-label" for="email">Email</label>
          <input class="input" type="email" id="email" value="des@example.com" />
        </div>
      </div>
    </section>

    <!-- Preferences Section -->
    <section class="card card--static u-mb-6">
      <h3 class="u-font-sans u-text-lg u-weight-semibold u-mb-4">Preferences</h3>
      <div class="stack">
        <div class="u-flex-between">
          <div>
            <p class="u-font-sans u-text-sm u-weight-medium">Dark mode</p>
            <p class="u-font-sans u-text-xs u-text-tertiary">Automatically switch based on system preference</p>
          </div>
          <input type="checkbox" class="toggle" aria-label="Toggle dark mode" />
        </div>
        <hr class="divider--subtle" />
        <div class="u-flex-between">
          <div>
            <p class="u-font-sans u-text-sm u-weight-medium">Email notifications</p>
            <p class="u-font-sans u-text-xs u-text-tertiary">Receive updates about your conversations</p>
          </div>
          <input type="checkbox" class="toggle" aria-label="Toggle notifications" checked />
        </div>
      </div>
    </section>

    <!-- Actions -->
    <div class="cluster cluster--end">
      <button class="button button--secondary">Cancel</button>
      <button class="button button--primary">Save changes</button>
    </div>
  </div>
</main>
```

### 23.3 Template: Dashboard

```html
<div class="app-shell">
  <aside class="sidebar" aria-label="Navigation">
    <div class="sidebar__section">
      <div class="sidebar__section-title">Overview</div>
      <a href="#" class="sidebar__item sidebar__item--active">Dashboard</a>
      <a href="#" class="sidebar__item">Analytics</a>
      <a href="#" class="sidebar__item">Reports</a>
    </div>
    <div class="sidebar__section">
      <div class="sidebar__section-title">Manage</div>
      <a href="#" class="sidebar__item">Team</a>
      <a href="#" class="sidebar__item">Settings</a>
    </div>
  </aside>

  <main class="app-shell__main">
    <nav class="navbar">
      <h2 class="navbar__brand-name">Dashboard</h2>
      <div class="navbar__actions">
        <button class="button button--secondary button--sm">Export</button>
        <button class="button button--primary button--sm">New report</button>
      </div>
    </nav>

    <div class="app-shell__content stagger-in">
      <!-- Metric cards -->
      <div class="grid grid--4 u-mb-8">
        <div class="card card--static">
          <span class="overline">Total Conversations</span>
          <p class="u-text-3xl u-weight-bold u-font-sans u-mt-2">12,847</p>
          <span class="badge badge--success u-mt-2">↑ 12.5%</span>
        </div>
        <div class="card card--static">
          <span class="overline">Active Users</span>
          <p class="u-text-3xl u-weight-bold u-font-sans u-mt-2">3,241</p>
          <span class="badge badge--success u-mt-2">↑ 8.3%</span>
        </div>
        <div class="card card--static">
          <span class="overline">Avg. Response Time</span>
          <p class="u-text-3xl u-weight-bold u-font-sans u-mt-2">1.2s</p>
          <span class="badge badge--success u-mt-2">↓ 15.0%</span>
        </div>
        <div class="card card--static">
          <span class="overline">Satisfaction</span>
          <p class="u-text-3xl u-weight-bold u-font-sans u-mt-2">94.7%</p>
          <span class="badge badge--warning u-mt-2">↓ 0.3%</span>
        </div>
      </div>

      <!-- Chart area -->
      <div class="card card--static u-mb-8">
        <div class="card__header u-flex-between">
          <h3 class="u-font-sans u-text-lg u-weight-semibold">Usage Over Time</h3>
          <div class="cluster">
            <button class="button button--ghost button--sm">7d</button>
            <button class="button button--ghost button--sm is-active">30d</button>
            <button class="button button--ghost button--sm">90d</button>
          </div>
        </div>
        <div class="card__body" style="height: 300px;">
          <!-- Chart rendered here -->
        </div>
      </div>

      <!-- Data table -->
      <div class="card card--static card--flush">
        <div class="u-p-6 u-flex-between">
          <h3 class="u-font-sans u-text-lg u-weight-semibold">Recent Activity</h3>
          <div class="search" style="width: 240px;">
            <input class="search__input input" type="search" placeholder="Search..." />
          </div>
        </div>
        <table class="table" role="table">
          <thead>
            <tr>
              <th>User</th>
              <th>Conversation</th>
              <th>Duration</th>
              <th>Status</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><div class="u-flex u-items-center u-gap-3"><div class="avatar avatar--sm">JS</div><span>Jane Smith</span></div></td>
              <td class="u-truncate" style="max-width: 240px;">Help with API integration for payment system</td>
              <td>4m 23s</td>
              <td><span class="badge badge--success">Complete</span></td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </main>
</div>
```

```css
/* Table styles */
.table {
  width: 100%;
  border-collapse: collapse;
  font-family: var(--font-sans);
  font-size: var(--text-sm);
}

.table thead {
  border-bottom: 1px solid var(--color-border-strong);
}

.table th {
  text-align: left;
  padding: var(--space-3) var(--space-4);
  font-weight: var(--weight-medium);
  color: var(--color-text-tertiary);
  font-size: var(--text-xs);
  letter-spacing: var(--tracking-wider);
  text-transform: uppercase;
}

.table td {
  padding: var(--space-3) var(--space-4);
  color: var(--color-text-primary);
  border-bottom: 1px solid var(--color-border);
}

.table tbody tr:hover {
  background: var(--color-highlight);
}

.table tbody tr:last-child td {
  border-bottom: none;
}
```

---

## 24. Quick Start Guide

### 24.1 Vanilla HTML/CSS — Minimal Boilerplate

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>My Claude-Styled App</title>

  <!-- Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,400;0,500;0,600;0,700;1,400&family=Poppins:wght@300;400;500;600;700&family=Fira+Code:wght@400;500&display=swap" rel="stylesheet" />

  <style>
    /* Paste design tokens from Section 2 here */
    /* Paste reset from Section 3.1 here */
    /* Add component CSS as needed */
  </style>
</head>
<body>
  <main class="page page--narrow u-py-12 stagger-in">
    <h1>Welcome to Your App</h1>
    <p class="text-lead">Built with the Claude Design System — warm, editorial, and refined.</p>
  </main>
</body>
</html>
```

### 24.2 React + Tailwind — Minimal Setup

1. Install Tailwind CSS
2. Configure `tailwind.config.js` with Claude tokens (see Section 14.2)
3. Add Google Fonts to `<head>` or use `next/font`
4. Create a `<ClaudeTheme>` wrapper component:

```jsx
// components/ClaudeTheme.jsx
export default function ClaudeTheme({ children }) {
  return (
    <div className="min-h-screen bg-canvas text-text-primary font-serif antialiased">
      {children}
    </div>
  );
}
```

### 24.3 Pre-Build Checklist

```
□ Design tokens file created (CSS custom properties)
□ Fonts loaded (Lora, Poppins, Fira Code)
□ Base reset applied
□ Dark mode tokens defined
□ Focus styles set (orange ring)
□ Viewport meta tag present
□ Color-scheme meta tag present
□ Safe area padding applied
```

### 24.4 Pre-Deploy Checklist

```
□ Design pre-flight answered (purpose, hierarchy, hero, motion, warmth)
□ All surfaces follow layer hierarchy (canvas → surface → elevated)
□ Z-index scale followed (no magic numbers)
□ Light mode tested — backgrounds are warm, not white
□ Dark mode tested — backgrounds are warm-dark, not cold-dark
□ Reduced-motion tested — all animations disabled gracefully
□ Touch targets minimum 44x44px on mobile
□ Contrast checker passed (WCAG AA minimum)
□ Heading hierarchy correct (h1 > h2 > h3, no skips)
□ Lighthouse audit: Accessibility ≥ 95, Performance ≥ 90
□ 60fps verified for all transitions
□ Fonts loaded — no FOIT visible
```

---

## 25. Typography Reference & Font Selection Guide

### 25.1 The Claude Typographic Voice

The Claude Design System's typography is its most distinctive feature. Where most tech products default to sans-serif everything, Claude leads with serif — a deliberate choice that signals humanity, editorial quality, and literary heritage.

**The founding pair:**
- **Tiempos** (Klim Type Foundry) — Anthropic's brand serif. Warm, contemporary, rooted in traditional newsprint design. Used for body text and headings on anthropic.com.
- **Styrene** (Commercial Type) — Anthropic's brand sans-serif. Geometric but slightly quirky — the f, j, r, t are wider than expected. Used for UI elements and labels.

Both are commercial fonts. For web projects, the system provides open-source equivalents:

### 25.2 Recommended Fonts

**Tier 1 — Primary UI Fonts (use these)**

| Font | Type | Role | Google Fonts Load | Why It Works |
|------|------|------|-------------------|-------------|
| **Lora** ⭐ | Serif | Body text, headings | `Lora:ital,wght@0,400;0,500;0,600;0,700;1,400;1,500` | Warm brushed serifs, excellent screen readability, contemporary yet classic. The closest free match to Tiempos's warmth. |
| **Poppins** ⭐ | Sans | UI labels, buttons, nav | `Poppins:wght@300;400;500;600;700` | Geometric, friendly, slightly rounded. Echoes Styrene's approachability without being quirky. |
| **Source Serif 4** | Serif | Alt body option | `Source+Serif+4:ital,wght@0,400;0,500;0,600;0,700;1,400` | Adobe's editorial serif. More structured than Lora. Excellent for long-form. |
| **DM Serif Display** | Serif | Display headings | `DM+Serif+Display:ital@0;1` | High-contrast, dramatic. Best for hero headings at 48px+. Pair with Poppins for UI. |

**Tier 2 — Alternative Pairings**

| Pairing | Mood | Best For |
|---------|------|---------|
| Lora + Poppins | Warm, friendly, editorial | Default — works for everything |
| Source Serif 4 + DM Sans | Structured, professional | Enterprise, documentation |
| Playfair Display + Work Sans | Dramatic, editorial | Marketing, editorial content |
| Bitter + Manrope | Sturdy, approachable | SaaS products, dashboards |

**Tier 3 — Avoid These**

| Font | Why |
|------|-----|
| Inter | Ubiquitous AI/tech default. Signals "generic template." |
| Roboto | Google's system font. Signals "Material Design clone." |
| Open Sans | Overused, personality-less. |
| Arial | System default. No editorial quality. |
| Montserrat | Overused in tech. Becoming the new "generic." |
| Times New Roman | System serif. Signals "didn't choose a font." |

### 25.3 Font Loading Strategy

```html
<!-- Optimal loading order -->
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />

<!-- Critical fonts: Lora (body) loads first, then Poppins (UI) -->
<link
  href="https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,400;0,500;0,600;0,700;1,400;1,500&family=Poppins:wght@300;400;500;600;700&family=Fira+Code:wght@400;500&display=swap"
  rel="stylesheet"
/>
```

**display=swap:** Prevents Flash of Invisible Text (FOIT). Text shows immediately in Georgia/Arial fallbacks, then swaps to web fonts when loaded.

**Self-hosting for production:**
For GDPR compliance or performance-critical applications, self-host fonts:
```
fonts/
├── lora/
│   ├── Lora-Regular.woff2
│   ├── Lora-Medium.woff2
│   ├── Lora-SemiBold.woff2
│   ├── Lora-Bold.woff2
│   ├── Lora-Italic.woff2
│   └── Lora-MediumItalic.woff2
├── poppins/
│   ├── Poppins-Light.woff2
│   ├── Poppins-Regular.woff2
│   ├── Poppins-Medium.woff2
│   ├── Poppins-SemiBold.woff2
│   └── Poppins-Bold.woff2
└── fira-code/
    ├── FiraCode-Regular.woff2
    └── FiraCode-Medium.woff2
```

### 25.4 Serif + Sans Pairing Rules

The Claude system's "serif for soul, sans for structure" principle requires disciplined application:

**Use SERIF (Lora) for:**
- Body paragraphs
- Headings h1, h2, h3
- Card titles and descriptions
- Blockquotes and pull-quotes
- Form input text (yes — inputs use serif)
- Chat message content
- Long-form reading content
- Article/post content

**Use SANS-SERIF (Poppins) for:**
- Navigation links
- Button labels
- Form labels
- Badges and tags
- Metadata (dates, counts, status)
- Overlines and section labels
- Sidebar items
- Tab labels
- Tooltip text
- Toast/notification text
- Table headers
- Caption text
- Breadcrumbs

**Use MONOSPACE (Fira Code) for:**
- Code blocks
- Inline code snippets
- Terminal/CLI output
- API endpoints
- Technical identifiers

### 25.5 Type Hierarchy in Practice

A well-composed Claude page uses no more than **4 type treatments** simultaneously:

```
┌──────────────────────────────────────┐
│ OVERLINE                             │  ← Sans, text-xs, uppercase, tracking-widest, tertiary
│                                      │
│ Main Heading in Serif                │  ← Serif, text-3xl, bold, primary
│                                      │
│ A supporting paragraph in serif      │
│ with comfortable line height and     │  ← Serif, text-base, regular, primary
│ generous spacing.                    │
│                                      │
│ Meta · Sans · 12px · tertiary       │  ← Sans, text-sm, tertiary
└──────────────────────────────────────┘
```

If you need a fifth treatment, use **weight** or **color** rather than adding a new size. The constraint creates visual harmony.

---

## 26. Color Theory & Palette Design

### 26.1 The Claude Color Philosophy

The Claude palette is fundamentally **warm and restrained**. It draws from natural materials — sand, parchment, terracotta, slate, sage — rather than from screens and pixels. This warmth is the single biggest differentiator from other AI product interfaces, which tend toward cold blues, purples, and sterile whites.

**The signature palette:**
```
Sand Canvas    ████████  #f3f1ea — The warm foundation
Cream Surface  ████████  #faf9f5 — Content areas
Near-Black     ████████  #141413 — Text (NOT pure black)
Rust Orange    ████████  #d97757 — The one accent that matters
Slate Blue     ████████  #6a9bcc — Informational, secondary
Sage Green     ████████  #788c5d — Success, positive
Terracotta Red ████████  #c44d3d — Error, destructive
Warm Amber     ████████  #c49132 — Warning, caution
```

### 26.2 Color Theory Applied to Warm UI

**Monochromatic warm palette** — The Claude system is fundamentally monochromatic: it's built on a range of warm browns/tans (the neutrals) with a single orange accent. This is the safest, most cohesive approach.

**Why one accent works:** In color theory, a single accent against a neutral field creates maximum impact with minimum visual noise. The rust-orange (#d97757) draws the eye precisely where needed — CTAs, active states, focus rings — without competing for attention.

**The 90/10 rule:** 90% of the interface is neutral (sand, cream, gray, charcoal). 10% is accent. If you find yourself using more accent, you're overusing it.

### 26.3 Warm vs. Cold Neutrals

The most important color decision in the Claude system is **using warm neutrals instead of cold ones**:

| Cold (avoid) | Warm (use) | Token |
|---|---|---|
| `#ffffff` pure white | `#faf9f5` cream | --color-surface |
| `#f5f5f5` cool gray | `#f3f1ea` sand | --color-canvas |
| `#e5e5e5` silver | `#e8e6dc` warm gray | --color-border |
| `#6b7280` slate | `#5c5b57` warm gray | --color-text-secondary |
| `#111827` blue-black | `#141413` warm black | --color-text-primary |
| `#000000` pure black | `#141413` near-black | Never use pure black |

**Dark mode warm neutrals:** Even in dark mode, backgrounds are warm-dark (`#1a1918`, `#242320`) not cold-dark (`#111827`, `#1e293b`). This is critical — cold dark mode destroys the Claude aesthetic.

### 26.4 Accent Color Deep Dive

The rust-orange accent (`#d97757`) is derived from Anthropic's brand. Here's its complete scale:

```css
:root {
  --accent-50:  #fef6f2;  /* Background tint */
  --accent-100: #f5e6de;  /* Subtle background */
  --accent-200: #ecc9b5;  /* Light background */
  --accent-300: #e3ac8d;  /* Muted */
  --accent-400: #d97757;  /* ★ PRIMARY — the brand accent */
  --accent-500: #c4613f;  /* Hover */
  --accent-600: #a84f2f;  /* Active / pressed */
  --accent-700: #8c3f24;  /* Dark variant */
  --accent-800: #6e311c;  /* Very dark */
  --accent-900: #502314;  /* Near-black accent */
}
```

**Usage guidance:**
- **accent-400:** CTAs, links, active sidebar items, focus rings, toggles
- **accent-100:** Subtle backgrounds (active tab bg, selected row, badge bg)
- **accent-500:** Hover states for primary buttons
- **accent-600:** Active/pressed states
- **accent-700+:** Text that needs to be accent-colored with guaranteed contrast on light backgrounds

### 26.5 Semantic Colors

Beyond the accent, four semantic colors cover all status/feedback needs:

```css
/* Each semantic color: main, subtle-bg, and text-safe */
--color-green:        #788c5d;  /* Success — sage green, not neon */
--color-green-subtle: #e5ead8;
--color-green-text:   #5e7040;  /* Contrast-safe on white */

--color-red:          #c44d3d;  /* Error — terracotta, not alarm red */
--color-red-subtle:   #f5dbd7;
--color-red-text:     #a33b2d;

--color-amber:        #c49132;  /* Warning — warm amber */
--color-amber-subtle: #f5ecd3;
--color-amber-text:   #9a7226;

--color-blue:         #6a9bcc;  /* Info — muted slate blue */
--color-blue-subtle:  #e0ecf4;
--color-blue-text:    #4a7da8;
```

**Critical rule:** Semantic colors are for STATE ONLY. Never use green decoratively, red for branding, or blue as a primary action color. The accent orange is the only "loud" color. Semantic colors are functional signals.

### 26.6 Dark Mode Color Strategy

Dark mode in the Claude system is NOT just "invert everything." It follows specific rules:

1. **Backgrounds warm up slightly** — dark mode backgrounds have warm undertones (brown-black, not blue-black)
2. **Text brightness reduces** — `#ece9e1` (warm off-white), not `#ffffff` (pure white, too bright)
3. **Accent brightens** — `#e08b6d` (lighter orange) to maintain contrast on dark surfaces
4. **Semantic colors lighten** — all status colors get 1-2 stops lighter for visibility
5. **Borders become translucent** — `rgba(255, 255, 255, 0.08)` instead of solid colors
6. **Shadows deepen dramatically** — dark mode shadows use `rgba(0, 0, 0, 0.30+)` because they need to be visible against dark surfaces

### 26.7 Data Visualization Palette

For charts and graphs, use this purpose-built palette that maintains distinctness and warm character:

```css
:root {
  --data-1: #d97757;  /* Orange (brand accent) */
  --data-2: #6a9bcc;  /* Blue */
  --data-3: #788c5d;  /* Green */
  --data-4: #c44d3d;  /* Red */
  --data-5: #c49132;  /* Amber */
  --data-6: #8b6e99;  /* Muted purple (only here, never in UI) */
  --data-7: #5c9a8f;  /* Teal */
  --data-8: #a67c5b;  /* Warm brown */
}
```

**Note:** Purple appears ONLY in data visualization, never in UI elements. This prevents it from becoming a competing accent.

### 26.8 Color Accessibility

```
□ All body text on canvas: minimum 4.5:1 contrast ratio
□ All body text on surface: minimum 4.5:1 contrast ratio
□ All large text (24px+): minimum 3:1 contrast ratio
□ All interactive elements: minimum 3:1 against background
□ Focus ring (orange): visible against both light and dark backgrounds
□ Error/success states: never rely on color alone (always pair with icon/text)
□ Colorblind-tested: protanopia, deuteranopia, tritanopia simulations
□ High contrast mode: solid borders replace shadows, colors darken
□ Reduced transparency: no translucent elements in the Claude system (already solid!)
```

### 26.9 Building Custom Brand Palettes

When extending the Claude system for a specific brand:

**Step 1:** Keep the warm neutral foundation (canvas, surface, elevated). This is non-negotiable — it IS the Claude aesthetic.

**Step 2:** Replace the accent. Swap `#d97757` with your brand's primary color, maintaining similar saturation (60-80%) and lightness (40-55%).

**Step 3:** Generate your accent scale following the pattern in Section 26.4.

**Step 4:** Keep semantic colors unchanged (green, red, amber, blue). These are functional, not brand.

**Step 5:** Test warmth. If your new accent is cool (blue, purple, teal), you MUST keep the warm neutrals. A cool accent on warm neutrals creates sophisticated contrast. A cool accent on cool neutrals destroys the Claude DNA.

---

*Document version: 1.1 — Based on Anthropic's brand identity (designed by Geist agency), the claude.ai product interface, Anthropic's official brand-guidelines skill, and Figma's typography and color theory best practices. Structured as comprehensive Codex instructions with mandatory patterns, naming conventions, file organization, page templates, deployment checklists, and complete mobile webapp transformation standards (Section 10).*
