# Developer Guide

A comprehensive guide for developers who want to extend, modify, or maintain this project. This guide assumes you have traditional programming experience (C, C++, Java) but may be new to LaTeX and document generation.

## Table of Contents

1. [Architecture Overview](#architecture-overview)
2. [Technology Stack](#technology-stack)
3. [Development Environment Setup](#development-environment-setup)
4. [Project Structure Deep Dive](#project-structure-deep-dive)
5. [Understanding LaTeX](#understanding-latex)
6. [The Skill System](#the-skill-system)
7. [Adding New Content](#adding-new-content)
8. [Modifying Existing Content](#modifying-existing-content)
9. [Testing Your Changes](#testing-your-changes)
10. [Common Patterns](#common-patterns)
11. [Best Practices](#best-practices)
12. [Extending for Other Textbooks](#extending-for-other-textbooks)

---

## Architecture Overview

### High-Level Flow

```
┌─────────────┐     ┌──────────────┐     ┌────────────┐     ┌─────────────┐
│ Source PDFs │────▶│ Claude Code  │────▶│ LaTeX Files│────▶│ Output PDF  │
│  (docs/)    │     │  + Skills    │     │ (output/)  │     │ (main.pdf)  │
└─────────────┘     └──────────────┘     └────────────┘     └─────────────┘
```

### Component Responsibilities

| Component | Purpose | Location |
|-----------|---------|----------|
| Source PDFs | Original textbook pages | `docs/*.pdf` |
| Skills | Workflow and patterns for expansion | `.claude/skills/` |
| LaTeX Template | Document structure and formatting | `.claude/skills/*/latex-template.tex` |
| Physics Macros | Mathematical notation shortcuts | `.claude/skills/*/physics-macros.tex` |
| Chapter Files | Expanded tutorial content | `output/chapters/*.tex` |
| Main Document | Master file that combines chapters | `output/main.tex` |
| Output PDF | Final compiled tutorial | `output/main.pdf` |

### Data Flow

1. **Input**: Claude Code reads source PDFs from `docs/`
2. **Processing**: Using the skill's patterns, identifies gaps and expands content
3. **Generation**: Creates LaTeX files in `output/chapters/`
4. **Compilation**: pdflatex converts LaTeX to PDF
5. **Output**: Final `main.pdf` in `output/`

---

## Technology Stack

### Core Technologies

| Technology | Version | Purpose | Documentation |
|------------|---------|---------|---------------|
| LaTeX | Any | Document typesetting | https://www.latex-project.org/ |
| pdflatex | (with MiKTeX/TeX Live) | Compile LaTeX to PDF | https://miktex.org/kb/pdflatex |
| Claude Code | Latest | AI-assisted expansion | https://claude.ai/ |

### LaTeX Packages Used

| Package | Purpose | Example Usage |
|---------|---------|---------------|
| `amsmath` | Advanced math formatting | `\begin{align}...\end{align}` |
| `amsthm` | Theorem environments | `\begin{theorem}...\end{theorem}` |
| `physics` | Physics notation | `\grad`, `\div`, `\curl` |
| `tcolorbox` | Colored content boxes | `\begin{intuition}...\end{intuition}` |
| `hyperref` | Clickable cross-references | `\ref{eq:example}` |
| `cleveref` | Smart references | `\cref{thm:main}` |

### Why LaTeX?

If you're coming from C/C++/Java, think of LaTeX as:
- **Source code** (`.tex` files) that **compiles** (via `pdflatex`) into **executables** (`.pdf` files)
- Like code, LaTeX has **syntax**, **macros** (like functions), and **packages** (like libraries)
- Errors during compilation are shown with line numbers, just like compiler errors

---

## Development Environment Setup

### Step 1: Install Required Software

#### LaTeX Distribution

**Windows (MiKTeX):**
```powershell
# Using winget (Windows Package Manager)
winget install MiKTeX.MiKTeX

# Or download from https://miktex.org/download
```

**macOS:**
```bash
brew install --cask mactex
```

**Linux:**
```bash
# Ubuntu/Debian
sudo apt-get install texlive-full

# Fedora
sudo dnf install texlive-scheme-full
```

#### Text Editor (Recommended: VS Code)

1. Download VS Code: https://code.visualstudio.com/
2. Install the "LaTeX Workshop" extension:
   - Open VS Code
   - Press Ctrl+Shift+X (Cmd+Shift+X on Mac)
   - Search "LaTeX Workshop"
   - Click Install

3. Configure LaTeX Workshop (optional):
   - Open Settings (Ctrl+,)
   - Search "latex-workshop.latex.tools"
   - The default settings usually work

#### Claude Code

Follow the installation instructions at https://claude.ai/ for Claude Code CLI.

### Step 2: Clone/Download the Project

```bash
# If using Git
git clone <repository-url> byron_fuller
cd byron_fuller

# Or just extract the downloaded ZIP file
```

### Step 3: Verify Setup

```bash
# Test LaTeX installation
pdflatex --version

# Test compilation
cd output
pdflatex main.tex
```

If you see "Output written on main.pdf", you're ready!

### Step 4: Open in Editor

```bash
# Open in VS Code
code .
```

---

## Project Structure Deep Dive

### Root Directory

```
byron_fuller/
├── CLAUDE.md              # Context file for Claude Code
├── README.md              # Project overview
├── .gitignore             # Git exclusions
├── .claude/               # Claude Code configuration
├── docs/                  # Source materials and documentation
├── output/                # Generated LaTeX and PDF
└── venv/                  # Python virtual environment (optional)
```

### The `.claude/` Directory

```
.claude/
└── skills/
    └── physics-text-to-tutorial/
        ├── SKILL.md           # Main skill definition
        ├── latex-template.tex # Document template
        └── physics-macros.tex # Math notation macros
```

**SKILL.md** defines:
- When the skill should be invoked
- The step-by-step workflow
- Patterns for expanding different types of content
- Quality checklist

**latex-template.tex** provides:
- Document class settings
- Package imports
- Custom environment definitions
- Header/footer configuration

**physics-macros.tex** provides:
- Vector notation: `\vect{x}`, `\uvect{n}`
- Operators: `\grad`, `\div`, `\curl`
- Quantum mechanics: `\bra`, `\ket`, `\braket`
- Common symbols and shortcuts

### The `docs/` Directory

```
docs/
├── (source PDFs)          # Your Byron & Fuller PDFs (not included - copyright)
├── chunk.py               # PDF splitting utility
├── USER_GUIDE.md          # User documentation
├── DEVELOPER_GUIDE.md     # This file
├── QUICK_START.md         # Quick start guide
├── TROUBLESHOOTING.md     # Problem solving
├── LATEX_REFERENCE.md     # LaTeX basics
└── OUTPUT_FILES_EXPLAINED.md  # What output files do
```

**Note:** The source textbook PDFs are not included in this repository due to copyright. You must provide your own copy of "Mathematics of Classical and Quantum Physics" by Byron & Fuller and place the PDFs in this folder.

### The `output/` Directory

```
output/
├── main.tex               # Master document
├── main.pdf               # Compiled PDF with expanded proofs
├── main.aux               # Auxiliary file (cross-references)
├── main.log               # Compilation log
├── main.out               # Hyperref bookmarks
├── main.toc               # Table of contents data
└── chapters/              # Expanded proofs for Chapter 1 "gaps"
    ├── ch01_scalar_product.tex   # Proofs for gaps in §1.3-1.4
    ├── ch01_vector_product.tex   # Proofs for gaps in §1.5
    ├── ch01_orbit_theory.tex     # Proofs for gaps in §1.6
    └── ch01_diff_ops.tex         # Proofs for gaps in §1.7
```

**What are "gaps"?** These are places in Byron & Fuller's textbook where proofs are left to the reader, derivations are skipped, or steps are marked as "clearly" or "easy to show." The chapter files provide the complete, expanded proofs for these gaps.

---

## Understanding LaTeX

### LaTeX vs. Traditional Programming

| Concept | C/C++/Java | LaTeX |
|---------|------------|-------|
| Source file | `.c`, `.java` | `.tex` |
| Compiler | gcc, javac | pdflatex |
| Output | executable, .class | .pdf |
| Libraries | `#include`, `import` | `\usepackage{}` |
| Functions | `void foo()` | `\newcommand{\foo}{}` |
| Comments | `// comment` | `% comment` |
| Main entry | `main()` | `\begin{document}` |

### Basic LaTeX Syntax

```latex
% This is a comment

\documentclass{book}       % Define document type (like #include <stdio.h>)

\usepackage{amsmath}       % Import package (like #include or import)

\newcommand{\mycommand}{text}  % Define macro (like #define or function)

\begin{document}           % Start of content (like main())

\section{Title}            % Section heading
Regular text goes here.

\begin{equation}           % Start math environment
    E = mc^2
\end{equation}             % End math environment

\end{document}             % End of content
```

### Common LaTeX Commands

| Command | Purpose | Example |
|---------|---------|---------|
| `\section{Title}` | Create section | `\section{Introduction}` |
| `\subsection{Title}` | Create subsection | `\subsection{Background}` |
| `\textbf{text}` | Bold text | `\textbf{important}` |
| `\textit{text}` | Italic text | `\textit{emphasis}` |
| `\begin{env}...\end{env}` | Environment | `\begin{proof}...\end{proof}` |
| `\label{name}` | Create reference point | `\label{eq:einstein}` |
| `\ref{name}` | Reference a label | `See Eq.~\ref{eq:einstein}` |
| `$$...$$` or `\[...\]` | Display math | `\[ E = mc^2 \]` |
| `$...$` | Inline math | `Energy is $E = mc^2$` |

### Math Mode Essentials

```latex
% Inline math (within text)
The equation $E = mc^2$ shows...

% Display math (centered, numbered)
\begin{equation}
    E = mc^2
    \label{eq:energy}
\end{equation}

% Display math (not numbered)
\[
    F = ma
\]

% Aligned equations
\begin{align}
    a &= b + c \\
    d &= e + f
\end{align}

% Common math symbols
\alpha, \beta, \gamma          % Greek letters
\sum_{i=1}^{n}                 % Summation
\int_{0}^{\infty}              % Integral
\frac{a}{b}                    % Fraction
\sqrt{x}                       % Square root
\partial                       % Partial derivative symbol
\nabla                         % Gradient/del operator
```

---

## The Skill System

### What Is a Skill?

A skill is a set of instructions that tells Claude Code how to perform a specific task. Think of it like a detailed recipe or procedure document.

### Skill Structure

```markdown
---
name: physics-text-to-tutorial
description: When to invoke this skill
---

# Skill Title

## When to Use

Conditions for invoking this skill...

## Workflow

Step-by-step process...

## Patterns

Templates for common transformations...

## Quality Checklist

Verification steps...
```

### How Skills Are Invoked

Skills are automatically invoked when Claude Code detects matching conditions:
- User asks to "expand" or "explain" textbook content
- User provides a PDF of physics/math content
- User requests tutorial generation

### Modifying the Skill

To change the workflow or add new patterns:

1. Open `.claude/skills/physics-text-to-tutorial/SKILL.md`
2. Edit the relevant section
3. Save the file

Changes take effect immediately on the next Claude Code interaction.

---

## Adding New Content

### Step-by-Step: Adding a New Section

Let's add Section 1.8 as an example.

#### Step 1: Read the Source Material

First, understand what "gaps" you're filling:
```bash
# Open your Byron & Fuller PDF from the docs/ folder
# Identify the "left to reader" proofs or skipped derivations
# Note the page numbers for source references
```

**Note:** Source PDFs are not included due to copyright. You must provide your own copy.

#### Step 2: Create the Chapter File

Create a new file `output/chapters/ch01_section_name.tex`:

```latex
%% ============================================================================
%% Section 1.8: [Section Title]
%% Source: Byron & Fuller, Chapter 1, Section 1.8, pp. XX--YY
%% ============================================================================

\section{[Section Title]}
\label{sec:section-name}
\sourceref{B\&F \S1.8, pp.~XX--YY}

%% ----------------------------------------------------------------------------
\subsection{Overview and Motivation}
%% ----------------------------------------------------------------------------

[Why this section matters...]

%% ----------------------------------------------------------------------------
\subsection{Prerequisites}
%% ----------------------------------------------------------------------------

Before proceeding, ensure familiarity with:
\begin{itemize}
    \item Previous concept (Section~\ref{sec:previous})
    \item Another concept
\end{itemize}

%% ----------------------------------------------------------------------------
\subsection{Main Content}
%% ----------------------------------------------------------------------------

\sourceref{B\&F p.~XX}

\begin{definition}[Definition Name]
[Precise mathematical definition...]
\end{definition}

\begin{intuition}
[Why this makes sense...]
\end{intuition}

\begin{theorem}[Theorem Name]
\sourceref{B\&F p.~YY}
[Theorem statement...]
\end{theorem}

\begin{proof}
[Complete step-by-step proof...]
\end{proof}

%% ----------------------------------------------------------------------------
\subsection{Key Results Summary}
%% ----------------------------------------------------------------------------

\begin{itemize}
    \item First key result
    \item Second key result
\end{itemize}
```

#### Step 3: Add to Main Document

Edit `output/main.tex`:

```latex
\input{chapters/ch01_scalar_product}
\input{chapters/ch01_vector_product}
\input{chapters/ch01_orbit_theory}
\input{chapters/ch01_diff_ops}
\input{chapters/ch01_section_name}    % <-- Add this line

\end{document}
```

#### Step 4: Compile and Test

```bash
cd output
pdflatex -interaction=nonstopmode main.tex
pdflatex -interaction=nonstopmode main.tex  # Run twice!
```

#### Step 5: Verify

1. Open `main.pdf`
2. Check the Table of Contents - new section should appear
3. Navigate to the new section
4. Verify all equations render correctly
5. Check cross-references work

### Adding a New Chapter

For a completely new chapter (e.g., Chapter 2):

1. Create files for each section in `output/chapters/`:
   - `ch02_section1.tex`
   - `ch02_section2.tex`
   - etc.

2. Add to `main.tex`:
   ```latex
   \chapter{Chapter 2 Title}
   \input{chapters/ch02_section1}
   \input{chapters/ch02_section2}
   ```

3. Compile and test.

---

## Modifying Existing Content

### Fixing a Typo

1. Open the relevant `.tex` file
2. Find the error (use Ctrl+F)
3. Fix it
4. Save
5. Recompile

### Adding an Equation

```latex
% Before
The energy is given by the famous equation.

% After
The energy is given by the famous equation:
\begin{equation}
    E = mc^2
    \label{eq:mass-energy}
\end{equation}
```

### Adding a New Theorem

```latex
\begin{theorem}[Descriptive Name]
\sourceref{B\&F p.~XX}
For all vectors $\vect{x}$ and $\vect{y}$ in $\R^n$,
\begin{equation}
    |\vect{x} \cdot \vect{y}| \leq |\vect{x}| |\vect{y}|.
\end{equation}
\end{theorem}

\begin{proof}
We prove this by considering...

\textbf{Step 1.} First, we note that...

\textbf{Step 2.} Next, we apply...

Therefore, the inequality holds.
\end{proof}
```

### Adding a Warning Box

```latex
\begin{warning}
A common mistake is to assume that $\vect{A} \times \vect{B} = \vect{B} \times \vect{A}$.
In fact, the cross product is \emph{anticommutative}:
$\vect{A} \times \vect{B} = -\vect{B} \times \vect{A}$.
\end{warning}
```

### Adding Source References

Always cite where content came from:

```latex
\begin{theorem}[Stokes' Theorem]
\sourceref{B\&F p.~28, Eq.~(1.89)}
\[
    \oint_C \vect{A} \cdot d\vect{l} = \iint_S (\nabla \times \vect{A}) \cdot d\vect{S}
\]
\end{theorem}

\begin{proof}
\sourceref{Marked ``left to reader'' at B\&F p.~28}
We prove this by...
\end{proof}
```

---

## Testing Your Changes

### Compilation Test

```bash
cd output
pdflatex -interaction=nonstopmode main.tex 2>&1 | grep -E "(Error|Warning|!)"
```

**Good output**: Only minor warnings about page breaks or references
**Bad output**: Lines starting with `!` indicate errors

### Visual Inspection

After compiling:
1. Open the PDF
2. Check the specific section you modified
3. Verify:
   - Equations render correctly (no broken symbols)
   - Cross-references show numbers (not "??")
   - Boxes display properly
   - No text overflow in margins

### Cross-Reference Test

If you added new labels or references:
```bash
# Compile three times to fully resolve references
pdflatex main.tex && pdflatex main.tex && pdflatex main.tex

# Check for undefined references
grep "undefined" main.log
```

### Common Errors and Fixes

| Error | Cause | Fix |
|-------|-------|-----|
| `Undefined control sequence` | Unknown command | Check spelling or add required package |
| `Missing $ inserted` | Math mode issue | Check for unclosed `$` or `\[` |
| `Missing \begin{document}` | Preamble error | Check for errors before `\begin{document}` |
| `Reference undefined` | Missing label | Run pdflatex again or check label name |
| `Overfull \hbox` | Line too long | Usually cosmetic, can ignore |

---

## Common Patterns

### Pattern 1: Expanding "Left to the Reader" Proofs

**Original text says**: "The proof is left to the reader."

**Expansion template**:
```latex
\begin{proof}
We prove this result in three steps.

\textbf{Step 1: Setup.}
Let $\vect{x}$ and $\vect{y}$ be arbitrary vectors in $\R^n$. We wish to show that...

\textbf{Step 2: Key Calculation.}
\begin{align}
    \text{LHS} &= \text{first step} \\
               &= \text{second step} \quad \text{(by previous result)} \\
               &= \text{third step}
\end{align}

\textbf{Step 3: Conclusion.}
Since all steps are reversible, the equality holds. Therefore...
\end{proof}
```

### Pattern 2: Expanding "Clearly" Statements

**Original**: "Clearly, $\nabla \cdot (\nabla \times \vect{A}) = 0$."

**Expansion**:
```latex
\begin{proposition}
For any sufficiently smooth vector field $\vect{A}$,
\[
    \nabla \cdot (\nabla \times \vect{A}) = 0.
\]
\end{proposition}

\begin{intuition}
The curl measures local rotation, producing a field with no sources or sinks.
Hence its divergence (which measures net outflow) must vanish.
\end{intuition}

\begin{proof}
We compute explicitly in Cartesian coordinates. Let $\vect{A} = A_x \uvect{x} + A_y \uvect{y} + A_z \uvect{z}$.

The curl is:
\[
    \nabla \times \vect{A} = \begin{vmatrix}
        \uvect{x} & \uvect{y} & \uvect{z} \\
        \partial_x & \partial_y & \partial_z \\
        A_x & A_y & A_z
    \end{vmatrix}
\]

[Continue with full computation...]
\end{proof}
```

### Pattern 3: Filling Equation Gaps

**Original**: "From (1.23), we immediately obtain (1.24)."

**Expansion**:
```latex
Starting from Equation~\eqref{eq:1.23}:
\begin{equation}
    \text{[Equation 1.23 here]}
    \label{eq:1.23}
\end{equation}

We proceed step by step:
\begin{align}
    \text{LHS} &= \text{Eq.~(1.23)} \\
    &= \text{Algebraic manipulation 1} \\
    &= \text{Algebraic manipulation 2} \quad \text{(using identity X)} \\
    &= \text{Algebraic manipulation 3} \\
    &= \text{[Equation 1.24 here]}
    \label{eq:1.24}
\end{align}

This completes the derivation of Equation~\eqref{eq:1.24}.
```

---

## Best Practices

### Code Quality

1. **Consistent formatting**: Use consistent indentation (4 spaces recommended)
2. **Comments**: Add `%` comments explaining complex sections
3. **Section markers**: Use `%% ===...===` to separate major sections
4. **Meaningful labels**: Use descriptive labels like `eq:schwarz-inequality`

### Content Quality

1. **Source references**: Always cite original page numbers
2. **Complete proofs**: Never write "clearly" or "left to reader" in output
3. **Step-by-step**: Show every algebraic step, or at most skip 2 trivial steps
4. **Physical insight**: Add intuition boxes for geometric/physical meaning

### File Organization

1. **One section per file**: Keep chapter files focused
2. **Consistent naming**: Use pattern `chNN_topic_name.tex`
3. **Logical order**: List chapters in `main.tex` in reading order

### Version Control (Git)

```bash
# Before making changes
git status
git pull

# After making changes
git add output/chapters/ch01_new_section.tex
git add output/main.tex
git commit -m "Add Section 1.8: Topic Name"
git push
```

---

## Extending for Other Textbooks

### Step 1: Create a New Skill

Copy the existing skill directory:
```bash
cp -r .claude/skills/physics-text-to-tutorial .claude/skills/new-textbook-skill
```

### Step 2: Modify the Skill

Edit `.claude/skills/new-textbook-skill/SKILL.md`:
- Update the name and description
- Modify patterns for the new textbook's style
- Update source reference format

### Step 3: Prepare Source Materials

1. Scan or obtain PDF of the textbook
2. Split into manageable chunks (50-100 pages each)
3. Place in `docs/` folder

### Step 4: Create Output Structure

```bash
mkdir -p output/chapters
# Create main.tex based on existing template
```

### Step 5: Begin Expansion

Use Claude Code with the new skill to expand content.

---

## Appendix: Quick Reference

### Essential Commands

```bash
# Compile PDF
cd output && pdflatex main.tex && pdflatex main.tex

# Check for errors
grep "^!" output/main.log

# Check undefined references
grep "undefined" output/main.log

# Clean auxiliary files
rm output/*.aux output/*.log output/*.out output/*.toc
```

### Essential LaTeX

```latex
% Math environments
\begin{equation} ... \end{equation}    % Numbered equation
\begin{align} ... \end{align}          % Aligned equations
\[ ... \]                              % Unnumbered display

% Theorem environments
\begin{definition} ... \end{definition}
\begin{theorem} ... \end{theorem}
\begin{proof} ... \end{proof}
\begin{lemma} ... \end{lemma}

% Custom boxes
\begin{intuition} ... \end{intuition}  % Green
\begin{warning} ... \end{warning}      % Red
\begin{physical} ... \end{physical}    % Blue
\begin{keystep} ... \end{keystep}      % Purple

% Cross-references
\label{eq:name}    % Create label
\ref{eq:name}      % Reference label
\eqref{eq:name}    % Reference with parentheses

% Source citations
\sourceref{B\&F p.~XX}
```

### Useful Resources

- LaTeX Wikibook: https://en.wikibooks.org/wiki/LaTeX
- TeX Stack Exchange: https://tex.stackexchange.com/
- Detexify (draw a symbol to find the command): https://detexify.kirelabs.org/
- MiKTeX Documentation: https://miktex.org/kb
