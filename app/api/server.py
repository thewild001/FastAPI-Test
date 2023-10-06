from datetime import timedelta

from fastapi import FastAPI
from fastapi_redis_cache import cache

from app.core.configuration import config, swagger

# Initialize APP
app = config.get_application()

# SWAGGER UI CONFIG
app = swagger.init_swagger_ui()

# APP ROUTES
from app.api.routes import router as api_router
app.include_router(api_router)


@app.get("/")
@cache(expire=timedelta(minutes=5))
def get_data():
    return {"message": "Fonoma - Backend Developer Test!"}

    