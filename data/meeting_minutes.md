# Team Meeting Minutes

## Meeting 1: Project Kick-off and Topic Selection
**Date:** 2025-02-11
**Attendees:** [Matthieu], [Raphael B], [Paul], [Lucas B]
**Duration:** 1 hour

### Agenda
* Brainstorming ideas for the AI project.
* Selecting the main topic.
* Defining initial roles.

### Key Decisions
* **Topic Chosen:** "Flight Risk Calculator based on Weather Conditions".
* **Rationale:** We want to build a tool that helps pilots or flight controllers make quick decisions based on multiple variables (wind, rain, visibility).
* **Programming Language:** Python (simple and effective for logic implementation).

### Action Items
* [Raphael B]: Research which weather parameters are critical for aviation safety.
* [Matthieu]: Setup the development environment.
* [Team]: Prepare the Project Proposal.

---

## Meeting 2: Proposal Finalization
**Date:** 2025-04-11
**Attendees:** All team members
**Duration:** 45 minutes

### Agenda.
* Planning the code structure.

### Key Decisions
* **Scope Definition:** We will focus on 4 main variables: Wind speed, Rain intensity, Thunderstorm presence, and Visibility.
* **Risk Scoring System:** We decided to implement a point-based system.
    * Low score = Safe.
    * High score = Dangerous.

### Action Items
* [Matthieu]: Start drafting the Python functions for the scoring logic.

---

## Meeting 3: Core Implementation
**Date:** 2025-09-11
**Attendees:** All team members
**Duration:** 1.5 hours

### Agenda
* Reviewing the first version of the code.
* Discussion on data storage.

### Discussion
* The initial `calculate_risk` function works well, but we need to calibrate the thresholds (e.g., is 40km/h wind dangerous?).
* **Issue:** How to store data?
* **Solution:** For this prototype, we will use a Python dictionary (`dict`) to store data in memory during the session.

### Action Items
* [Lucas]: Implement the input validation (ensure users type numbers, not text).
* [Paul]: Add the "Seasonal Analysis" feature to compare risks across seasons.

---

## Meeting 4: Code Refactoring and Language Standardization
**Date:** 2025-23-11
**Attendees:** All team members
**Duration:** 1 hour

### Agenda
* Code review and cleanup.

### Key Decisions
* **Language Change:** The initial code was partly in French. We decided to translate the entire codebase (variables, comments, UI) into English to meet professional standards and module requirements.
* **Testing:** We tested the calculator with extreme values (e.g., 100km/h wind) to ensure the logic holds up.
* **GitHub:** We established the final folder structure (`src`, `docs`, `data`).

### Action Items
* [Team]: Push the final English version of `main.py` to GitHub.
* [Lucas]: Write the README file.

---

## Meeting 5: Final Portfolio & Presentation Prep
**Date:** 2025-07-12
**Attendees:** All team members
**Duration:** 2 hours

### Agenda
* Final check of deliverables against the Assessment Specification.
* Preparing the presentation.

### Key Decisions
* **Portfolio:** The GitHub repository is public and organized.
* **Presentation Strategy:** We will demonstrate the code running live during the presentation.

### Action Items
* [Team]: Submit the GitHub link to Moodle before Dec 19th.
* [Team]: Rehearse the presentation slides.
