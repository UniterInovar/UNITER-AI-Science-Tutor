# AI Science Tutor

AI-Science-Tutor is an education assistant that generates lessons, explanations, and practice questions for science topics.

This repository contains the backend AI services, content, and frontend UI used by the project.

---

## Author

Timothy Chile

## Brand

UniterInovar

## GitHub

UniterInovar

## Email

Unitercode9@gmail.com

## License

MIT

## Python Version

3.11

---

## Quickstart (backend)

1. Open a PowerShell terminal and change to the project root:

   Set-Location "C:\\UNITER\\Projects\\UNITER-AI-Science-Tutor"

2. Create and activate the virtual environment (if not already present):

   python -m venv .venv
   .\.venv\Scripts\Activate.ps1

3. Install runtime dependencies:

   .\.venv\Scripts\pip.exe install -r requirements.txt

4. Running the simple tests / examples

   The project includes small test scripts under backend/tests which are runnable directly. Run them from the project root so imports resolve and force UTF-8 console output to avoid encoding errors:

   $env:PYTHONPATH = (Get-Location).Path
   $env:PYTHONIOENCODING = 'utf-8'
   .\.venv\Scripts\python.exe .\backend\tests\test_topic_matcher.py
   .\.venv\Scripts\python.exe .\backend\tests\test_tutor.py

   These scripts print example outputs (topic matching and a tutor response).

5. Run the backend server (development)

   From the project root:
   .\.venv\Scripts\python.exe .\backend\main.py

   (Adjust host/port in backend/main.py or via environment variables if required.)

---

## Frontend

1. Change into the frontend folder and install Node deps (requires Node.js/npm):

   Set-Location .\frontend
   npm install
   npm run dev

2. The frontend runs separately from the backend and communicates with the API endpoints exposed by the backend.

---

## Packaging / Release

- Create a zip or artifact of the repository for release. Consider adding a CI workflow to build and publish artifacts.

---

## Contributing

- Run the backend test scripts as shown above when making changes.
- Add unit tests under backend/tests and ensure imports work by running from the project root or via pytest with PYTHONPATH set.

---

Generated using **UNITER Project Generator v3.5.0**
