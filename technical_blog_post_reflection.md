# From Ad Hoc Review to Auditable Math QA: Verifying 263 Physics Problem-Solution PDFs

I just completed a full audit workflow for a large set of textbook problem PDFs: 263 total files across chapters 1–10, where each PDF was self-contained (problem statement + original solution). The goal was strict: review each problem rigorously, produce per-problem critique artifacts, and generate complete revised solutions whenever the original was incomplete or incorrect, without modifying any source files.

## What I Delivered

I produced two levels of output:

1. **Per-problem critique reports (PDF):** one for every problem in chapters 2–10 (246 total), plus chapter 1 handled in its earlier pass.
2. **Revised solution PDFs:** only for flagged problems.

Final tally:
- **Total problems:** 263
- **Flagged and revised:** 51  
  - Chapter 1: 4 revised (1.4, 1.13, 1.16, 1.17)
  - Chapters 2–10: 47 revised
- **Accepted originals:** 212

I also generated reporting artifacts:
- Full status report (all problems)
- Concise flagged-only report
- Session transcript export in JSONL and formatted HTML

## How I Did It

The process became reliable once I treated it like a reproducible QA pipeline instead of a one-off reading task.

### 1) Deterministic queue + strict status model
I processed files in chapter/problem order with a single status taxonomy:
- `manually_verified_accept`
- `manually_verified_incomplete`
- `manually_verified_incorrect`

This removed ambiguity and guaranteed no file was skipped.

### 2) Auditable progress tracking
I maintained three live artifacts:
- `manual_review_progress_ch02_ch10.csv` (per-problem source of truth)
- `manual_review_live_status.txt` (current pointer + counters)
- `manual_review_activity.log` (append-only timeline)

This made progress externally inspectable at any time.

### 3) Repeatable report generation
I used a script (`chapter_audit/update_review.py`) to atomically:
- Update CSV row status
- Advance next problem to `in_progress`
- Refresh live status/log
- Regenerate the critique PDF for that problem via LaTeX (`tectonic`)

That gave me one command path per verdict and reduced manual drift.

### 4) Manual mathematical verification protocol
For each PDF:
- Read problem and original solution from extracted text
- Check derivation logic line-by-line
- Validate algebra/signs/transformations and theorem usage
- Confirm the final result matches the argument
- Record concise technical note

If flagged:
- Write a full revised derivation/proof in LaTeX
- Add a structured comment section: what was wrong, why it matters, how the revision fixes it
- Compile to `*_revised.pdf`

## Engineering Details That Helped

- **Separation of outputs** (`review_reports_ch02_ch10/` vs `revised_ch02_ch10/`) made artifact checks trivial.
- **Coverage audit scripts** at the end validated:
  - 246/246 in chapters 2–10 reviewed
  - no lingering `in_progress`
  - critique PDF exists for every reviewed file
  - every non-accept row has a revised PDF
- **Transcript export** into HTML made the workflow and tool activity reviewable for stakeholders.

## What I Could Have Done Better

If I repeated this project, I would improve four things:

1. **Earlier end-to-end pipeline hardening**
   I initially relied on broad script batches and later had to adjust for shell timeout behavior. Next time I’d start with smaller chunking and retry logic from the beginning.

2. **Cleaner text ingestion quality controls**
   Some extracted text had encoding artifacts. I handled them during review, but a pre-clean normalization pass would reduce friction and lower cognitive load.

3. **Richer status schema from day one**
   A single `notes` field works, but adding explicit columns for “error type” (algebraic, conceptual, incomplete derivation, basis mismatch, etc.) would improve downstream analytics.

4. **Automated invariant checks for revised files**
   I validated consistency manually and by file existence checks. I’d add a formal post-build validator that cross-references flagged IDs against revised filenames and checks compile logs for warnings/errors systematically.

## Closing Reflection

The most important lesson: for large mathematical review tasks, **process architecture is as important as mathematical skill**. Once the workflow became deterministic, logged, and artifact-driven, rigor became sustainable. The work shifted from “Did I check this?” to “Can I prove I checked this?” That distinction is what made a 263-problem audit manageable and credible.
