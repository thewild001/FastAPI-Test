from fastapi import APIRouter

from app.api.routes.solution import router as solution_router

router = APIRouter()
router.include_router(solution_router, tags=["solution"])