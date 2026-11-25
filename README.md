
# Progressive Adaptive Dashboard

**README prose word count:** 606 (including headings and list text; excluding this word-count line).

## Project Status

This repository contains a single-page browser prototype exploring progressive, mixed-initiative adaptation in an operations dashboard. It displays four monitoring panels: Priority alerts, Equipment status, Throughput and Maintenance queue. All values are illustrative, not live data.

When a user focuses the same panel twice in one session, the prototype suggests moving it to the top. The user can accept or reject the suggestion. Accepted preferences are stored in the browser using `localStorage`. After the same change has been accepted twice, a later session can apply it automatically if low-risk automatic changes are enabled. The user can undo the latest change, pause automation or reset learning.

The adaptation is a deterministic, rule-based simulation, not a trained machine-learning model. There is no backend, external API, live equipment connection or real operational data. The sidebar entries for Equipment, Maintenance, Activity and Adaptive interface are visual labels only; they do not open separate pages. Starting a new session resets the panel order and focus counts for the demonstration but retains accepted preferences.

## Technology Stack

- **HTML5** for page structure.
- **CSS3** for layout and responsive styling.
- **Vanilla JavaScript** for interactions and adaptation rules.
- **Browser localStorage** for local preference history.

No external packages, server, API key or installation are needed.

## Run or Inspect

1. Download or clone this repository.
2. Open `prototype/index.html` in Chrome, Edge or Firefox.
3. Select **Reset learning** to start from a clean state.
4. Focus the same panel twice and accept the recommendation.
5. Start a new session and accept the same recommendation again. In the following session, focus that panel twice to see the automatic change.
6. Try rejecting a suggestion, undoing a change and switching automatic changes off.

Preference history is stored in the same browser profile. **Reset learning** clears it.

## Development Record

1. **Scope:** Focused on one demonstrable behaviour — moving a frequently focused panel to the top — instead of building a full operations application.

2. **Dashboard:** Added four panels with illustrative values and a focus button. This explicit action simulates user interest; the prototype does not track browsing in the background.

3. **Mixed initiative:** Two focus actions trigger an explained recommendation. The user can accept or reject it.

4. **Progressive automation:** Accepted choices are remembered. After two acceptances of the same change, a later session can apply it automatically when enabled.

5. **User control:** Added undo, pause and reset. Automatic adaptation changes panel order only, not the displayed information.

6. **Checks:** Checked recommendation, acceptance, rejection, repeated acceptance, automatic reordering, undo, pause, reset and the narrow-screen layout.

## AI Assistance

ChatGPT was used to generate and revise parts of the prototype code, explain the adaptation logic, and help prepare the report, system diagram, storyboards and README. The code and written claims were checked against the prototype's behaviour. The main interactions were checked in a browser. The report should also be checked against Week 1–4 lecture terminology and the student's own understanding. AI assistance is acknowledged here.

## Files

- `prototype/index.html` — interactive browser prototype.
- `docs/system-architecture.png` and `.svg` — system diagram.
- `docs/interaction-storyboards.png` and `.svg` — three illustrated scenarios.
- `docs/make_assets.py` — source script for the diagrams and storyboards.

The A2 report is submitted separately and contains the written explanation, diagrams, storyboards, references and links to this repository and README. No separate ZIP is needed for these repository files.

## Submission Version

Use the latest commit on `main` as the submitted version. After committing this README, copy the latest full commit SHA from GitHub into the A2 report. Update the SHA if you make further changes.

Never commit passwords, access tokens, API keys or private information.
