# User Guide

A complete, step-by-step guide to using the Physics Textbook to Tutorial Converter.

## Table of Contents

1. [Introduction](#introduction)
2. [System Requirements](#system-requirements)
3. [Installation](#installation)
4. [Viewing the Tutorial](#viewing-the-tutorial)
5. [Understanding the Tutorial Structure](#understanding-the-tutorial-structure)
6. [Navigating the PDF](#navigating-the-pdf)
7. [Using Source References](#using-source-references)
8. [Making Changes](#making-changes)
9. [Recompiling the PDF](#recompiling-the-pdf)
10. [Common Tasks](#common-tasks)

---

## Introduction

### What Is This Project?

This project transforms the condensed content from physics textbooks into expanded, detailed tutorials. Think of it as having a patient tutor who fills in all the gaps that textbooks leave out.

### What Problem Does It Solve?

Physics textbooks often assume you can fill in missing steps. Common phrases include:
- "The proof is left to the reader"
- "It is easy to show that..."
- "Clearly, we have..."

This project **fills in all those gaps** with complete, step-by-step explanations.

### Who Is This For?

- **Students** studying mathematical physics who want complete explanations
- **Self-learners** working through textbooks on their own
- **Educators** who want comprehensive teaching materials
- **Anyone** frustrated by "left to the reader" proofs

---

## System Requirements

### Minimum Requirements

| Requirement | Specification |
|-------------|---------------|
| Operating System | Windows 10/11, macOS 10.14+, or Linux |
| RAM | 4 GB minimum |
| Disk Space | 100 MB for this project |
| PDF Reader | Any (Adobe Reader, Preview, browser, etc.) |

### For Compiling Changes

If you want to modify the LaTeX source and regenerate the PDF:

| Requirement | Specification |
|-------------|---------------|
| LaTeX Distribution | MiKTeX, MacTeX, or TeX Live |
| Disk Space | 2-5 GB (for LaTeX distribution) |
| Terminal/Command Line | Basic familiarity helpful |

---

## Installation

### Step 1: Download the Project

**Option A: Download ZIP (Easiest)**
1. Download the project folder
2. Extract to a location like `C:\Users\YourName\Documents\byron_fuller`
3. Done!

**Option B: Clone with Git**
```bash
git clone <repository-url> byron_fuller
cd byron_fuller
```

### Step 2: Install a LaTeX Distribution (Optional)

Only needed if you want to compile changes. Skip if you just want to read the PDF.

#### Windows (MiKTeX)

1. **Download MiKTeX**
   - Go to https://miktex.org/download
   - Click "Download" for the Windows installer

2. **Run the Installer**
   - Double-click the downloaded `.exe` file
   - Click "Next" on the welcome screen
   - Accept the license agreement
   - Choose "Install for: Anyone who uses this computer" (recommended)
   - Keep the default installation folder
   - Click "Next" and then "Start"
   - Wait for installation (may take 10-20 minutes)

3. **Configure MiKTeX**
   - After installation, search for "MiKTeX Console" in the Start menu
   - Open it and let it check for updates
   - If prompted, allow it to install missing packages automatically
   - Close the console

4. **Verify Installation**
   - Open Command Prompt (search "cmd" in Start menu)
   - Type: `pdflatex --version`
   - You should see version information. If not, see Troubleshooting.

#### macOS (MacTeX)

1. **Install via Homebrew** (recommended)
   ```bash
   # Install Homebrew first if you don't have it
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

   # Install MacTeX
   brew install --cask mactex
   ```

2. **Or Download Directly**
   - Go to https://tug.org/mactex/
   - Download MacTeX.pkg (about 4 GB)
   - Double-click to install
   - Follow the installer prompts

3. **Verify Installation**
   ```bash
   pdflatex --version
   ```

#### Linux (TeX Live)

**Ubuntu/Debian:**
```bash
sudo apt-get update
sudo apt-get install texlive-full
```

**Fedora:**
```bash
sudo dnf install texlive-scheme-full
```

**Arch Linux:**
```bash
sudo pacman -S texlive-most
```

---

## Viewing the Tutorial

### Finding the PDF

The pre-compiled tutorial is located at:
```
output/main.pdf
```

Full path example:
- Windows: `C:\Users\YourName\Documents\byron_fuller\output\main.pdf`
- Mac/Linux: `/home/yourname/byron_fuller/output/main.pdf`

### Opening the PDF

**Windows:**
- Double-click `main.pdf` to open in your default PDF viewer
- Or right-click → Open with → Choose your preferred viewer

**macOS:**
- Double-click `main.pdf` to open in Preview
- Or right-click → Open With → Choose viewer

**Linux:**
- Double-click to open in your default viewer (Evince, Okular, etc.)
- Or from terminal: `evince output/main.pdf`

---

## Understanding the Tutorial Structure

### Document Organization

The tutorial is organized like a book:

1. **Title Page** - Project title and source information
2. **Table of Contents** - Clickable navigation (if your PDF reader supports it)
3. **Chapters** - Main content organized by topic
4. **Sections** - Subdivisions within chapters

### Visual Elements

The tutorial uses colored boxes to highlight different types of content:

#### Green Box: Intuition
```
┌─ Intuition ─────────────────────────────┐
│ The key insight is that...              │
│ This works because geometrically...     │
└─────────────────────────────────────────┘
```
Contains explanations of **why** something is true, often with geometric or physical interpretations.

#### Red Box: Warning
```
┌─ Warning ───────────────────────────────┐
│ A common mistake is to assume...        │
│ Be careful not to...                    │
└─────────────────────────────────────────┘
```
Highlights common errors and misconceptions to avoid.

#### Blue Box: Physical Interpretation
```
┌─ Physical Interpretation ───────────────┐
│ In physical terms, this means...        │
│ An example would be...                  │
└─────────────────────────────────────────┘
```
Connects mathematical results to real-world physics.

#### Purple Box: Key Step
```
┌─ Key Step ──────────────────────────────┐
│ The crucial step in this derivation...  │
│ This is where we use the identity...    │
└─────────────────────────────────────────┘
```
Highlights the most important steps in a derivation.

### Mathematical Environments

**Definitions** are numbered and titled:
```
Definition 1.3.1 (Scalar Product)
The scalar product of two vectors...
```

**Theorems** state important results:
```
Theorem 1.3.2 (Schwarz Inequality)
For any two vectors x and y...
```

**Proofs** follow theorems and show complete derivations:
```
Proof.
Step 1: We begin by...
Step 2: Applying the identity...
...
∎
```

### Margin Notes

Small italic text in the margins shows where content came from in the original textbook:
```
                                          B&F Ch. 1, p. 5
```
This helps you locate the corresponding content in Byron & Fuller's original book.

---

## Navigating the PDF

### Using the Table of Contents

1. Go to the Table of Contents (usually page 2-3)
2. If your PDF reader supports it, click on a section name
3. You'll jump directly to that section

### Using Bookmarks

Many PDF readers show a bookmark panel:

**Adobe Reader:**
- View → Show/Hide → Navigation Panes → Bookmarks
- Click on any bookmark to jump to that section

**Preview (macOS):**
- View → Table of Contents
- Click entries to navigate

**Evince (Linux):**
- Press F9 to show the side panel
- Select "Index" tab

### Using Cross-References

The tutorial contains clickable cross-references:
- "See Equation (1.23)" - Click to jump to that equation
- "As shown in Theorem 1.3.2" - Click to jump to that theorem
- "Refer to Section 1.5" - Click to jump to that section

### Searching

Use Ctrl+F (Windows/Linux) or Cmd+F (Mac) to search for specific terms.

---

## Using Source References

### What Are Source References?

Every theorem, definition, and proof in the tutorial includes a reference to where it appears in the original Byron & Fuller textbook.

### Reference Format

References appear in margin notes:
```
B&F §1.3, pp. 5-8
```

This means:
- **B&F** - Byron & Fuller textbook
- **§1.3** - Section 1.3
- **pp. 5-8** - Pages 5 through 8

### Why Source References Matter

1. **Verification**: Check the original if something seems unclear
2. **Context**: See how Byron & Fuller introduced the topic
3. **Additional Material**: The original may have exercises or examples not included here
4. **Academic Integrity**: Properly credits the source material

### Finding the Original Pages

The original textbook PDFs should be placed in the `docs/` folder (not included due to copyright - you must provide your own copy of Byron & Fuller's textbook).

To find "B&F p. 17":
1. Open your Byron & Fuller PDF in the `docs/` folder
2. Navigate to page 17

---

## Making Changes

### Can I Edit the Tutorial?

Yes! The tutorial is written in LaTeX, a document preparation system. You can:
- Fix typos
- Add your own notes
- Expand sections further
- Add new chapters

### Where Are the Source Files?

LaTeX source files are in the `output/` folder:
- `main.tex` - Master document that combines everything
- `chapters/` - Individual chapter files

### Basic LaTeX Editing

**To fix a typo:**
1. Open the relevant `.tex` file in any text editor
2. Find and fix the text
3. Save the file
4. Recompile (see next section)

**Example:**
If you find "teh" instead of "the":
1. Open `output/chapters/ch01_scalar_product.tex`
2. Use Find (Ctrl+F) to locate "teh"
3. Replace with "the"
4. Save the file
5. Recompile the PDF

---

## Recompiling the PDF

After making changes to any `.tex` file, you need to recompile to see changes in the PDF.

### Windows (Command Prompt)

1. **Open Command Prompt**
   - Press Win+R, type `cmd`, press Enter
   - Or search "Command Prompt" in Start menu

2. **Navigate to the output folder**
   ```cmd
   cd C:\Users\YourName\Documents\byron_fuller\output
   ```
   Replace `YourName` with your actual username.

3. **Run pdflatex twice**
   ```cmd
   "C:\Users\YourName\AppData\Local\Programs\MiKTeX\miktex\bin\x64\pdflatex.exe" -interaction=nonstopmode main.tex
   "C:\Users\YourName\AppData\Local\Programs\MiKTeX\miktex\bin\x64\pdflatex.exe" -interaction=nonstopmode main.tex
   ```

   **Why twice?** LaTeX needs two passes to resolve cross-references and the table of contents.

4. **Check for errors**
   - If you see "Output written on main.pdf" - success!
   - If you see errors, check Troubleshooting

### macOS/Linux (Terminal)

1. **Open Terminal**

2. **Navigate to the output folder**
   ```bash
   cd ~/byron_fuller/output
   ```

3. **Run pdflatex twice**
   ```bash
   pdflatex -interaction=nonstopmode main.tex
   pdflatex -interaction=nonstopmode main.tex
   ```

4. **View the updated PDF**
   ```bash
   open main.pdf    # macOS
   evince main.pdf  # Linux
   ```

### Using VS Code (All Platforms)

If you use Visual Studio Code:

1. Install the "LaTeX Workshop" extension
2. Open the `output` folder in VS Code
3. Open `main.tex`
4. Press Ctrl+Alt+B (or Cmd+Alt+B on Mac) to build
5. The PDF viewer will update automatically

---

## Common Tasks

### Task 1: Reading a Specific Section

1. Open `output/main.pdf`
2. Go to the Table of Contents
3. Click on the section you want

### Task 2: Finding the Original Textbook Content

1. Note the source reference (e.g., "B&F §1.5, p. 14")
2. Open your Byron & Fuller PDF in the `docs/` folder
3. Navigate to that page number

**Note:** Source PDFs are not included due to copyright. You must provide your own copy.

### Task 3: Printing the Tutorial

1. Open `output/main.pdf`
2. File → Print
3. Recommended settings:
   - Print on both sides (if available)
   - Use "Fit to page" for best results

### Task 4: Copying Equations

Most PDF readers let you copy text. For equations:
1. Some readers have a "Select" tool
2. Select the equation
3. Copy and paste

Note: Mathematical formatting may not preserve perfectly when pasting.

### Task 5: Adding a Personal Note

1. Open the relevant chapter file (e.g., `output/chapters/ch01_scalar_product.tex`)
2. Find the location where you want to add a note
3. Add your note like this:
   ```latex
   \begin{remark}
   My personal note: This reminds me of...
   \end{remark}
   ```
4. Save and recompile

---

## Getting Help

- **Something doesn't work?** See [Troubleshooting](TROUBLESHOOTING.md)
- **Want to learn LaTeX?** See [LaTeX Reference](LATEX_REFERENCE.md)
- **Want to understand the output files?** See [Output Files Explained](OUTPUT_FILES_EXPLAINED.md)
- **Want to add new content?** See [Developer Guide](DEVELOPER_GUIDE.md)
- **Quick examples?** See [Quick Start Guide](QUICK_START.md)
