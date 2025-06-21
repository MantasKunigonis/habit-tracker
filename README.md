# Habit Tracker
Track and build better habits with this app.

## Tech Stack: Flask + React (Next.js) + Bootstrap
- Backend: Flask
- Environment Management: python-dotenv + .env file
- Database: SQLite
- ORM: SQLAlchemy
- Auth: Flask-Login
- API Docs: Flask-RESTX
- Frontend: React (Next.js)
- Styling: Bootstrap
- Testing: pytest + Flask-Testing
- CI/CD: GitHub Actions
- Deployment: Docker

## Prerequisites
- Node.js ≥ 22.16
- Python ≥ 3.13
- SQLite ≥ 3.45
- .env file in backend/ (see [backend/.env.example](backend/.env.example))
- Git

## Setup
### Clone the repository
- git clone https://github.com/MantasKunigonis/habit-tracker.git
### Set up backend
- cd backend
- python -m venv .venv
#### If macOS/Linux
- source .venv/bin/activate
#### If Windows
- .venv\Scripts\activate
### Set up frontend
- cd ../frontend
- npm install

## Coding Standards
### Format
#### Backend
- cd ../backend
- black .
#### Frontend
- cd ../frontend
- TBD
### Lint
#### Backend
- cd ../backend
- flake8 .
#### Frontend
- cd ../frontend
- TBD
### Test
#### Backend
- cd ../backend
- pytest
#### Frontend
- cd ../frontend
- TBD

### Style Guides
- PEP8 style guide for Python.
- Airbnb style guide for React.

## Architecture
- Diagrams and project information are in [docs/architecture.md](docs/architecture.md).
- Decisions are documented in [docs/adr](docs/adr).

## Security
- Security guidelines are in [SECURITY.md](SECURITY.md).
- Private vulnerability reporting is enabled via GitHub.