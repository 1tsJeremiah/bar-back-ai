FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY app ./app
RUN useradd -U -u 1000 appuser && \
    chown -R 1000:1000 /app
USER 1000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
EXPOSE 80
