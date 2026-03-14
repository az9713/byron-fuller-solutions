# Troubleshooting Guide

Solutions to common problems you might encounter when using this project.

## Table of Contents

1. [PDF Viewing Issues](#pdf-viewing-issues)
2. [LaTeX Installation Problems](#latex-installation-problems)
3. [Compilation Errors](#compilation-errors)
4. [Missing Packages](#missing-packages)
5. [Cross-Reference Problems](#cross-reference-problems)
6. [Formatting Issues](#formatting-issues)
7. [File Not Found Errors](#file-not-found-errors)
8. [Performance Issues](#performance-issues)
9. [Claude Code Issues](#claude-code-issues)
10. [Getting More Help](#getting-more-help)

---

## PDF Viewing Issues

### Problem: PDF won't open

**Symptoms:**
- Double-clicking `main.pdf` does nothing
- Error message about file association
- "Choose an app" dialog appears

**Solutions:**

**Windows:**
1. Right-click `main.pdf`
2. Select "Open with"
3. Choose "Adobe Acrobat Reader" or your preferred PDF viewer
4. Check "Always use this app"

**Mac:**
1. Right-click `main.pdf`
2. Select "Open With" → "Preview"
3. Or install Adobe Reader: https://get.adobe.com/reader/

**Linux:**
```bash
# Install a PDF viewer
sudo apt-get install evince    # Ubuntu/Debian
sudo dnf install evince        # Fedora

# Open the PDF
evince output/main.pdf
```

---

### Problem: PDF displays but equations look wrong

**Symptoms:**
- Equations show as rectangles or question marks
- Fonts appear corrupted
- Mathematical symbols missing

**Solutions:**

1. **Update your PDF viewer**
   - Download the latest version of Adobe Reader or your preferred viewer

2. **Try a different PDF viewer**
   - Adobe Acrobat Reader (recommended for math)
   - SumatraPDF (Windows)
   - Preview (Mac)
   - Evince or Okular (Linux)

3. **Check your system fonts**
   - Ensure Latin Modern fonts are installed
   - These come with LaTeX distributions

---

### Problem: Clickable links don't work

**Symptoms:**
- Cross-references show numbers but don't link
- Table of Contents entries aren't clickable
- URLs don't open

**Solutions:**

1. **Check PDF viewer settings**
   - Some viewers disable links by default
   - Look for "Enable links" or similar option

2. **Try a different viewer**
   - Adobe Reader has best link support

3. **Recompile the PDF**
   - Run pdflatex three times to ensure hyperref is properly set up:
   ```bash
   cd output
   pdflatex main.tex && pdflatex main.tex && pdflatex main.tex
   ```

---

## LaTeX Installation Problems

### Problem: pdflatex command not found

**Symptoms:**
```
'pdflatex' is not recognized as an internal or external command
```
or
```
bash: pdflatex: command not found
```

**Solutions:**

**Windows (MiKTeX):**

1. **Check if MiKTeX is installed**
   - Open Start Menu, search "MiKTeX"
   - If not found, install from https://miktex.org/download

2. **Add to PATH manually**
   - Find your MiKTeX bin folder, usually:
     ```
     C:\Users\<YourName>\AppData\Local\Programs\MiKTeX\miktex\bin\x64\
     ```
   - Add to PATH:
     1. Search "Environment Variables" in Start Menu
     2. Click "Environment Variables" button
     3. Under "User variables", find "Path", click "Edit"
     4. Click "New", paste the MiKTeX path
     5. Click "OK" on all dialogs
     6. **Restart** your terminal/command prompt

3. **Use full path instead**
   ```cmd
   "C:\Users\YourName\AppData\Local\Programs\MiKTeX\miktex\bin\x64\pdflatex.exe" main.tex
   ```

**Mac (MacTeX):**

1. **Check installation**
   ```bash
   which pdflatex
   ```
   Should return something like `/usr/local/texlive/2024/bin/x86_64-darwin/pdflatex`

2. **If not found, install MacTeX**
   ```bash
   brew install --cask mactex
   ```

3. **Update shell configuration**
   ```bash
   # For bash
   echo 'eval "$(/usr/libexec/path_helper)"' >> ~/.bash_profile
   source ~/.bash_profile

   # For zsh
   echo 'eval "$(/usr/libexec/path_helper)"' >> ~/.zshrc
   source ~/.zshrc
   ```

**Linux:**

1. **Install TeX Live**
   ```bash
   # Ubuntu/Debian
   sudo apt-get update
   sudo apt-get install texlive-full

   # Fedora
   sudo dnf install texlive-scheme-full
   ```

2. **Verify installation**
   ```bash
   pdflatex --version
   ```

---

### Problem: MiKTeX installation hangs or fails

**Symptoms:**
- Installer stuck at a certain percentage
- "Installation failed" error

**Solutions:**

1. **Run as administrator**
   - Right-click the installer
   - Select "Run as administrator"

2. **Disable antivirus temporarily**
   - Some antivirus software interferes with installation
   - Re-enable after installation completes

3. **Use the basic installer first**
   - Download "Basic MiKTeX" instead of full version
   - Missing packages will be installed on-demand

4. **Check disk space**
   - Full installation needs 2-5 GB
   - Ensure sufficient free space

---

## Compilation Errors

### Problem: "! LaTeX Error: File `physics.sty' not found"

**Symptoms:**
```
! LaTeX Error: File `physics.sty' not found.
```
(or any other `.sty` file)

**Solutions:**

**MiKTeX (Windows):**
1. MiKTeX should auto-install missing packages
2. If not, open MiKTeX Console:
   - Search "MiKTeX Console" in Start Menu
   - Go to "Packages" tab
   - Search for "physics"
   - Click "+" to install

**MacTeX/TeX Live:**
```bash
# Install specific package
sudo tlmgr install physics

# Or update everything
sudo tlmgr update --all
```

**Linux:**
```bash
# Ubuntu/Debian
sudo apt-get install texlive-science  # Contains physics package

# Or install everything
sudo apt-get install texlive-full
```

---

### Problem: "! Missing $ inserted"

**Symptoms:**
```
! Missing $ inserted.
<inserted text>
                $
l.42 ...for all vectors x
                         and y
```

**Cause:** Mathematical content outside of math mode.

**Solutions:**

1. **Find the line number** (e.g., line 42)

2. **Open the file and find the problem**
   ```latex
   % Wrong:
   for all vectors x and y

   % Correct:
   for all vectors $\vect{x}$ and $\vect{y}$
   ```

3. **Wrap math in dollar signs**
   - Inline math: `$x$`
   - Display math: `\[ x \]`

---

### Problem: "! Undefined control sequence"

**Symptoms:**
```
! Undefined control sequence.
l.55 \vect
          {x}
```

**Cause:** Using a command that hasn't been defined.

**Solutions:**

1. **Check spelling**
   - `\vect` vs `\vec` vs `\mathbf`

2. **Check if package is loaded**
   - The `\vect` command is defined in `main.tex`
   - Make sure `\newcommand{\vect}[1]{\mathbf{#1}}` exists in the preamble

3. **Check for typos in command name**
   ```latex
   % Wrong:
   \beigin{theorem}

   % Correct:
   \begin{theorem}
   ```

---

### Problem: "! Emergency stop"

**Symptoms:**
```
! Emergency stop.
<*> main.tex

*** (job aborted, no legal \end found)
```

**Cause:** Missing `\end{document}` or mismatched environments.

**Solutions:**

1. **Check for missing `\end{document}`**
   - Must be the last line of `main.tex`

2. **Check for mismatched environments**
   ```latex
   % Wrong:
   \begin{theorem}
   ...
   \end{proof}  % Should be \end{theorem}

   % Correct:
   \begin{theorem}
   ...
   \end{theorem}
   ```

3. **Check included files**
   - Each chapter file must have balanced `\begin`/`\end` pairs
   - No `\documentclass` or `\begin{document}` in chapter files

---

## Missing Packages

### Problem: tcolorbox errors

**Symptoms:**
```
! LaTeX Error: File `tcolorbox.sty' not found.
```
or
```
! Package tcolorbox Error: You have requested library `theorems'
```

**Solutions:**

1. **Install the full tcolorbox package**

   **MiKTeX:**
   - Open MiKTeX Console → Packages
   - Search "tcolorbox"
   - Install "tcolorbox" package

   **TeX Live:**
   ```bash
   sudo tlmgr install tcolorbox
   ```

2. **Install dependencies**
   tcolorbox needs several other packages:
   ```bash
   sudo tlmgr install pgf environ etoolbox
   ```

---

### Problem: hyperref errors

**Symptoms:**
```
! Package hyperref Error: Wrong DVI mode driver option `pdftex'
```

**Solutions:**

1. **Use pdflatex, not latex**
   ```bash
   # Wrong:
   latex main.tex

   # Correct:
   pdflatex main.tex
   ```

2. **Check for conflicting packages**
   - Load `hyperref` last (it should be one of the final packages loaded)

---

## Cross-Reference Problems

### Problem: "??" instead of numbers

**Symptoms:**
- Equations show as "Eq. (??)"
- References show "Theorem ??"
- Table of contents missing page numbers

**Solutions:**

1. **Run pdflatex multiple times**
   ```bash
   pdflatex main.tex
   pdflatex main.tex
   pdflatex main.tex
   ```

   Why? LaTeX needs multiple passes:
   - First pass: Creates labels
   - Second pass: Resolves references
   - Third pass: Finalizes everything

2. **Check for typos in labels**
   ```latex
   % In one place:
   \label{eq:schwarz}

   % In another place (WRONG - typo!):
   \ref{eq:schwartz}
   ```

3. **Check the log file**
   ```bash
   grep "undefined" main.log
   ```
   This shows which references couldn't be resolved.

---

### Problem: "Label multiply defined"

**Symptoms:**
```
LaTeX Warning: Label `eq:energy' multiply defined.
```

**Cause:** Same label used twice.

**Solutions:**

1. **Search for duplicate labels**
   ```bash
   grep -r "label{eq:energy}" output/
   ```

2. **Rename one of them**
   ```latex
   \label{eq:energy-kinetic}
   \label{eq:energy-potential}
   ```

---

## Formatting Issues

### Problem: Text overflows into margin

**Symptoms:**
- Text or equations extend past the right margin
- "Overfull \hbox" warnings

**Solutions:**

1. **For equations that are too long**
   ```latex
   % Use multline for breaking equations
   \begin{multline}
       \text{very long equation part 1} \\
       + \text{very long equation part 2}
   \end{multline}
   ```

2. **For text**
   - Break long words manually: `super\-cali\-fragilistic`
   - Reword to use shorter phrases

3. **Minor overflows are often OK**
   - The warning threshold is strict
   - If it looks fine in the PDF, it's usually fine

---

### Problem: Colored boxes don't display correctly

**Symptoms:**
- Boxes appear as plain text
- Colors missing
- Box borders broken

**Solutions:**

1. **Check tcolorbox is loaded**
   - The preamble should have:
   ```latex
   \usepackage{tcolorbox}
   \tcbuselibrary{theorems,skins,breakable}
   ```

2. **Check environment names**
   ```latex
   % These are the defined environments:
   \begin{intuition}   % Green box
   \begin{warning}     % Red box
   \begin{physical}    % Blue box
   \begin{keystep}     % Purple box
   ```

---

## File Not Found Errors

### Problem: "File `chapters/ch01_scalar_product.tex' not found"

**Symptoms:**
```
! LaTeX Error: File `chapters/ch01_scalar_product.tex' not found.
```

**Solutions:**

1. **Check you're in the right directory**
   ```bash
   # You should be in the output/ directory
   cd output
   ls chapters/   # Should list .tex files
   ```

2. **Check the filename matches exactly**
   - Case-sensitive on Linux/Mac
   - Check for spaces or special characters

3. **Check the path in main.tex**
   ```latex
   % Relative to main.tex location:
   \input{chapters/ch01_scalar_product}
   ```

---

### Problem: "I can't find file `main.tex'"

**Symptoms:**
```
I can't find file `main.tex'.
Please type another input file name:
```

**Solutions:**

1. **Navigate to the correct directory**
   ```bash
   cd /path/to/byron_fuller/output
   pdflatex main.tex
   ```

2. **Use full path**
   ```bash
   pdflatex /full/path/to/output/main.tex
   ```

---

## Performance Issues

### Problem: Compilation is very slow

**Symptoms:**
- pdflatex takes more than 1-2 minutes
- Computer becomes unresponsive

**Solutions:**

1. **Normal compilation time**
   - First compile after changes: 30-60 seconds
   - Subsequent compiles: 15-30 seconds
   - Full rebuild: 1-2 minutes

2. **If much slower:**
   - Close other applications
   - Check disk space
   - Restart computer

3. **Use draft mode for quick previews**
   ```latex
   \documentclass[draft]{book}
   ```
   This skips images and some formatting.

---

### Problem: PDF file is locked

**Symptoms:**
```
I can't write on file `main.pdf'.
```

**Solutions:**

1. **Close the PDF viewer**
   - Some viewers lock the file
   - Close the PDF before recompiling

2. **Use a viewer that doesn't lock**
   - SumatraPDF (Windows) auto-reloads
   - VS Code's LaTeX Workshop auto-reloads

3. **Delete and recompile**
   ```bash
   rm main.pdf
   pdflatex main.tex
   ```

---

## Claude Code Issues

### Problem: Claude Code doesn't recognize the skill

**Symptoms:**
- Claude doesn't follow the physics-text-to-tutorial workflow
- Skill patterns not applied

**Solutions:**

1. **Check skill location**
   - Should be at `.claude/skills/physics-text-to-tutorial/SKILL.md`
   - Path is relative to project root

2. **Check skill syntax**
   - Frontmatter must have correct format:
   ```markdown
   ---
   name: physics-text-to-tutorial
   description: ...
   ---
   ```

3. **Restart Claude Code**
   - Exit and restart the session

---

### Problem: Generated LaTeX has errors

**Symptoms:**
- Claude generates content but it won't compile
- Missing environments or packages

**Solutions:**

1. **Check for common issues**
   - Unmatched `\begin`/`\end`
   - Missing package imports
   - Incorrect environment names

2. **Provide feedback**
   - Tell Claude Code: "The generated LaTeX has an error on line X"
   - It can help fix the issue

3. **Manual fixes**
   - Sometimes small manual edits are fastest
   - See [Compilation Errors](#compilation-errors) for specific fixes

---

## Getting More Help

### Check the Log File

The most useful debugging tool is `main.log`:

```bash
# View the entire log
cat output/main.log

# Search for errors
grep "^!" output/main.log

# Search for warnings
grep "Warning" output/main.log

# Find undefined references
grep "undefined" output/main.log
```

### Online Resources

1. **TeX Stack Exchange**: https://tex.stackexchange.com/
   - Search for your error message
   - Usually someone has asked before

2. **LaTeX Wikibook**: https://en.wikibooks.org/wiki/LaTeX
   - Good for learning LaTeX basics

3. **Detexify**: https://detexify.kirelabs.org/
   - Draw a symbol, find the LaTeX command

### Still Stuck?

1. **Read the error message carefully**
   - Line numbers tell you where to look
   - Often the error describes the problem

2. **Simplify and isolate**
   - Comment out sections until it compiles
   - Add back one piece at a time
   - Find exactly what causes the error

3. **Start fresh**
   - Sometimes auxiliary files get corrupted
   - Delete all `.aux`, `.log`, `.out`, `.toc` files
   - Recompile from scratch

```bash
cd output
rm -f *.aux *.log *.out *.toc
pdflatex main.tex
pdflatex main.tex
```
