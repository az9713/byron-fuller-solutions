# LaTeX Reference for Beginners

A gentle introduction to LaTeX for those new to document typesetting. This guide assumes you have programming experience (C, C++, Java) but no LaTeX background.

## Table of Contents

1. [What Is LaTeX?](#what-is-latex)
2. [LaTeX vs. Programming](#latex-vs-programming)
3. [Document Structure](#document-structure)
4. [Basic Text Formatting](#basic-text-formatting)
5. [Mathematical Notation](#mathematical-notation)
6. [Environments](#environments)
7. [Cross-References](#cross-references)
8. [Commands and Macros](#commands-and-macros)
9. [Common Errors](#common-errors)
10. [Cheat Sheet](#cheat-sheet)

---

## What Is LaTeX?

### The Concept

LaTeX (pronounced "LAY-tek" or "LAH-tek") is a document preparation system. Think of it as:

- **Source code** → **Compiler** → **Output**
- `.tex` file → `pdflatex` → `.pdf` file

Just like you write C code and compile it to an executable, you write LaTeX code and compile it to a PDF.

### Why LaTeX?

1. **Mathematical typesetting**: Equations look professional
2. **Automatic numbering**: Equations, sections, references
3. **Consistency**: Same formatting throughout
4. **Version control friendly**: It's plain text

### The Workflow

```
1. Write/edit .tex file
2. Run pdflatex
3. View the .pdf
4. Repeat
```

---

## LaTeX vs. Programming

If you know programming, LaTeX will feel familiar:

| Concept | C/C++/Java | LaTeX |
|---------|------------|-------|
| Source file extension | `.c`, `.cpp`, `.java` | `.tex` |
| Compiler | gcc, g++, javac | pdflatex |
| Output | executable, .class | .pdf |
| Include files | `#include`, `import` | `\input{}`, `\usepackage{}` |
| Functions | `void foo() {...}` | `\newcommand{\foo}{...}` |
| Comments | `// comment` or `/* */` | `% comment` |
| Main function | `main()` | `\begin{document}` |
| Blocks | `{ }` | `\begin{} ... \end{}` |
| Escape character | `\` | `\` |
| String quotes | `"string"` | ``` ``string'' ``` |

### Key Differences

1. **LaTeX is markup, not algorithmic**
   - You describe WHAT the document should contain
   - Not HOW to create it step by step

2. **Compilation is iterative**
   - Often need to run 2-3 times for references

3. **Errors stop compilation**
   - Like a compiler, but you can choose to continue

---

## Document Structure

### Minimal Document

```latex
\documentclass{article}          % Like #include <stdio.h>

\begin{document}                 % Like main() {

Hello, world!                    % Content

\end{document}                   % Like }
```

### Full Document Structure

```latex
% ===== PREAMBLE (before \begin{document}) =====

\documentclass[11pt,a4paper]{book}    % Document type and options

% Packages (like libraries)
\usepackage{amsmath}                  % Advanced math
\usepackage{amsthm}                   % Theorem environments
\usepackage{hyperref}                 % Clickable links

% Custom commands (like function definitions)
\newcommand{\vect}[1]{\mathbf{#1}}   % \vect{x} → bold x

% ===== DOCUMENT BODY =====

\begin{document}

\title{My Document}
\author{Your Name}
\maketitle

\tableofcontents

\chapter{Introduction}
Content goes here...

\section{Subsection}
More content...

\end{document}
```

### Document Classes

| Class | Purpose | Example |
|-------|---------|---------|
| `article` | Short documents | Papers, homework |
| `report` | Medium documents | Theses, reports |
| `book` | Long documents | Books, tutorials |
| `letter` | Letters | Correspondence |

This project uses `book` class.

---

## Basic Text Formatting

### Text Styles

```latex
\textbf{bold text}              % Bold
\textit{italic text}            % Italic
\underline{underlined}          % Underline
\texttt{monospace}              % Code/typewriter font
\emph{emphasized}               % Usually italic, context-aware
```

### Paragraphs and Spacing

```latex
First paragraph.
Still the first paragraph (single newline is ignored).

Second paragraph (blank line creates new paragraph).

Force line break\\
without new paragraph.

Add vertical space:
\vspace{1cm}
More text after space.
```

### Lists

```latex
% Bullet list
\begin{itemize}
    \item First item
    \item Second item
    \item Third item
\end{itemize}

% Numbered list
\begin{enumerate}
    \item First item
    \item Second item
    \item Third item
\end{enumerate}

% Description list
\begin{description}
    \item[Term 1] Definition of term 1
    \item[Term 2] Definition of term 2
\end{description}
```

### Special Characters

Some characters have special meaning in LaTeX:

| Character | Meaning | To type literally |
|-----------|---------|-------------------|
| `%` | Comment | `\%` |
| `$` | Math mode | `\$` |
| `&` | Table alignment | `\&` |
| `#` | Macro parameter | `\#` |
| `_` | Subscript | `\_` |
| `^` | Superscript | `\^{}` |
| `{` `}` | Grouping | `\{` `\}` |
| `~` | Non-breaking space | `\~{}` |
| `\` | Command prefix | `\textbackslash` |

---

## Mathematical Notation

### Math Modes

```latex
% INLINE MATH (within text)
The equation $E = mc^2$ shows...
% Alternative: \( E = mc^2 \)

% DISPLAY MATH (centered, on its own line)
\[
    E = mc^2
\]
% Alternative: $$ E = mc^2 $$

% DISPLAY MATH WITH NUMBER
\begin{equation}
    E = mc^2
    \label{eq:einstein}
\end{equation}
```

### Common Math Symbols

```latex
% Greek letters
\alpha, \beta, \gamma, \delta, \epsilon
\Gamma, \Delta, \Omega         % Capital Greek

% Operations
+ - \times \div \pm \mp

% Relations
= \neq \leq \geq < > \approx \equiv \propto

% Arrows
\rightarrow \leftarrow \Rightarrow \Leftarrow \leftrightarrow

% Logic
\forall \exists \neg \land \lor \in \notin \subset \supset

% Sets
\cup \cap \emptyset \setminus

% Calculus
\partial \nabla \infty \int \sum \prod \lim

% Other
\cdot \ldots \cdots \vdots \ddots
```

### Fractions, Exponents, Subscripts

```latex
% Fractions
\frac{a}{b}                    % a over b
\frac{x^2 + 1}{x - 1}          % Complex fraction

% Exponents (superscripts)
x^2                            % x squared
x^{10}                         % x to the 10th (braces for multiple chars)
e^{i\pi}                       % e to the i*pi

% Subscripts
x_1                            % x sub 1
x_{ij}                         % x sub ij
a_{n+1}                        % Subscript with expression

% Both
x_1^2                          % x sub 1 squared
\sum_{i=1}^{n} x_i             % Sum from i=1 to n
```

### Roots and Functions

```latex
% Square root
\sqrt{x}
\sqrt{x^2 + y^2}

% nth root
\sqrt[3]{x}                    % Cube root
\sqrt[n]{x}                    % nth root

% Named functions (upright, not italic)
\sin, \cos, \tan, \log, \ln, \exp
\sin(x), \log_2(n)

% Limits
\lim_{x \to 0} \frac{\sin x}{x}
\lim_{n \to \infty} a_n
```

### Matrices and Vectors

```latex
% Vector (bold)
\mathbf{v}                     % Bold v
\vec{v}                        % Arrow over v

% Matrix (parentheses)
\begin{pmatrix}
    a & b \\
    c & d
\end{pmatrix}

% Matrix (brackets)
\begin{bmatrix}
    1 & 0 \\
    0 & 1
\end{bmatrix}

% Matrix (determinant bars)
\begin{vmatrix}
    a & b \\
    c & d
\end{vmatrix}
```

### Integrals and Sums

```latex
% Integrals
\int f(x) \, dx                % Indefinite integral
\int_0^1 x^2 \, dx             % Definite integral
\int_a^b                       % Limits above and below
\iint, \iiint                  % Double, triple integrals
\oint                          % Contour integral

% Sums and Products
\sum_{i=1}^{n} x_i             % Sum
\prod_{i=1}^{n} x_i            % Product

% The \, adds a small space before dx
```

### Aligned Equations

```latex
% Multiple aligned equations
\begin{align}
    a &= b + c \\              % & marks alignment point
    d &= e + f + g \\
    x &= y
\end{align}

% Without numbering
\begin{align*}
    a &= b + c \\
    d &= e + f
\end{align*}
```

### Brackets and Delimiters

```latex
% Manual sizing
(x), [x], \{x\}, |x|, \|x\|

% Auto-sizing (recommended)
\left( \frac{a}{b} \right)
\left[ \frac{a}{b} \right]
\left\{ \frac{a}{b} \right\}
\left| \frac{a}{b} \right|
\left\| \frac{a}{b} \right\|

% You can mix: \left( ... \right]
```

---

## Environments

Environments are like blocks in programming - they define a region with special formatting.

### Syntax

```latex
\begin{environment_name}
    content
\end{environment_name}
```

### Common Environments

```latex
% ITEMIZE - Bullet list
\begin{itemize}
    \item First
    \item Second
\end{itemize}

% ENUMERATE - Numbered list
\begin{enumerate}
    \item First
    \item Second
\end{enumerate}

% EQUATION - Numbered equation
\begin{equation}
    E = mc^2
\end{equation}

% ALIGN - Aligned equations
\begin{align}
    a &= b \\
    c &= d
\end{align}

% FIGURE - For images
\begin{figure}
    \centering
    \includegraphics[width=0.8\textwidth]{image.png}
    \caption{My figure}
    \label{fig:myfig}
\end{figure}

% TABLE - For tables
\begin{table}
    \centering
    \begin{tabular}{|c|c|c|}
        \hline
        A & B & C \\
        \hline
        1 & 2 & 3 \\
        \hline
    \end{tabular}
    \caption{My table}
    \label{tab:mytab}
\end{table}
```

### Theorem-Like Environments (from amsthm)

```latex
% These are defined in the preamble:
% \newtheorem{theorem}{Theorem}[section]

\begin{definition}[Optional title]
    A vector space is...
\end{definition}

\begin{theorem}[Pythagorean]
    For a right triangle: $a^2 + b^2 = c^2$.
\end{theorem}

\begin{lemma}
    Helper result...
\end{lemma}

\begin{proof}
    We prove by induction...

    Therefore, the result holds.
\end{proof}
% Proof automatically adds ∎ at the end
```

### Custom Environments in This Project

```latex
% Intuition box (green)
\begin{intuition}
    The key insight is that...
\end{intuition}

% Warning box (red)
\begin{warning}
    A common mistake is...
\end{warning}

% Physical interpretation (blue)
\begin{physical}
    Physically, this means...
\end{physical}

% Key step (purple)
\begin{keystep}
    The crucial calculation is...
\end{keystep}
```

---

## Cross-References

### Creating Labels

```latex
\section{Introduction}
\label{sec:intro}              % Label for this section

\begin{equation}
    E = mc^2
    \label{eq:einstein}        % Label for this equation
\end{equation}

\begin{theorem}
    ...
    \label{thm:main}           % Label for this theorem
\end{theorem}
```

### Using References

```latex
As discussed in Section~\ref{sec:intro}...

Using Equation~\eqref{eq:einstein}...  % Adds parentheses

By Theorem~\ref{thm:main}...
```

### Why References?

- **Automatic numbering**: Change document order, references update
- **Clickable links**: With hyperref package
- **Consistency**: No manual tracking of numbers

### The Tilde (~)

The `~` creates a non-breaking space:
```latex
Section~\ref{sec:intro}        % "Section" and "1" stay on same line
```

---

## Commands and Macros

### Using Existing Commands

```latex
\textbf{bold}                  % Command with argument in braces
\sqrt{x}                       % Command with argument
\frac{a}{b}                    % Command with two arguments
\section{Title}                % Creates a section
```

### Defining New Commands

```latex
% Simple replacement
\newcommand{\R}{\mathbb{R}}    % \R → ℝ

% With one argument
\newcommand{\vect}[1]{\mathbf{#1}}
% Usage: \vect{x} → 𝐱

% With two arguments
\newcommand{\inner}[2]{\langle #1, #2 \rangle}
% Usage: \inner{x}{y} → ⟨x, y⟩

% With optional argument
\newcommand{\norm}[1]{\left\| #1 \right\|}
% Usage: \norm{x} → ‖x‖
```

### Commands Used in This Project

From `physics-macros.tex`:

```latex
\vect{x}        % Bold vector: 𝐱
\uvect{n}       % Unit vector: n̂
\grad           % Gradient: ∇
\div            % Divergence: ∇·
\curl           % Curl: ∇×
\R              % Real numbers: ℝ
\C              % Complex numbers: ℂ
\comm{A}{B}     % Commutator: [A, B]
```

---

## Common Errors

### Error: Missing $ inserted

**Problem:**
```latex
The variable x is positive.    % WRONG
```

**Solution:**
```latex
The variable $x$ is positive.  % CORRECT
```

Math symbols need math mode!

---

### Error: Undefined control sequence

**Problem:**
```latex
\bfx                           % WRONG - no such command
```

**Solution:**
```latex
\mathbf{x}                     % CORRECT
% or use custom command:
\vect{x}                       % If \vect is defined
```

---

### Error: Missing \begin{document}

**Problem:** Something went wrong in the preamble (before `\begin{document}`).

**Solution:** Check for:
- Typos in package names
- Unclosed braces
- Invalid commands in preamble

---

### Error: File not found

**Problem:**
```latex
\input{chapter1}               % Can't find chapter1.tex
```

**Solution:**
- Check the filename exactly (case-sensitive on Linux/Mac)
- Check the path is correct
- Don't include `.tex` extension

---

### Error: Environment not closed

**Problem:**
```latex
\begin{theorem}
    Content...
                               % Missing \end{theorem}!
```

**Solution:** Every `\begin{X}` needs an `\end{X}`.

---

## Cheat Sheet

### Essential Commands

| Command | Result | Notes |
|---------|--------|-------|
| `\textbf{x}` | **x** | Bold text |
| `\textit{x}` | *x* | Italic text |
| `$x$` | *x* | Inline math |
| `\[ x \]` | (display) | Display math |
| `\frac{a}{b}` | a/b | Fraction |
| `x^2` | x² | Superscript |
| `x_i` | xᵢ | Subscript |
| `\sqrt{x}` | √x | Square root |
| `\sum` | Σ | Summation |
| `\int` | ∫ | Integral |

### Greek Letters

| Lowercase | Uppercase | Command |
|-----------|-----------|---------|
| α | A | `\alpha`, A |
| β | B | `\beta`, B |
| γ | Γ | `\gamma`, `\Gamma` |
| δ | Δ | `\delta`, `\Delta` |
| ε | E | `\epsilon`, E |
| θ | Θ | `\theta`, `\Theta` |
| λ | Λ | `\lambda`, `\Lambda` |
| μ | M | `\mu`, M |
| π | Π | `\pi`, `\Pi` |
| σ | Σ | `\sigma`, `\Sigma` |
| φ | Φ | `\phi`, `\Phi` |
| ω | Ω | `\omega`, `\Omega` |

### Document Structure

```latex
\chapter{Title}        % Book class only
\section{Title}
\subsection{Title}
\subsubsection{Title}
\paragraph{Title}
```

### Compilation Steps

```bash
cd output
pdflatex main.tex      # First pass
pdflatex main.tex      # Second pass (for references)
# Open main.pdf
```

### Quick Fixes

| Problem | Solution |
|---------|----------|
| ?? instead of numbers | Run pdflatex again |
| Missing package | Install via MiKTeX/tlmgr |
| Undefined command | Check spelling, add package |
| Overfull hbox | Usually OK to ignore |
| PDF won't open | Close and retry |

---

## Next Steps

### Learn More

1. **Practice**: Edit the existing `.tex` files
2. **Experiment**: Try adding your own notes
3. **Read**: The Developer Guide for advanced topics
4. **Reference**: TeX Stack Exchange for specific questions

### Useful Resources

- **Overleaf Documentation**: https://www.overleaf.com/learn
- **LaTeX Wikibook**: https://en.wikibooks.org/wiki/LaTeX
- **Detexify** (draw symbols): https://detexify.kirelabs.org/
- **LaTeX Math Symbols**: https://oeis.org/wiki/List_of_LaTeX_mathematical_symbols
