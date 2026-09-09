# LLM Wiki — Journal Club Paper Wiki

A personal/lab knowledge base of papers, following [Karpathy's LLM Wiki pattern](https://gist.github.com/karpathy/1dd0294ef9567971c1e4348a90d69285):

```
Original PDF → sources/*.md (LLM summary) → wiki/{category}/*.md (final page)
```

**Language policy**: All wiki content is in English. Conversation can be in any language.

---

## THE FOUR RULES (do not violate)

These rules are the core of the system. They prevent hallucination and keep every claim traceable.

1. **No web search.** Never use `WebSearch` or `WebFetch` to fill gaps. The point of this wiki is that every answer is grounded in papers we actually have.
2. **Answer from the wiki first.** Use `sources/` and `wiki/` as the only sources of truth.
3. **If the wiki is insufficient, re-read the PDF.** Go to `papers/{author}-{year}-{words}.pdf` and extract more detail with `pypdf`. Then update the wiki.
4. **If the wiki has no paper on the topic, say so.** Tell the user *"I don't have a paper on this — please give me the PDF."* Do not improvise.

These rules apply to **every** response, including overview pages: cite only papers that exist in the wiki.

---

## Repository Structure

```
LLMwiki/
├── CLAUDE.md               # This file
├── index.md                # Page catalog
├── papers/                 # Original PDFs (cp, never symlink) — your own JC papers go here
│   └── {author}-{year}-{title-5-words}.pdf
├── sources/                # PDF summaries (English)
│   └── {author}-{year}-{title-5-words}.md
└── wiki/                   # Wiki pages (English)
    ├── neural-development/ # Neurogenesis, cortical development, progenitors
    ├── transcriptomics/    # scRNA-seq, bulk RNA-seq, spatial transcriptomics
    ├── cell-types/         # Cell type atlases, classification, brain cell types
    ├── epigenomics/        # Chromatin, ATAC-seq, methylation, histone mods
    ├── circuit-neuroscience/ # Synapses, connectivity, electrophysiology
    ├── disease/            # Neurodevelopmental disorders, ASD, SCZ, epilepsy
    ├── methods/            # Computational tools, pipelines, algorithms
    ├── concepts/           # Key concepts and theoretical frameworks
    └── overviews/          # Synthesis pages (where compounding happens)
```

> Add your own category folders under `wiki/` if your JC paper doesn't fit these
> (e.g. a gene- or system-specific folder like `wiki/MyGene/`). Keep the same
> three-tier pattern (PDF → source → wiki page) for anything you add.

## File Naming Convention

All three tiers (PDF, source, wiki) share the same stem:

```
{first-author-lastname}-{year}-{first-5-title-words}.{ext}
```

- Lowercase, special chars stripped, spaces → `-`
- Year is 4 digits
- Consortium papers: use consortium name (e.g. `allen-brain-atlas-2014-...`)

Example: `nowakowski-2017-spatiotemporal-gene-expression-trajectories.pdf`

## Categories

| Category | Includes |
|---|---|
| `neural-development` | Neurogenesis, cortical layering, progenitor cells, brain organoids, axon guidance, synaptogenesis |
| `transcriptomics` | scRNA-seq, bulk RNA-seq, spatial transcriptomics (Visium, MERFISH, etc.), multi-omics |
| `cell-types` | Cell type classification, brain cell atlases, marker genes, taxonomy |
| `epigenomics` | Chromatin accessibility (ATAC-seq), DNA methylation, histone modifications, 3D genome |
| `circuit-neuroscience` | Synaptic biology, neural connectivity, electrophysiology, functional imaging |
| `disease` | ASD, schizophrenia, epilepsy, intellectual disability, other neurodevelopmental disorders |
| `methods` | Computational tools, bioinformatics pipelines, statistical methods, ML for genomics |
| `concepts` | Key methods and algorithms explained generically (e.g., trajectory inference, batch correction) |
| `overviews` | Synthesis pages spanning multiple papers |

Tip: classify by **method or biological process**, not phenotype. A scRNA-seq paper studying ASD goes to `transcriptomics`, not `disease`.

---

## Adding a New Paper

### Step 1 — Copy PDF to `papers/` and extract text

Use `pypdf` (pure Python, no Java required). Run from the repo root:

```bash
python extract_pdf.py "papers/{stem}.pdf"
```

This prints the first ~12,000 characters of extracted text to the terminal so an LLM summary can be written from it.

### Step 2 — Write `sources/{stem}.md`

```yaml
---
title: "Paper Title"
authors: Author List
year: YYYY
doi: DOI
category: [category]
pdf_path: papers/{stem}.pdf
pdf_filename: {stem}.pdf
source_collection: external
---

## One-line Summary
## 1. Document Information
## 2. Key Contributions
## 3. Methodology and Architecture
## 4. Key Results and Benchmarks
## 5. Limitations and Future Work
## 6. Related Work
## 7. Glossary
```

### Step 3 — Write `wiki/{category}/{stem}.md`

```yaml
---
title: "Paper Title"
authors: Author list
year: YYYY
doi: DOI
source: {stem}.md
category: [category]
pdf_path: papers/{stem}.pdf
pdf_filename: {stem}.pdf
source_collection: external
tags: []
---

## Summary
## Key Contributions
## Methodology and Architecture
## Results
## Related Papers
- [[category/page]] — relationship
```

### Step 4 — Update `index.md`

Add a one-line entry under the right category.

---

## PDF Management Rules

- **Always copy, never symlink.** Copy PDFs from wherever you downloaded them into `papers/`.
- `pdf_path` always points inside `papers/`. Never use `~/Downloads/` or other external paths.
- `pdf_filename` must match `basename(pdf_path)`.
- Do not commit/share PDFs you don't have redistribution rights for beyond your own use — this repo is for your own study, not public redistribution of copyrighted articles.

## Knowledge Compounding

The most valuable pages are not individual paper summaries — they are `wiki/overviews/` pages that synthesize across papers. When a question is answered well, save the answer:

> "Save this as an overview page in `wiki/overviews/`"

Each conversation should produce a handful of new or updated wiki pages. Over time the wiki becomes a searchable, cross-referenced knowledge graph you can draw from for JC presentations and comps.

## Browsing with Obsidian

For visual navigation, install [Obsidian](https://obsidian.md/) (free, native app) and open this folder as a Vault. Native support for `[[wikilinks]]`, graph view, and full-text search. Recommended whenever you want to read or browse the wiki — Obsidian only reads files, so it does not interfere with Claude's edits.

---

## Design Principles

- **3-tier**: Raw PDF (immutable) → sources/*.md → wiki/**/*.md
- **English only** in wiki content (RAG-friendly)
- **Obsidian compatible**: `[[wikilinks]]`, plain markdown
- **Consistent YAML**: every file has title, authors, year, doi, category, pdf_path, pdf_filename, source_collection
- **No web search**: rule #1 above

When in doubt, follow rule #1.
