from fastapi import APIRouter

router = APIRouter()

from . import routes  # noqa: E402
router.include_router(routes.router)
