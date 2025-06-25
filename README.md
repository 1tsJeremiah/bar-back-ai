# Bar-Back AI

Bar-Back AI analyzes bar inventory images and videos to generate insights. This project is structured for microservice deployment.

## Development

1. Copy `.env.example` to `.env` and set environment variables.
2. Run services with Docker Compose:
   ```bash
   docker-compose up --build
   ```
3. Run tests:
   ```bash
   pytest backend/tests
   ```

## Directory Structure

- `backend/` – FastAPI backend
- `frontend/` – React frontend
- `services/` – Placeholder ML services
- `.github/workflows/` – CI/CD pipelines

Future plans include integrating LLMs and ML models for automated analysis.
