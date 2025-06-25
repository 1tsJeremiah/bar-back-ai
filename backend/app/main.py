from fastapi import FastAPI
from .api.routes import router as api_router

app = FastAPI(title="Bar-Back AI")

app.include_router(api_router)


@app.get("/health")
def health_check():
    return {"status": "ok"}
