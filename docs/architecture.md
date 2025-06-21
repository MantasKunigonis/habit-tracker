## Overview
### Purpose
Help users build consistent habits through tracking and feedback.
### User Personas
- A "Solo Habit Tracker" who wants to track habits like meditation, reading, or workouts.
- An "Accountability Seeker" who wants reminders and to visualize progress.
- A "Goal-Oriented Pro" who tracks performance and reviews past data.
### Use Cases
- Register/login/logout user.
- Create/edit/delete habits.
- Mark completion of habits.
- View progress for habits.
- Set reminders.
### Goal
- User can create and track habits.
- App is user friendly.
- UI is mobile friendly.
- App is deployed via Docker container with GitHub CI/CD.

## Architecture Layers
- UI -> API -> Business Logic -> Data Layer
- UI: Next.js components that the user interacts with.
- API: Flask-RESTX endpoints.
- Business Logic: Creation, editing, and tracking of habits.
- Data Layer: SQLAlchemy models and SQLite.

## Architecture Diagrams
### Context Diagram
- User -> Frontend
- Frontend -> Backend
- Backend -> Database
- GitHub Actions -> Application
- Docker -> Application
### Component Diagram
Frontend: pages -> Backend: Flask API (RESTX), Authorization (Flask-Login), Database layer (SQLAlchemy models), Config (python-dotenv) -> Database: SQLite (tables: users and habits) -> CI/CD: GitHub Actions (lint and test), Docker (deploy)

## Deployment Overview
- Docker Compose and .env for config for local development.
- Docker image and GitHub Actions for production.