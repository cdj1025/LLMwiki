# LLM Wiki — Setup Guide (Journal Club)

This is a personal paper-wiki system you'll use for JC this semester. Every paper you present
(or read) gets turned into a structured, cross-referenced markdown page that Claude Code can
answer questions from — grounded only in papers you've actually added, never web search.

The rules Claude follows live in [`CLAUDE.md`](CLAUDE.md) — read it once, you don't need to
touch it.

## 1. Install Claude Code

Follow the official install instructions: https://docs.claude.com/en/docs/claude-code
(requires a Claude account/API access — check with the instructor if you don't have one yet).

## 2. Install Python + pypdf

You need Python 3.9+ on your machine. Then, from this folder:

```bash
pip install -r requirements.txt
```

## 3. Get your own copy of this repo

Click **"Use this template"** on the GitHub repo page (or `git clone` your fork), then clone it
to your machine:

```bash
git clone <your-repo-url>
cd LLMwiki
```

## 4. Open it with Claude Code

```bash
claude
```

Run this from inside the repo folder — Claude Code will automatically pick up `CLAUDE.md` and
follow its rules for this project.

## 5. Add your first paper

1. Copy the PDF into `papers/` (name it `{author}-{year}-{first-5-title-words}.pdf`).
2. Ask Claude: *"Add papers/{filename}.pdf to the wiki."* It will extract the text, write a
   summary in `sources/`, write a wiki page in `wiki/{category}/`, and update `index.md`.
3. Check the generated page — fix anything Claude got wrong before your JC presentation.

## 6. Browsing visually (optional)

Install [Obsidian](https://obsidian.md/) (free) and open this folder as a Vault to get graph
view, `[[wikilinks]]`, and full-text search over your wiki.

## Notes

- **Don't commit PDFs.** `.gitignore` already excludes `papers/*.pdf` — most JC papers are
  copyrighted journal articles, so keep them local-only. Only the markdown you and Claude write
  in `sources/` and `wiki/` gets pushed to GitHub.
- Everything in `wiki/` and `sources/` should be in **English**, even if you discuss in Korean
  with Claude.
- The wiki only knows what you've added. If Claude says it doesn't have a paper on something,
  that's the system working correctly — add the PDF rather than asking it to guess.
