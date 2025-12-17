# Team Meeting Minutes

## Meeting 1: Project Kick-off and Topic Selection
**Date:** 2024-09-12
**Attendees:** [Student 1], [Student 2], [Student 3]
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
* [Student 1]: Research which weather parameters are critical for aviation safety.
* [Student 2]: Setup the development environment.
* [Team]: Prepare the Project Proposal for the October deadline.

---

## Meeting 2: Proposal Finalization
**Date:** 2024-10-05
**Attendees:** All team members
**Duration:** 45 minutes

### Agenda
* Reviewing the Project Proposal document (1,000 words).
* Planning the code structure.

### Key Decisions
* **Scope Definition:** We will focus on 4 main variables: Wind speed, Rain intensity, Thunderstorm presence, and Visibility.
* **Risk Scoring System:** We decided to implement a point-based system.
    * Low score = Safe.
    * High score = Dangerous.
* **Submission:** Proposal is ready to be submitted before Oct 15th.

### Action Items
* [Team]: Submit the proposal on Moodle.
* [Student 3]: Start drafting the Python functions for the scoring logic.

---

## Meeting 3: Core Implementation
**Date:** 2024-11-10
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
* [Student 1]: Implement the input validation (ensure users type numbers, not text).
* [Student 2]: Add the "Seasonal Analysis" feature to compare risks across seasons.

---

## Meeting 4: Code Refactoring and Language Standardization
**Date:** 2024-12-05
**Attendees:** All team members
**Duration:** 1 hour

### Agenda
* Code review and cleanup.
* Preparing for the final submission.

### Key Decisions
* **Language Change:** The initial code was partly in French. We decided to translate the entire codebase (variables, comments, UI) into English to meet professional standards and module requirements.
* **Testing:** We tested the calculator with extreme values (e.g., 100km/h wind) to ensure the logic holds up.
* **GitHub:** We established the final folder structure (`src`, `docs`, `data`).

### Action Items
* [Team]: Push the final English version of `main.py` to GitHub.
* [Student 1]: Write the README file.

---

## Meeting 5: Final Portfolio & Presentation Prep
**Date:** 2025-17-12
**Attendees:** All team members
**Duration:** 2 hours

### Agenda
* Final check of deliverables against the Assessment Specification.
* Preparing the Viva presentation.

### Key Decisions
* **Portfolio:** The GitHub repository is public and organized.
* **Reflective Report:** Each member confirmed they are writing their individual 500-word report.
* **Presentation Strategy:** We will demonstrate the code running live during the Viva.

### Action Items
* [Team]: Submit the GitHub link to Moodle before Dec 27th.
* [Team]: Rehearse the presentation slides.
