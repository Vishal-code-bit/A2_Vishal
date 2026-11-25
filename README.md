# Progressive adaptive dashboard

**README prose word count:** 469 (headings and list text included; code blocks excluded).

## Project status

This is a working, standalone browser prototype for progressive mixed-initiative dashboard adaptation. It has four illustrative monitoring panels. Users can focus a panel, accept or reject a recommendation, retain preferences across sessions, allow a learned low-risk reordering, undo a change, pause automation or reset learning. All metrics are mock values. The adaptation policy is a deterministic rule-based simulation, not a trained machine-learning model. There is no live equipment connection, backend, API or production data.

## Technology stack

- HTML5, CSS3 and vanilla JavaScript for the interface and interaction logic.
- Browser `localStorage` for local preference history.
- ChatGPT for assistance with the initial code, report draft, diagrams, storyboards and test plan.

## Run or inspect

Open `prototype/index.html` in Chrome, Edge or Firefox. No installation, server, account or API key is required. Use `docs/demo-guide.md` to reproduce the three storyboards. Diagrams are in `docs/`; test results and screenshots are in `evidence/`. To rerun the optional Playwright smoke test, install `requirements-test.txt`, install Chromium with `python -m playwright install chromium`, then run `python evidence/test_prototype.py`.

## Development record

1. **Scope:** narrowed the A1 idea to one observable behaviour: moving a frequently focused panel to the top.
2. **Interface:** added four stable cards with a visible focus action and illustrative metrics.
3. **Adaptation:** added explained suggestions, accept/reject choices and preference retention across sessions.
4. **Control:** added undo, pause, reset and a new-session control; only layout position changes.
5. **Checking:** browser tests covered recommendation, acceptance, repeated acceptance, automatic reordering, undo, rejection and a 390-pixel mobile viewport. Screenshots and the test result are in `evidence/`.

## AI assistance and checking

ChatGPT helped draft the prototype, rationale, system diagram, storyboards and README. Browser interactions were tested for each main state, and the mobile layout was checked. References were checked against publisher or author records. The student must still compare terminology with the actual Week 1–4 lecture materials, review every claim, run the prototype locally and edit the report to reflect their own understanding and contribution.

## Report and submission

The assignment report is submitted separately from this repository. It should link to this public repository and to this `README.md`. The report is not included in this repository ZIP.

Before publishing, create a public GitHub repository and upload the contents of this folder. Replace the repository placeholder in your report with the real public URL and record the final commit hash or release tag.

Never commit passwords, personal access tokens or API keys.

## Project files

- `prototype/index.html` — interactive prototype.
- `docs/system-architecture.*` — system architecture diagram in PNG and editable SVG formats.
- `docs/interaction-storyboards.*` — three interaction storyboards in PNG and editable SVG formats.
- `docs/demo-guide.md` — reproducible walkthrough.
- `evidence/` — browser test record, test script and screenshots.
- `requirements-test.txt` — optional test dependency.
