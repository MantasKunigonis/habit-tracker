# Testing Strategy

## Test Types
- Unit Tests - test individual functions or classes.
- Integration Tests - test Flask API routes + DB.
- End-to-End Tests - full user flows (optional, later).

## Testing Frameworks
- pytest
- Flask-Testing
- SQLite in-memory

## Database Testing
- Use SQLite in-memory for isolated, fast tests.
- Mocks for external services like API calls.

## Folder Structure
/tests/
  test_auth.py
  test_habits.py
  test_api.py