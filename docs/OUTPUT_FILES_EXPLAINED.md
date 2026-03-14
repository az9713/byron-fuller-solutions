# Output Files Explained

A detailed guide explaining what each output file is, how they work together, and exactly what goes into the final `main.pdf`.

## Table of Contents

1. [Overview: The Big Picture](#overview-the-big-picture)
2. [Directory Structure](#directory-structure)
3. [The Master Document: main.tex](#the-master-document-maintex)
4. [Chapter Files](#chapter-files)
5. [Auxiliary Files](#auxiliary-files)
6. [The Final PDF: main.pdf](#the-final-pdf-mainpdf)
7. [How Compilation Works](#how-compilation-works)
8. [File Dependencies](#file-dependencies)
9. [What Goes Into main.pdf](#what-goes-into-mainpdf)

---

## Overview: The Big Picture

### The Compilation Pipeline

```
┌─────────────────────────────────────────────────────────────────────────┐
│                           SOURCE FILES                                   │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│   main.tex ─────────────┐                                               │
│       │                 │                                                │
│       ├── \input{chapters/ch01_scalar_product.tex}                      │
│       ├── \input{chapters/ch01_vector_product.tex}                      │
│       ├── \input{chapters/ch01_orbit_theory.tex}                        │
│       └── \input{chapters/ch01_diff_ops.tex}                            │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
                              ┌──────────┐
                              │ pdflatex │  (compiler)
                              └──────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                           OUTPUT FILES                                   │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│   main.pdf ◄──── Final output (what you read)                           │
│   main.aux ◄──── Cross-reference data                                   │
│   main.log ◄──── Compilation log (errors/warnings)                      │
│   main.toc ◄──── Table of contents data                                 │
│   main.out ◄──── PDF bookmark data                                      │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

### Analogy for Programmers

Think of it like compiling a C program:

| C/C++ | LaTeX | Purpose |
|-------|-------|---------|
| `main.c` | `main.tex` | Main source file |
| `header.h` | `chapters/*.tex` | Included files |
| `gcc` | `pdflatex` | Compiler |
| `a.out` / `main.exe` | `main.pdf` | Final output |
| `.o` files | `.aux`, `.toc` | Intermediate files |
| Compiler output | `main.log` | Build log |

---

## Directory Structure

```
output/
├── main.tex              # Master document (the "main.c")
├── main.pdf              # Compiled PDF (the "executable")
├── main.aux              # Auxiliary file (cross-references)
├── main.log              # Compilation log
├── main.toc              # Table of contents data
├── main.out              # PDF bookmarks/outline
└── chapters/             # Expanded proofs for Chapter 1 "gaps"
    ├── ch01_scalar_product.tex   # Fills gaps in §1.3-1.4
    ├── ch01_vector_product.tex   # Fills gaps in §1.5
    ├── ch01_orbit_theory.tex     # Fills gaps in §1.6
    └── ch01_diff_ops.tex         # Fills gaps in §1.7
```

**What are "gaps"?** Byron & Fuller's textbook contains statements like "the proof is left to the reader" or "it is easy to show that..." The chapter files in `output/chapters/` provide the complete, expanded proofs for these gaps.

**Note:** The source textbook PDFs should be placed in the `docs/` folder but are not included in this repository due to copyright.

---

## The Master Document: main.tex

### What It Is

`main.tex` is the **master document** that:
1. Defines the document type and settings
2. Loads required packages
3. Defines custom commands and environments
4. Includes all chapter files
5. Specifies the document structure

### File Structure Explained

```latex
%% ============================================================================
%% SECTION 1: DOCUMENT CLASS
%% ============================================================================

\documentclass[11pt,a4paper,twoside]{book}
```

**What this does:**
- `book` - Uses the book document class (chapters, front/back matter)
- `11pt` - Base font size is 11 points
- `a4paper` - A4 paper size (210mm × 297mm)
- `twoside` - Different margins for left/right pages (for printing)

```latex
%% ============================================================================
%% SECTION 2: PACKAGES
%% ============================================================================

\usepackage[utf8]{inputenc}     % Allow Unicode characters in source
\usepackage[T1]{fontenc}        % Better font encoding
\usepackage{lmodern}            % Modern fonts

% Mathematics
\usepackage{amsmath}            % Advanced math: align, equation*, etc.
\usepackage{amssymb}            % Math symbols: ℝ, ∀, ∃, etc.
\usepackage{amsthm}             % Theorem environments
\usepackage{mathtools}          % Extensions to amsmath
\usepackage{physics}            % Physics notation: ∇, bra-ket, etc.
\usepackage{cancel}             % Strike out terms in equations

% Layout
\usepackage[margin=1in]{geometry}  % Page margins
\usepackage{parskip}               % Paragraph spacing
\usepackage{enumitem}              % List customization

% Visual elements
\usepackage{tcolorbox}          % Colored boxes
\tcbuselibrary{theorems,skins,breakable}  % tcolorbox extensions

% References
\usepackage{hyperref}           % Clickable cross-references
\usepackage{cleveref}           % Smart references (\cref)
```

**What packages provide:**

| Package | Provides | Example |
|---------|----------|---------|
| `amsmath` | Advanced equations | `\begin{align}...\end{align}` |
| `amssymb` | Math symbols | `\mathbb{R}` → ℝ |
| `amsthm` | Theorem environments | `\begin{theorem}...\end{theorem}` |
| `physics` | Physics notation | `\grad`, `\div`, `\curl` |
| `tcolorbox` | Colored boxes | Intuition, warning boxes |
| `hyperref` | Clickable links | Cross-references, TOC links |

```latex
%% ============================================================================
%% SECTION 3: COLORS
%% ============================================================================

\definecolor{defcolor}{RGB}{0,100,150}      % Blue for definitions
\definecolor{thmcolor}{RGB}{150,50,0}       % Brown for theorems
\definecolor{intcolor}{RGB}{0,100,50}       % Green for intuition
\definecolor{warncolor}{RGB}{180,0,0}       % Red for warnings
\definecolor{keycolor}{RGB}{100,0,150}      % Purple for key steps
\definecolor{linkcolor}{RGB}{0,50,150}      % Blue for links
```

**Color usage:**
- Links in PDF are blue (`linkcolor`)
- Intuition boxes have green borders (`intcolor`)
- Warning boxes have red borders (`warncolor`)

```latex
%% ============================================================================
%% SECTION 4: THEOREM ENVIRONMENTS
%% ============================================================================

\theoremstyle{definition}
\newtheorem{definition}{Definition}[section]
\newtheorem{example}{Example}[section]
\newtheorem{notation}{Notation}[section]

\theoremstyle{plain}
\newtheorem{theorem}{Theorem}[section]
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{corollary}[theorem]{Corollary}
\newtheorem{proposition}[theorem]{Proposition}

\theoremstyle{remark}
\newtheorem{remark}{Remark}[section]
\newtheorem*{note}{Note}
```

**What this creates:**

| Environment | Style | Numbering | Example |
|-------------|-------|-----------|---------|
| `definition` | Upright text | Definition 1.3.1 | `\begin{definition}...\end{definition}` |
| `theorem` | Italic text | Theorem 1.3.1 | `\begin{theorem}...\end{theorem}` |
| `lemma` | Italic text | Lemma 1.3.2 (shares counter with theorem) | `\begin{lemma}...\end{lemma}` |
| `remark` | Upright text | Remark 1.3.1 | `\begin{remark}...\end{remark}` |

```latex
%% ============================================================================
%% SECTION 5: COLORED BOX ENVIRONMENTS
%% ============================================================================

\newtcolorbox{intuition}[1][]{
    enhanced, breakable,
    colback=intcolor!5, colframe=intcolor!70,
    fonttitle=\bfseries, title=Intuition, #1
}

\newtcolorbox{warning}[1][]{
    enhanced, breakable,
    colback=warncolor!5, colframe=warncolor!70,
    fonttitle=\bfseries, title=Warning, #1
}

\newtcolorbox{physical}[1][]{
    enhanced, breakable,
    colback=blue!5, colframe=blue!50,
    fonttitle=\bfseries, title=Physical Interpretation, #1
}

\newtcolorbox{keystep}[1][]{
    enhanced, breakable,
    colback=keycolor!5, colframe=keycolor!70,
    fonttitle=\bfseries, title=Key Step, #1
}
```

**Box settings explained:**
- `enhanced` - Enables advanced features
- `breakable` - Box can split across pages
- `colback=intcolor!5` - Background is 5% intensity of the color
- `colframe=intcolor!70` - Border is 70% intensity of the color
- `fonttitle=\bfseries` - Title is bold
- `title=Intuition` - Default title text

```latex
%% ============================================================================
%% SECTION 6: CUSTOM COMMANDS
%% ============================================================================

\renewcommand{\qedsymbol}{$\blacksquare$}   % QED symbol: ■
\newcommand{\vect}[1]{\mathbf{#1}}          % Vector: bold
\newcommand{\uvect}[1]{\hat{\mathbf{#1}}}   % Unit vector: bold with hat
\newcommand{\mat}[1]{\mathbf{#1}}           % Matrix: bold
\newcommand{\trans}{^{\mathsf{T}}}          % Transpose: ^T
\newcommand{\R}{\mathbb{R}}                 % Real numbers: ℝ

% Source reference commands
\newcommand{\sourceref}[1]{\marginpar{\footnotesize\textit{#1}}}
\newcommand{\sourceinline}[1]{{\footnotesize\textit{[Source: #1]}}}
\newcommand{\sourceeq}[1]{\textit{[#1]}}

\numberwithin{equation}{section}            % Equations numbered 1.1, 1.2, etc.
```

**Custom commands provide shortcuts:**

| Command | Input | Output | Purpose |
|---------|-------|--------|---------|
| `\vect{x}` | `\vect{x}` | **x** | Vector notation |
| `\uvect{n}` | `\uvect{n}` | **n̂** | Unit vector |
| `\R` | `\R` | ℝ | Real numbers |
| `\sourceref{p.~5}` | `\sourceref{B\&F p.~5}` | (margin note) | Source citation |

```latex
%% ============================================================================
%% SECTION 7: DOCUMENT BODY
%% ============================================================================

\begin{document}

% Title page
\begin{titlepage}
    \centering
    \vspace*{2cm}
    {\Huge\bfseries Vectors in Classical Physics\par}
    \vspace{1cm}
    {\Large A Research-Level Tutorial\par}
    ...
\end{titlepage}

% Front matter (roman numerals: i, ii, iii, ...)
\frontmatter
\tableofcontents

% Main content (arabic numerals: 1, 2, 3, ...)
\mainmatter

% Include chapter files
\input{chapters/ch01_scalar_product}
\input{chapters/ch01_vector_product}
\input{chapters/ch01_orbit_theory}
\input{chapters/ch01_diff_ops}

\end{document}
```

**Document structure:**
1. **Title page** - Project title, source attribution, date
2. **Front matter** - Table of contents (with Roman numeral pages)
3. **Main matter** - All chapter content (with Arabic numeral pages)

---

## Chapter Files

### What They Are

Each chapter file contains one section of the tutorial. They are **included** into `main.tex` using `\input{}`.

### Important: No Document Structure

Chapter files contain **only content**, not document structure:

```latex
%% ============================================================================
%% ch01_scalar_product.tex - CORRECT
%% ============================================================================

\section{The Scalar Product}
\label{sec:scalar-product}
\sourceref{B\&F \S1.3, pp.~5--8}

Content goes here...

\begin{theorem}[Schwarz Inequality]
...
\end{theorem}
```

**NOT like this:**

```latex
%% WRONG - Don't include these in chapter files!
\documentclass{book}           % WRONG!
\begin{document}               % WRONG!
...
\end{document}                 % WRONG!
```

### Chapter File Structure

Each chapter file follows this pattern:

```latex
%% ============================================================================
%% Header comment with section info and source reference
%% ============================================================================

\section{Section Title}
\label{sec:section-name}
\sourceref{B\&F \S1.X, pp.~YY--ZZ}

%% ----------------------------------------------------------------------------
\subsection{Overview and Motivation}
%% ----------------------------------------------------------------------------

[Why this topic matters, context, prerequisites]

%% ----------------------------------------------------------------------------
\subsection{Main Content Title}
%% ----------------------------------------------------------------------------

\sourceref{B\&F p.~YY}

\begin{definition}[Name]
[Precise mathematical definition]
\end{definition}

\begin{intuition}
[Why this makes sense]
\end{intuition}

\begin{theorem}[Name]
\sourceref{B\&F p.~ZZ}
[Formal statement]
\end{theorem}

\begin{proof}
[Complete step-by-step proof]
\end{proof}

%% ----------------------------------------------------------------------------
\subsection{Key Results Summary}
%% ----------------------------------------------------------------------------

\begin{itemize}
    \item Key result 1
    \item Key result 2
\end{itemize}
```

### Current Chapter Files

These files contain **expanded proofs** for the "gaps" in Byron & Fuller's Chapter 1:

| File | Gaps Filled | Topics Covered | Pages |
|------|-------------|----------------|-------|
| `ch01_scalar_product.tex` | §1.3-1.4 gaps | Scalar product axioms, Schwarz inequality proof | ~6 |
| `ch01_vector_product.tex` | §1.5 gaps | Cross product, BAC-CAB rule derivation | ~5 |
| `ch01_orbit_theory.tex` | §1.6 gaps | Kepler orbits, Laplace-Runge-Lenz vector | ~5 |
| `ch01_diff_ops.tex` | §1.7 gaps | curl(grad)=0, div(curl)=0 proofs | ~8 |

---

## Auxiliary Files

When you compile `main.tex`, pdflatex creates several auxiliary files. These are **intermediate files** needed for features like cross-references and table of contents.

### main.aux - Auxiliary File

**What it contains:**
- Label definitions (from `\label{}`)
- Reference data (for `\ref{}`)
- Citation data
- Counter values

**Example content:**
```
\relax
\@writefile{toc}{\contentsline {section}{\numberline {1.3}The Scalar Product}{1}{section.1.3}\protected@file@percent }
\newlabel{sec:scalar-product}{{1.3}{1}{The Scalar Product}{section.1.3}{}}
\newlabel{eq:inner-product-def}{{1.1}{1}{The Scalar Product}{equation.1.3.1}{}}
```

**Why it exists:**
- First pdflatex pass: Creates `.aux` with all labels
- Second pass: Reads `.aux` to resolve `\ref{}` commands

**Can you delete it?** Yes, but you'll need to compile twice again.

### main.log - Log File

**What it contains:**
- Complete compilation output
- All warnings and errors
- Package loading information
- Font information
- Page break decisions

**Example content:**
```
This is pdfTeX, Version 3.141592653-2.6-1.40.24 (MiKTeX 23.5)
...
LaTeX Warning: Reference `eq:missing' on page 5 undefined on input line 234.
...
Output written on main.pdf (29 pages, 571967 bytes).
```

**When to check it:**
- When compilation fails
- When you see "??" in the PDF
- When something looks wrong

**Useful commands:**
```bash
# Find errors
grep "^!" main.log

# Find warnings
grep "Warning" main.log

# Find undefined references
grep "undefined" main.log
```

### main.toc - Table of Contents

**What it contains:**
- Section titles and numbers
- Page numbers for each section
- Hierarchy information

**Example content:**
```
\contentsline {section}{\numberline {1.3}The Scalar Product}{1}{section.1.3}
\contentsline {subsection}{\numberline {1.3.1}Overview and Motivation}{1}{subsection.1.3.1}
\contentsline {section}{\numberline {1.4}Orthogonality}{4}{section.1.4}
```

**Why it exists:**
- First pass: Writes section info to `.toc`
- Second pass: `\tableofcontents` reads `.toc` to build TOC

### main.out - PDF Bookmarks

**What it contains:**
- Bookmark/outline data for PDF readers
- Section hierarchy for navigation panel

**Example content:**
```
\BOOKMARK [1][-]{section.1.3}{The Scalar Product}{}
\BOOKMARK [2][-]{subsection.1.3.1}{Overview and Motivation}{section.1.3}
```

**Where you see it:**
- PDF reader's "Bookmarks" or "Outline" panel
- Sidebar navigation in Adobe Reader, Preview, etc.

---

## The Final PDF: main.pdf

### What It Is

`main.pdf` is the **compiled output** - the actual document you read. It contains:

1. **Rendered text** - All content from `.tex` files
2. **Formatted mathematics** - Equations typeset beautifully
3. **Page layout** - Margins, headers, footers
4. **Embedded fonts** - Latin Modern fonts for consistent display
5. **Hyperlinks** - Clickable cross-references
6. **Bookmarks** - Navigation outline
7. **Metadata** - Title, author (if set)

### PDF Structure

```
main.pdf
├── Page 1: Title page
│   └── Title, subtitle, source attribution, date
├── Pages 2-3: Table of Contents
│   └── Clickable section list with page numbers
├── Pages 4-29: Main content
│   ├── Section 1.3: The Scalar Product
│   ├── Section 1.4: Orthogonality
│   ├── Section 1.5: The Vector Product
│   ├── Section 1.6: Classical Orbit Theory
│   └── Section 1.7: Differential Operations
└── PDF Metadata
    ├── Bookmarks/Outline
    └── Hyperlink destinations
```

### File Size Breakdown

Typical `main.pdf` size: ~550-600 KB

| Component | Approximate Size | Notes |
|-----------|------------------|-------|
| Embedded fonts | ~300 KB | Latin Modern family |
| Page content | ~150 KB | Text and equations |
| Vector graphics | ~50 KB | Boxes, lines, symbols |
| Metadata/structure | ~50 KB | Bookmarks, links, TOC |

---

## How Compilation Works

### Step-by-Step Process

```
┌─────────────────────────────────────────────────────────────────────────┐
│                         FIRST PDFLATEX PASS                              │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  1. Read main.tex                                                        │
│  2. Load packages                                                        │
│  3. Process \input{} commands (read chapter files)                      │
│  4. Typeset all content                                                  │
│  5. Write labels to main.aux                                            │
│  6. Write TOC data to main.toc                                          │
│  7. Generate PDF (but references show "??")                             │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                        SECOND PDFLATEX PASS                              │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  1. Read main.tex again                                                  │
│  2. Read main.aux (now has label data)                                  │
│  3. Read main.toc (now has TOC data)                                    │
│  4. Resolve \ref{} commands using aux data                              │
│  5. Build table of contents using toc data                              │
│  6. Generate PDF (references now show numbers)                          │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                    OPTIONAL THIRD PASS (if needed)                       │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  Sometimes page numbers change after references are resolved,           │
│  which changes the TOC, which might change page numbers again.          │
│  A third pass ensures everything is stable.                             │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

### Why Multiple Passes?

**Problem:** LaTeX processes the document linearly, top to bottom.

When it sees `\ref{eq:later}` on page 2, but `\label{eq:later}` is on page 10:
- First pass: Can't know the equation number yet → writes "??"
- During first pass: Reaches page 10, records label in `.aux`
- Second pass: Reads `.aux` first, now knows all labels → writes correct number

**Same for Table of Contents:**
- First pass: Doesn't know page numbers yet → TOC is empty or wrong
- During first pass: Records all sections with page numbers in `.toc`
- Second pass: Reads `.toc` → builds correct TOC

### Compilation Commands

**Basic compilation:**
```bash
cd output
pdflatex main.tex                    # First pass
pdflatex main.tex                    # Second pass
```

**With error handling:**
```bash
pdflatex -interaction=nonstopmode main.tex
```
- `nonstopmode`: Don't stop on errors, try to continue

**Full rebuild:**
```bash
# Delete auxiliary files
rm -f main.aux main.log main.toc main.out

# Compile from scratch
pdflatex main.tex && pdflatex main.tex && pdflatex main.tex
```

---

## File Dependencies

### Dependency Graph

```
                              main.tex
                                  │
                    ┌─────────────┼─────────────┐
                    │             │             │
                    ▼             ▼             ▼
              Package 1      Package 2      Package N
             (amsmath)      (tcolorbox)    (hyperref)
                                  │
                    ┌─────────────┼─────────────┬─────────────┐
                    │             │             │             │
                    ▼             ▼             ▼             ▼
              ch01_scalar   ch01_vector   ch01_orbit   ch01_diff
              _product.tex  _product.tex  _theory.tex  _ops.tex
                    │             │             │             │
                    └─────────────┴─────────────┴─────────────┘
                                          │
                                          ▼
                                      main.pdf
```

### What Depends on What

| File | Depends On | Used By |
|------|------------|---------|
| `main.tex` | All packages, LaTeX installation | pdflatex |
| `ch01_*.tex` | `main.tex` (for commands/environments) | `main.tex` via `\input{}` |
| `main.aux` | `main.tex`, chapter files | Second pdflatex pass |
| `main.toc` | `main.tex`, chapter files | `\tableofcontents` command |
| `main.pdf` | All source files, aux files | End user |

### If You Change...

| Changed File | What to Do |
|--------------|------------|
| Any `.tex` file | Run pdflatex twice |
| Add new `\label{}` | Run pdflatex twice |
| Add new section | Run pdflatex twice (for TOC) |
| Change page layout | Run pdflatex twice or three times |
| Nothing (just want fresh build) | Delete `.aux`, run pdflatex twice |

---

## What Goes Into main.pdf

### Complete Content Map

Here is exactly what appears in the final PDF, in order:

```
PAGE 1: TITLE PAGE
├── "Vectors in Classical Physics" (title)
├── "A Research-Level Tutorial" (subtitle)
├── "Based on" + "Mathematics of Classical and Quantum Physics"
├── "by F.W. Byron, Jr. and R.W. Fuller"
├── "Chapter 1: Expanded with Complete Proofs"
├── "Generated using physics-text-to-tutorial skill"
└── Date of compilation

PAGES 2-3: TABLE OF CONTENTS (auto-generated)
├── 1.3 The Scalar Product ..................... page X
│   ├── 1.3.1 Overview and Motivation
│   ├── 1.3.2 Axioms of the Scalar Product
│   └── ...
├── 1.4 Orthogonality .......................... page X
├── 1.5 The Vector Product ..................... page X
├── 1.6 A Vector Treatment of Classical Orbit Theory ... page X
└── 1.7 Differential Operations on Scalar and Vector Fields ... page X

PAGES 4-9: SECTION 1.3-1.4 (from ch01_scalar_product.tex)
├── Section header with margin source reference
├── Subsection: Overview and Motivation
├── Subsection: Axioms of the Scalar Product
│   ├── Definition 1.3.1 (Scalar Product)
│   ├── Intuition box (green)
│   └── Examples
├── Subsection: Properties
│   ├── Theorem 1.3.1 (properties)
│   └── Proof
├── Subsection: Schwarz Inequality
│   ├── Theorem 1.3.2 (Schwarz)
│   ├── Key Step box (purple)
│   └── Complete proof
├── Section 1.4: Orthogonality
│   ├── Definition of orthogonality
│   ├── Gram-Schmidt process
│   └── Physical interpretation box (blue)
└── Key Results Summary

PAGES 10-14: SECTION 1.5 (from ch01_vector_product.tex)
├── Section header with source reference
├── Definition of cross product
├── Geometric interpretation
│   └── Intuition box
├── Properties
│   ├── Anticommutativity
│   ├── Distributivity
│   └── Warning box (red) about order
├── BAC-CAB Rule
│   ├── Theorem statement
│   ├── Key Step box
│   └── Complete proof with index notation
├── Scalar Triple Product
│   ├── Definition
│   ├── Determinant formula
│   └── Cyclic property proof
└── Key Results Summary

PAGES 15-19: SECTION 1.6 (from ch01_orbit_theory.tex)
├── Section header with source reference
├── Overview: Why vector methods?
├── Conservation of Angular Momentum
│   ├── Theorem (Kepler's Second Law)
│   └── Complete proof
├── The Inverse-Square Force
│   ├── Equation of motion
│   └── Physical interpretation box
├── Expression for Angular Momentum
│   ├── Lemma
│   └── Proof
├── Key Derivative Calculation
│   ├── Lemma: d/dt(v × L) = k·ṅ
│   ├── Key Step box
│   └── Detailed proof using BAC-CAB
├── Laplace-Runge-Lenz Vector
│   ├── Definition
│   └── Physical meaning
├── Orbit Equation Derivation
│   ├── Step-by-step derivation
│   ├── Theorem: r = A/(1 + ε cos θ)
│   └── Eccentricity classification
├── Eccentricity-Energy Relation
│   ├── Formula derivation
│   └── Corollary: orbit type from energy
└── Key Results Summary

PAGES 20-29: SECTION 1.7 (from ch01_diff_ops.tex)
├── Section header with source reference
├── Overview: Differential operators on fields
├── The Gradient
│   ├── Definition
│   ├── Geometric meaning (steepest ascent)
│   ├── Intuition box
│   └── Coordinate expressions
├── The Divergence
│   ├── Definition
│   ├── Physical meaning (net outflow)
│   └── Coordinate expressions
├── The Curl
│   ├── Definition
│   ├── Physical meaning (local rotation)
│   ├── Determinant formula
│   └── Coordinate expressions
├── The Laplacian
│   ├── Definition
│   └── Connection to heat/wave equations
├── Key Identities
│   ├── Theorem: curl(grad φ) = 0
│   │   ├── Intuition box
│   │   └── Complete proof (antisymmetry)
│   ├── Theorem: div(curl V) = 0
│   │   ├── Intuition box
│   │   └── Complete proof (Levi-Civita)
│   └── Warning box about converse
├── Integral Theorems
│   ├── Gauss's Divergence Theorem
│   │   ├── Statement
│   │   └── Physical interpretation
│   └── Stokes' Theorem
│       ├── Statement
│       └── Physical interpretation
├── Application: Maxwell's Equations
│   ├── The four equations
│   └── Physical meaning of each
└── Key Results Summary

PDF METADATA (invisible but present)
├── Bookmarks/Outline (for sidebar navigation)
├── Hyperlink destinations (for clickable refs)
└── Document info (title, date)
```

### Content Statistics

| Metric | Value |
|--------|-------|
| Total pages | 29 |
| Sections | 5 (1.3, 1.4, 1.5, 1.6, 1.7) |
| Definitions | ~12 |
| Theorems | ~15 |
| Lemmas | ~8 |
| Proofs | ~20 |
| Intuition boxes | ~10 |
| Warning boxes | ~5 |
| Physical interpretation boxes | ~8 |
| Key Step boxes | ~6 |
| Numbered equations | ~80 |
| Cross-references | ~50 |
| Source references | ~40 |

---

## Summary

### Quick Reference

| File | Type | Purpose | Delete Safe? |
|------|------|---------|--------------|
| `main.tex` | Source | Master document | NO |
| `chapters/*.tex` | Source | Chapter content | NO |
| `main.pdf` | Output | Final document | Yes (regenerate) |
| `main.aux` | Auxiliary | Cross-references | Yes (recompile 2x) |
| `main.log` | Log | Debugging info | Yes |
| `main.toc` | Auxiliary | TOC data | Yes (recompile 2x) |
| `main.out` | Auxiliary | Bookmarks | Yes (recompile 2x) |

### Key Concepts

1. **main.tex** defines structure, loads packages, includes chapters
2. **Chapter files** contain only content, no document structure
3. **Auxiliary files** are intermediate files needed for cross-references
4. **Multiple compilation passes** are needed to resolve references
5. **main.pdf** is the final output containing rendered content, fonts, and links
