# End-to-End Workflow: Generating 263 Solution PDFs

## Project Overview

**Goal:** Solve every end-of-chapter problem from all 10 chapters of *Mathematics of Classical and Quantum Physics* by Frederick W. Byron Jr. and Robert W. Fuller, producing one standalone LaTeX-compiled PDF per problem.

**Final Output:** 263 PDF files organized in `ch01/` through `ch10/`, named `ch{CC}_{PP}.pdf`.

**Source Material:** The textbook, with page images extracted for multimodal reading.

---

## Phase 0: Environment Setup

### 0.1 Source Material Inventory

The book's pages were available as individual PNG images:
```
/path/to/pages/page_0001.png  (front matter)
...
/path/to/pages/page_0669.png  (back matter)
```

### 0.2 Page Offset Discovery

The book's printed page numbers do not match the file numbering. By reading the table of contents and comparing with page images:

- **Offset = +10**: Book page N corresponds to `page_{N+10:04d}.png`
- Example: Book page 39 (Ch1 problems) → `page_0049.png`

### 0.3 Chapter Boundaries (from Table of Contents)

| Chapter | Title | Book Pages | Image File Range |
|---------|-------|------------|------------------|
| 1 | Vectors in Classical Physics | 1–42 | 11–52 |
| 2 | Calculus of Variations | 43–84 | 53–94 |
| 3 | Vectors and Matrices | 85–141 | 95–151 |
| 4 | Vector Spaces in Physics | 142–211 | 152–221 |
| 5 | Hilbert Space | 212–304 | 222–314 |
| 6 | Complex Variable Theory | 305–387 | 315–397 |
| 7 | Green's Functions | 388–468 | 398–478 |
| 8 | Introduction to Integral Equations | 469–509 | 479–519 |
| 9 | Integral Equations in Hilbert Space | 510–579 | 520–589 |
| 10 | Introduction to Group Theory | 556–649 | 566–659 |

### 0.4 LaTeX Compiler Installation

**Problem:** No LaTeX distribution was installed. `pdflatex`, `xelatex`, and MiKTeX were all absent.

**Solution:** Installed [Tectonic](https://tectonic-typesetting.github.io/) via Scoop:
```bash
scoop install tectonic
```
Tectonic (v0.15.0) is a self-contained LaTeX engine that automatically downloads packages on first use. No manual package management needed.

**Compilation command (used throughout):**
```bash
tectonic filename.tex
```
Tectonic produces `filename.pdf` in the same directory and skips intermediate files by default.

---

## Phase 1: Reading the Textbook (OCR via Multimodal Vision)

### 1.1 Method

Claude Code's `Read` tool can open PNG image files and interpret their contents visually (multimodal LLM capability). This was used to:

1. **Read the table of contents** to determine chapter boundaries
2. **Read end-of-chapter problem pages** to transcribe problem statements
3. **Read chapter body pages** to understand notation, theorems, and equations referenced by problems

### 1.2 Reading Strategy

For each chapter, the workflow was:

1. **Locate the PROBLEMS section.** Problems are always at the end of each chapter, typically spanning 2–8 pages before the next chapter begins. The word "PROBLEMS" appears as a section header.

2. **Read problem pages sequentially.** Each page image was read using Claude Code's multimodal `Read` tool. The model extracts mathematical notation, equation numbers, and problem text from the scanned images.

3. **Read key chapter sections for context.** Many problems reference specific equations (e.g., "use Eq. (9.34)"), theorems (e.g., "Theorem 9.4"), or examples. These were read as needed to understand what the problem is asking and what tools/results are available.

### 1.3 Challenges

- **Scan quality:** Some symbols are ambiguous (e.g., distinguishing `ε` from `e`, or `ℓ` from `l`).
- **Mathematical notation density:** Pages contain dense equations with subscripts, superscripts, integrals, matrices, and special functions. The multimodal model handles this well but occasionally misreads a symbol.
- **Cross-references:** Problems frequently reference equations, theorems, and examples from earlier in the chapter or from previous chapters. Solving a problem often required reading 5–10 additional pages of chapter content.

---

## Phase 2: Chapter 1 — Manual Solving (Establishing the Template)

Chapter 1 was solved entirely by hand (by the main Claude Code agent) to establish the LaTeX template, workflow, and quality standard.

### 2.1 LaTeX Template

Every solution file follows this structure:

```latex
\documentclass[12pt]{article}
\usepackage{amsmath,amssymb,amsfonts,amsthm}
\usepackage[margin=1in]{geometry}
\usepackage{bm}  % (optional, for bold math symbols)

% Optional custom commands
\newcommand{\vect}[1]{\mathbf{#1}}
\newcommand{\ehat}[1]{\hat{\vect{e}}_{#1}}

\begin{document}

\begin{center}
{\Large\bfseries Chapter X, Problem Y}\\[6pt]
Byron \& Fuller, \textit{Mathematics of Classical and Quantum Physics}
\end{center}

\bigskip

\textbf{Problem.} [Problem statement]

\bigskip
\textbf{Solution.}

[Full step-by-step solution with equations, explanations, and boxed final answers]

\hfill $\blacksquare$

\end{document}
```

### 2.2 Solution Style

- **Solution** includes every intermediate step, not just the final answer
- **Key results** are highlighted with `\boxed{...}`
- **Physical interpretation** or remarks are included where appropriate
- **Verification** steps (e.g., checking limiting cases, trace conditions) are shown when natural
- Multi-part problems use `\subsection*{(a) ...}` etc.

### 2.3 Chapter 1 Output

17 problems solved → 17 `.tex` files → 17 `.pdf` files:
```
ch01_01.pdf  (Rhombus diagonals are orthogonal)
ch01_02.pdf  (Circular motion: v⊥r, acceleration, angular momentum)
...
ch01_17.pdf  (Multipole moments for point charge)
```

### 2.4 Compilation Verification

Each file was compiled individually and all compiled successfully on first attempt.

---

## Phase 3: Chapters 2–10 — Parallel Agent Team

### 3.1 Initial Approach: Sequential Chapter-by-Chapter

The initial plan was to solve chapters one at a time.

### 3.2 Revised Approach: Parallel Agent Team

To speed up the process, a team of 9 specialized agents was created using Claude Code's `Agent` tool:

**Team name:** `byron-fuller-solutions`

**Agents created:**
| Agent ID | Assignment |
|----------|------------|
| ch02-solver | Chapter 2: Calculus of Variations |
| ch03-solver | Chapter 3: Vectors and Matrices |
| ch04-solver | Chapter 4: Vector Spaces in Physics |
| ch05-solver | Chapter 5: Hilbert Space |
| ch06-solver | Chapter 6: Complex Variable Theory |
| ch07-solver | Chapter 7: Green's Functions |
| ch08-solver | Chapter 8: Intro to Integral Equations |
| ch09-solver | Chapter 9: Integral Equations in Hilbert Space |
| ch10-solver | Chapter 10: Intro to Group Theory |

### 3.3 Agent Prompt Template

Each agent received a detailed prompt containing:

1. **The task:** "Solve all end-of-chapter problems for Chapter X of Byron & Fuller"
2. **Page locations:** Specific page ranges for the problem section and key chapter content
3. **LaTeX template:** The exact template established in Phase 2
4. **Compilation instructions:** Use `tectonic` to compile each `.tex` file
5. **Output directory and naming convention:** `chXX_YY.tex` / `chXX_YY.pdf`

### 3.4 Agent Workflow (per agent)

Each agent independently:

1. Read the problem pages (PNG images) to transcribe all problem statements
2. Read relevant chapter sections for context (theorems, equations, examples)
3. Wrote each solution as a standalone `.tex` file
4. Compiled each `.tex` file with `tectonic`
5. Fixed any compilation errors (typos, missing packages, etc.)
6. Reported completion with a summary of all problems solved

### 3.5 Agent Results

| Agent | Problems Found | PDFs Produced | Notes |
|-------|---------------|---------------|-------|
| ch02-solver | 13 | 13 | Clean run |
| ch03-solver | 28 | 28 | Clean run |
| ch04-solver | 27 | 27 | Had `\uusepackage` typo in all files; fixed with sed |
| ch05-solver | 33 | 33 | Clean run |
| ch06-solver | 39 | 39 | Clean run |
| ch07-solver | 29 | 29 | Clean run |
| ch08-solver | 26 | 26 | Clean run |
| ch09-solver | 27 | 0 | Agent went idle; produced nothing |
| ch10-solver | 24 | 24 | Clean run |

### 3.6 Agent Failure: Chapter 9

The ch09-solver agent failed to produce any output. It went idle without creating files. The root cause was likely a context window issue or the agent entering an idle state.

**Resolution:** Chapter 9 was solved manually by the main agent (see Phase 4).

---

## Phase 4: Chapter 9 — Manual Recovery

### 4.1 Problem Discovery

The Ch9 problems section was harder to locate than other chapters because:
- The chapter is long (~70 pages)
- The PROBLEMS section starts deep into the chapter
- Problems span 10 pages

### 4.2 Problem Inventory

27 problems were identified, covering:

| Problems | Topics |
|----------|--------|
| 1–4 | Completeness, measure zero modifications, mean convergence, Hilbert-Schmidt norm |
| 5 | Rayleigh-Ritz variational method (generalized eigenvalue problem) |
| 6–8 | Parity operator P, commutation with integral operator A, trial functions |
| 9 | Hydrogen atom Stark effect (nearly degenerate perturbation theory) |
| 10 | Maximum principle for second-order perturbation correction |
| 11 | Simpson's rule discretization of integral equations |
| 12 | Finite-rank kernel approximations |
| 13–16 | Fredholm determinant and numerator: convergence, recursion, resolvent |
| 17–18 | Residues of resolvent, rank-1 kernel Fredholm reduction |
| 19 | Neumann series vs Fredholm series agreement |
| 20 | Extension to square-integrable kernels (Carleman modification) |
| 21–24 | Scattering theory: Yukawa potential, Born approximation, optical theorem, phase shifts |
| 25 | Numerical solution of integral equations |
| 26 | Extension of Fourier transform to L₂ (Theorem 9.11 completion) |
| 27 | Hermite functions as Fourier transform eigenfunctions |

### 4.3 Context Reading

To solve these problems, the following chapter sections were read:
- Section 9.1: Completely continuous Hermitian operators (Theorems 9.1–9.5)
- Section 9.2: Eigenvalue problems and perturbation theory (Eqs. 9.33–9.42)
- Section 9.3: Finite-rank techniques
- Section 9.4: Fredholm alternative
- Section 9.5: Numerical solution of integral equations (Eqs. 9.98–9.113)
- Section 9.6: Unitary transformations (Theorem 9.11)

### 4.4 Writing Strategy

Solutions were written in batches of 6, then compiled:
- Batch 1: Problems 1–6 (wrote, compiled, all passed)
- Batch 2: Problems 7–12 (wrote, compiled, all passed)
- Batch 3: Problems 13–18 (wrote, compiled in background, all passed)
- Batch 4: Problems 19–27 (wrote, compiled in background, all passed)

All 27 PDFs produced successfully.

---

## Phase 5: Bug Fixes and Quality Assurance

### 5.1 Chapter 4 Compilation Failure

**Problem:** All 26 `.tex` files in `ch04_tex/` had `\uusepackage` (double 'u') on line 3 instead of `\usepackage`. This was a systematic typo by the ch04-solver agent.

**Detection:** Batch compilation failed for all ch04 files.

**Fix:**
```bash
for f in /path/to/ch04_tex/*.tex; do
  sed -i 's/\\uusepackage/\\usepackage/g' "$f"
done
```

**Result:** All 27 ch04 files compiled successfully after the fix.

### 5.2 Batch Compilation Verification

A batch compilation script was run across all chapters to verify every `.tex` file produces a valid PDF:

```bash
for ch in ch01 ch02 ch03 ch04 ch05 ch06 ch07 ch08 ch09 ch10; do
  for f in /path/to/${ch}_tex/*.tex; do
    tectonic "$f" 2>&1 | tail -1
  done
done
```

### 5.3 Final PDF Count Verification

```
ch01: 17 PDFs
ch02: 13 PDFs
ch03: 28 PDFs
ch04: 27 PDFs
ch05: 33 PDFs
ch06: 39 PDFs
ch07: 29 PDFs
ch08: 26 PDFs
ch09: 27 PDFs
ch10: 24 PDFs
TOTAL: 263 PDFs
```

---

## Directory Structure (Final)

```
.
├── ch01/                 # Chapter 1 solution PDFs (17 files)
├── ch02/                 # Chapter 2 solution PDFs (13 files)
├── ch03/                 # Chapter 3 solution PDFs (28 files)
├── ch04/                 # Chapter 4 solution PDFs (27 files)
├── ch05/                 # Chapter 5 solution PDFs (33 files)
├── ch06/                 # Chapter 6 solution PDFs (39 files)
├── ch07/                 # Chapter 7 solution PDFs (29 files)
├── ch08/                 # Chapter 8 solution PDFs (26 files)
├── ch09/                 # Chapter 9 solution PDFs (27 files)
├── ch10/                 # Chapter 10 solution PDFs (24 files)
├── ch01_tex/             # Chapter 1 LaTeX sources
├── ch02_tex/             # Chapter 2 LaTeX sources
├── ...                   # (one *_tex/ directory per chapter)
├── ch10_tex/             # Chapter 10 LaTeX sources
├── README.md
└── WORKFLOW_DOCUMENTATION.md  (this file)
```

---

## Tools and Technologies Used

| Tool | Purpose |
|------|---------|
| Claude Code (Opus 4.6) | Main orchestrator, problem solver, LaTeX author |
| Claude Code Agent tool | Spawned 9 parallel sub-agents for Chapters 2–10 |
| Claude Code Read tool (multimodal) | Read page images to extract math/text |
| Tectonic v0.15.0 | LaTeX → PDF compilation |
| Bash | Shell for compilation scripts and file management |

---

## Problem Count by Chapter

| Ch | Title | Problems |
|----|-------|----------|
| 1 | Vectors in Classical Physics | 17 |
| 2 | Calculus of Variations | 13 |
| 3 | Vectors and Matrices | 28 |
| 4 | Vector Spaces in Physics | 27 |
| 5 | Hilbert Space | 33 |
| 6 | Complex Variable Theory | 39 |
| 7 | Green's Functions | 29 |
| 8 | Introduction to Integral Equations | 26 |
| 9 | Integral Equations in Hilbert Space | 27 |
| 10 | Introduction to Group Theory | 24 |
| **Total** | | **263** |

---

## Known Limitations and Caveats

1. **AI-generated solutions:** All solutions were produced by Claude Opus 4.6 and have not been individually verified for mathematical correctness.

2. **Agent solution quality:** The 8 chapters solved by sub-agents (Ch2–8, Ch10) were not individually reviewed. The agents may have misread some details or made mathematical errors.

3. **Chapter 9 agent failure:** The ch09-solver agent produced zero output, requiring manual intervention. The root cause was likely context window exhaustion.

4. **Cross-chapter references:** Some problems reference results from earlier chapters. Agents solving later chapters may not have read the earlier chapter material, potentially missing context.

5. **Figures and graphs:** Problems that reference figures in the text (e.g., "see Fig. 9.4") could not be fully addressed since the agent cannot reproduce the original figures in the PDF solutions.

6. **Computational problems:** A few problems ask for numerical computation. These were addressed with analytical outlines rather than actual numerical code execution.

7. **Chapter 4 typo:** All ch04 `.tex` files had a systematic `\uusepackage` typo that required a bulk sed fix before compilation.

---

## Reproducibility

To reproduce this workflow:

1. Ensure `tectonic` is installed (`scoop install tectonic`, `brew install tectonic`, or equivalent)
2. Have the book's pages available as images for multimodal reading
3. For each chapter:
   a. Read the problem pages to transcribe problem statements
   b. Read relevant chapter sections for context
   c. Write each solution as a standalone `.tex` file following the template
   d. Compile with `tectonic filename.tex`
4. Verify all PDFs are produced without errors

The entire process can be parallelized at the chapter level since chapters are independent (modulo cross-references to earlier material).
