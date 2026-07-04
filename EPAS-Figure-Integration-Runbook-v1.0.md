# EPAS Figure Integration Runbook v1.0

**Purpose:** Replace EPAS v2.0 publication-draft diagram placeholders with Markdown image references to the accepted final controlled PNG figure set.

## Preconditions

The final PNG files must exist in:

`figures/png/`

The manuscript to update is:

`EdgePlatformArchitectureSpecification-v2.0-publication-draft.md`

The integration script is:

`tools/integrate_final_figures.py`

## Run from Codespaces

From the repository root:

```bash
git pull
python tools/integrate_final_figures.py
```

Then review the changed manuscript:

```bash
git diff EdgePlatformArchitectureSpecification-v2.0-publication-draft.md
```

Expected result: each `Diagram Placeholder` block under Figures 1 through 19 is replaced by a Markdown image reference such as:

```markdown
![Figure 1 — Edge Platform Context Model](figures/png/figure-01-edge-platform-context-model.png)
```

Existing captions should remain in place.

## Commit

```bash
git add EdgePlatformArchitectureSpecification-v2.0-publication-draft.md
git commit -m "docs(epas): integrate final figure references"
git push
```

## Verification

After committing, verify that no diagram placeholders remain:

```bash
grep -n "Diagram Placeholder" EdgePlatformArchitectureSpecification-v2.0-publication-draft.md
```

No output means the placeholders have been removed.

Verify figure references:

```bash
grep -n "figures/png/figure-" EdgePlatformArchitectureSpecification-v2.0-publication-draft.md
```

Expected count: 19.
