# AGENTS.md - Project Context for Codex

> **Repository update:** the complete solution-review process was run in **Codex App**, powered by **GPT-5.3-Codex** with **High reasoning**.
>
> Legacy content below describes an earlier tutorial-generation workflow and is retained for reference.

## Project Overview

This is **No Proof Left Behind** - a Codex Skill that transforms terse physics textbook content into comprehensive, research-level tutorials with complete proofs, detailed derivations, and professional LaTeX formatting.

**Key Points:**
- The `physics-text-to-tutorial` skill automates the gap-filling process
- Byron & Fuller's textbook is used as an **example** - the skill is **general-purpose**
- Works with any physics or mathematical physics textbook

## What This Project Does

1. **Reads** physics textbook PDFs from the `docs/` directory
2. **Identifies gaps** like "left to the reader" proofs, "clearly" statements, and skipped derivations
3. **Expands** the content with complete mathematical proofs and explanations (using the Codex Skill)
4. **Outputs** professional LaTeX documents compiled to PDF

## Project Structure

```
byron_fuller/
├── AGENTS.md              # This file - Codex context
├── README.md              # Project overview and setup
├── .gitignore             # Git ignore patterns
├── .Codex/
│   └── skills/
│       └── physics-text-to-tutorial/
│           ├── SKILL.md           # Main skill workflow documentation
│           ├── latex-template.tex # LaTeX document template
│           └── physics-macros.tex # Mathematical notation macros
├── docs/
│   ├── (source PDFs)      # Byron & Fuller PDFs go here (not included - copyright)
│   ├── USER_GUIDE.md      # Detailed user documentation
│   ├── DEVELOPER_GUIDE.md # Developer documentation
│   ├── QUICK_START.md     # Quick start with use cases
│   ├── TROUBLESHOOTING.md # Common issues and solutions
│   ├── LATEX_REFERENCE.md # LaTeX guide for beginners
│   └── OUTPUT_FILES_EXPLAINED.md # What each output file does
├── output/
│   ├── main.tex           # Master LaTeX document
│   ├── main.pdf           # Compiled PDF with expanded proofs
│   └── chapters/          # Expanded proofs filling Chapter 1 "gaps"
│       ├── ch01_scalar_product.tex  # Proofs for gaps in §1.3-1.4
│       ├── ch01_vector_product.tex  # Proofs for gaps in §1.5
│       ├── ch01_orbit_theory.tex    # Proofs for gaps in §1.6
│       └── ch01_diff_ops.tex        # Proofs for gaps in §1.7
└── venv/                  # Python virtual environment (optional)
```

## Key Commands

### Compile LaTeX to PDF (Windows with MiKTeX)
```bash
cd output
pdflatex -interaction=nonstopmode main.tex
pdflatex -interaction=nonstopmode main.tex  # Run twice for cross-references
```

### Typical MiKTeX Path on Windows
```
C:\Users\<username>\AppData\Local\Programs\MiKTeX\miktex\bin\x64\pdflatex.exe
```

## Skill Usage

The `physics-text-to-tutorial` skill is invoked when:
- Converting physics/math textbook PDFs to expanded tutorials
- User asks to "explain", "expand", or "fill in" textbook content
- Creating tutorial materials from academic sources
- Filling in "left to the reader" proofs

## LaTeX Document Structure

The tutorial uses a `book` class with:
- **amsmath, amsthm**: Mathematical typesetting
- **physics**: Physics notation (\grad, \div, \curl, etc.)
- **tcolorbox**: Colored boxes for intuition, warnings, key steps
- **hyperref**: Cross-references and PDF bookmarks

### Custom Environments
- `\begin{definition}...\end{definition}` - Mathematical definitions
- `\begin{theorem}...\end{theorem}` - Formal theorem statements
- `\begin{proof}...\end{proof}` - Complete proofs
- `\begin{intuition}...\end{intuition}` - Physical/mathematical intuition (green box)
- `\begin{warning}...\end{warning}` - Common mistakes (red box)
- `\begin{physical}...\end{physical}` - Physical interpretation (blue box)
- `\begin{keystep}...\end{keystep}` - Critical derivation steps (purple box)

### Source Reference Commands
- `\sourceref{B\&F Ch.~1, p.~5}` - Margin note citing original source
- `\sourceinline{Ch.~1, p.~5}` - Inline source citation
- `\sourceeq{Eq.~(1.34)}` - Reference to original equation number

## Content Expansion Patterns

### Pattern 1: "Left to the reader"
**Original**: "We leave the proof to the reader."
**Expansion**: Complete step-by-step proof with justifications

### Pattern 2: "Clearly" / "It is easy to show"
**Original**: "It is easy to show that div(curl V) = 0."
**Expansion**: Full computation with explicit index manipulation

### Pattern 3: "Using Eq. (X), we obtain"
**Original**: "Using Eq. (1.34), we obtain..."
**Expansion**: Restate the equation, show substitution, all intermediate steps

### Pattern 4: Equation jumps
**Original**: Going from step A directly to step Z
**Expansion**: Fill in all intermediate algebraic steps

## Quality Checklist

Before completing any section:
- [ ] All "left to reader" proofs filled in completely
- [ ] All "clearly" and "obviously" statements justified
- [ ] No equation jumps > 2 algebraic steps
- [ ] Notation consistent with Byron & Fuller
- [ ] Source references cite original page numbers
- [ ] Section numbering matches original book
- [ ] LaTeX compiles without errors
- [ ] PDF renders equations correctly

## Common Tasks

### Add a New Chapter Section
1. Read the relevant PDF pages in `docs/`
2. Create a new `.tex` file in `output/chapters/`
3. Add `\input{chapters/ch0X_name}` to `main.tex`
4. Compile PDF (run pdflatex twice)

### Fix Undefined References
Run pdflatex multiple times until warnings disappear:
```bash
pdflatex main.tex && pdflatex main.tex && pdflatex main.tex
```

### Add New Macros
Edit `.Codex/skills/physics-text-to-tutorial/physics-macros.tex`

## Current Progress

**Completed:**
- Chapter 1, Section 1.3-1.4: Scalar Product
- Chapter 1, Section 1.5: Vector Product
- Chapter 1, Section 1.6: Classical Orbit Theory
- Chapter 1, Section 1.7: Differential Operations

**Remaining:**
- Chapter 1, Section 1.8+: Additional sections
- Chapters 2-12: Complete textbook

## Dependencies

- **LaTeX Distribution**: MiKTeX (Windows), TeX Live (Linux/Mac)
- **Required Packages**: amsmath, amsthm, physics, tcolorbox, hyperref, cleveref
- **PDF Reader**: Any PDF viewer

## Notes for Codex

1. **Always read** the source PDF section before writing tutorial content
2. **Use \sourceref{}** to cite original Byron & Fuller page numbers
3. **Match section numbering** with the original textbook
4. **Expand completely** - no "clearly" or "left to reader" in output
5. **Compile twice** for cross-references to resolve
6. **Check quality** against the checklist above before marking complete
