# Design.md — Playlytics V3
# Visual Design Document

---

## Purpose

This document defines the visual identity of Playlytics V3.

Every UI decision references this document.
No colors, fonts, or spacing values are hardcoded
without being defined here first.

---

## Design Philosophy

- Clean and readable above all else
- Dark theme by default
- Results communicate meaning through color, not just text
- No decorative elements that do not serve a purpose
- Looks professional, not flashy

---

## Theme

### Base Theme
Dark

### Reasoning
- Easier on the eyes during extended sessions
- Common in gaming and developer tooling
- Provides strong contrast for severity colors

---

## Color Palette

### Background Colors

| Name            | Hex       | Usage                        |
|-----------------|-----------|------------------------------|
| Background      | #1E1E2E   | Main window background       |
| Surface         | #2A2A3E   | Card and panel backgrounds   |
| Surface Hover   | #313145   | Hovered elements             |
| Border          | #3A3A5C   | Borders and dividers         |

### Text Colors

| Name            | Hex       | Usage                        |
|-----------------|-----------|------------------------------|
| Text Primary    | #EDEDED   | Main readable text           |
| Text Secondary  | #A0A0B0   | Subtext, labels, hints       |
| Text Muted      | #606070   | Disabled or inactive text    |

### Severity Colors

| Severity  | Background | Border    | Text      |
|-----------|------------|-----------|-----------|
| SUCCESS   | #1E3A2F    | #2ECC71   | #2ECC71   |
| INFO      | #1A2A3A    | #3498DB   | #3498DB   |
| WARNING   | #3A2E1A    | #F39C12   | #F39C12   |
| ERROR     | #3A1E1E    | #E74C3C   | #E74C3C   |

### Accent Colors

| Name       | Hex       | Usage                         |
|------------|-----------|-------------------------------|
| Accent     | #7C6AF7   | Primary buttons, highlights   |
| Accent Alt | #5E5AC4   | Pressed button state          |

---

## Typography

### Font Family
System default monospace for input fields.
System default sans-serif for all other text.

Reasoning:
Avoids font loading complexity.
Tkinter handles system fonts reliably across platforms.

### Font Sizes

| Element          | Size | Weight  |
|------------------|------|---------|
| App Title        | 20   | Bold    |
| Section Header   | 14   | Bold    |
| Card Title       | 12   | Bold    |
| Card Message     | 11   | Normal  |
| Card Suggestion  | 10   | Normal  |
| Input Label      | 11   | Normal  |
| Input Field      | 11   | Normal  |
| Button           | 11   | Bold    |
| Footer / Muted   | 9    | Normal  |

---

## Layout

### Window

| Property      | Value              |
|---------------|--------------------|
| Min Width     | 600px              |
| Min Height    | 500px              |
| Default Width | 700px              |
| Default Height| 600px              |
| Resizable     | Yes                |
| Title         | Playlytics V3      |

### Padding and Spacing

| Property         | Value  |
|------------------|--------|
| Window Padding   | 20px   |
| Card Padding     | 12px   |
| Card Gap         | 8px    |
| Section Gap      | 16px   |
| Label Gap        | 6px    |

---

## Components

### Input Form

Layout: Vertical stack of labeled input fields.

Fields:
- Kills       (integer input)
- Deaths      (integer input)
- Accuracy    (float input, percentage)
- Gun Type    (text input or dropdown)

Button:
- Label: Analyze
- Color: Accent (#7C6AF7)
- Width: Full width of form
- Position: Below all input fields

Validation errors appear below the relevant field
or as an ERROR card in the results area.

---

### Result Card

Each RuleResult is displayed as one card.

Card Structure:
┌─────────────────────────────────────┐
│ [Severity Icon]  Rule Name          │
│                                     │
│ Message text here                   │
│                                     │
│ 💡 Suggestion text here (optional)  │
└─────────────────────────────────────┘

Card Border:
Left border only, 4px wide, severity color.

Card Background:
Severity background color.

Card Text:
Message in Text Primary color.
Suggestion in Text Secondary color.
Suggestion prefixed with 💡

---

### Severity Icons

| Severity | Icon |
|----------|------|
| SUCCESS  | ✅   |
| INFO     | ℹ️   |
| WARNING  | ⚠️   |
| ERROR    | ❌   |

---

### Results Area

Scrollable vertical list of result cards.
Appears below or beside the input form.
Empty state shows a placeholder message:

"Enter your match stats and press Analyze."

---

### K/D Display

Displayed as a summary line above the result cards.

Format:
K/D Ratio: 2.50

Color: Text Primary
Size: 13, Bold

---

## Application Layout

```
┌─────────────────────────────────────────┐
│  Playlytics V3                    v3.0.0│
├─────────────────────────────────────────┤
│                                         │
│  Kills       [        ]                 │
│  Deaths      [        ]                 │
│  Accuracy    [        ]                 │
│  Gun Type    [        ]                 │
│                                         │
│  [        Analyze         ]             │
│                                         │
├─────────────────────────────────────────┤
│                                         │
│  K/D Ratio: —                           │
│                                         │
│  ┌─────────────────────────────────┐    │
│  │ ✅  Strong Performance          │    │
│  │ Keep up the good work.          │    │
│  └─────────────────────────────────┘    │
│                                         │
│  ┌─────────────────────────────────┐    │
│  │ ⚠️  Survival Needs Work         │    │
│  │ Consider avoiding open areas.   │    │
│  │ 💡 Stay in cover more often.    │    │
│  └─────────────────────────────────┘    │
│                                         │
└─────────────────────────────────────────┘
```

---

## States

### Empty State
No results shown.
Placeholder text displayed in results area.
K/D shows a dash.

### Loading State
Not required for V3.0.0.
Analysis is synchronous and fast enough.

### Error State
ERROR severity card displayed.
Input fields remain editable.
User can correct and reanalyze.

### Success State
All result cards displayed.
K/D ratio shown.
Results scrollable if they exceed the visible area.

---

## Accessibility

- All text meets minimum contrast ratio against backgrounds
- Severity communicated through both color and icon
- No information conveyed by color alone
- Font sizes readable without zooming

---

## What Is Not In V3.0.0

- Light theme
- Custom fonts
- Animations or transitions
- Themes selector
- Responsive scaling beyond window resize
- Logo or custom icon (placeholder only)

These may be added in V3.1.0 or V3.2.0 if genuinely needed.

---

*This document is the single source of truth for*
*all visual decisions in Playlytics V3.*
*Any UI element not defined here requires*
*this document to be updated before implementation.*