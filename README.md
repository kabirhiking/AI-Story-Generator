# AI Story Generator Backend

This project is the backend service for the AI Story Generator application. It provides APIs for generating, storing, and managing AI-generated stories.

## Features

- Generate stories using AI models
- Save and retrieve generated stories
- User authentication and management
- RESTful API endpoints

## Technologies Used

## AI Story Generator — Backend

This repository contains the backend API for the AI Story Generator application. It provides endpoints to create, store, and retrieve generated stories and manages background jobs that call an LLM to produce story content.

The backend is written in Python using FastAPI and uses SQLAlchemy for persistence. The repository includes a small local SQLite/Postgres wiring (configurable via environment variables) and a minimal story generator integration that calls an LLM provider.

---

## Quick start (local, Windows / PowerShell)

1. Open a PowerShell terminal and change to the Backend folder:

```powershell
cd "E:\MY Drive\AI Story Generator\Backend"
```

2. Create and activate the virtual environment (the project expects `.venv`):

```powershell
python -m venv .venv
. .venv\Scripts\Activate.ps1
```

3. Install runtime dependencies:

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
# or install minimal set:
python -m pip install fastapi "uvicorn[standard]" sqlalchemy pydantic-settings langchain-openai
```

4. Configure environment variables:

- Copy `Backend/.env.example` (or create `Backend/.env`) and set the required keys. Important variables:
  - `DATABASE_URL` — SQLAlchemy database URL (e.g., `sqlite:///./database.db` or a Postgres URL)
  - `OPENAI_API_KEY` — your OpenAI API key (do NOT commit this file)

```powershell
copy .env.example .env
# edit Backend\.env and set OPENAI_API_KEY
```

5. Create DB tables and run the app:

```powershell
python -c "from db.database import create_tables; create_tables()"
python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

Open `http://localhost:8000/docs` for the interactive Swagger UI.

---

## Project layout

- `main.py` — FastAPI app entry point
- `core/` — configuration, prompts, and story generation logic
- `db/` — database setup and helpers
- `models/` — SQLAlchemy models (Story, StoryNode, StoryJob)
- `routers/` — API routes for stories and jobs
- `schemas/` — Pydantic request/response schemas

---

## Environment & secrets

- Never commit `.env` or secrets to Git. This repo includes `Backend/.gitignore` and `.env` is ignored. If a secret was accidentally committed, rotate the key immediately and remove it from history (see Troubleshooting below).
- Use environment variables or a secrets manager for production deployments.

---

## Troubleshooting

- "ModuleNotFoundError: No module named 'fastapi'": activate `.venv` and run `pip install fastapi uvicorn[standard]`.
- Pydantic v2: `BaseSettings` moved to `pydantic-settings`. Install with `pip install pydantic-settings` and import `BaseSettings` from `pydantic_settings`.
- Git push rejected due to secret scanning: if you accidentally committed a key, rotate it immediately and remove it from the repo history (use `git filter-repo` or BFG). See GitHub docs for push-protection.
- If `uvicorn` reports "Could not import module 'main'", make sure you run it from the `Backend` folder (or use `Backend.main:app` from repo root) and that the venv interpreter is active.

---

## Development notes

- Use `Backend/.venv` for local development; select it as the interpreter in VS Code.
- Add a `.env.example` file (no secrets) listing required variables.

---

If you want, I can also:
- add `requirements.txt` or `pyproject.toml` with pinned deps,
- create a `.env.example` file and a short CONTRIBUTING.md,
- or implement CI that blocks secret commits.

License: MIT
