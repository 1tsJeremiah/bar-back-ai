from fastapi import APIRouter

router = APIRouter()


@router.get("/api/health")
def api_health():
    return {"detail": "ok"}
