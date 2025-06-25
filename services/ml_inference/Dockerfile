# Placeholder Dockerfile for ML inference service
FROM python:3.11-slim
WORKDIR /app
COPY . .
CMD ["python", "-m", "http.server", "8080"]
EXPOSE 8080
RUN useradd -U -u 1000 appuser && \
    chown -R 1000:1000 /app
USER 1000
