from starlette.config import Config

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.docs import tags_metadata

from app.core.configuration import tasks
from app.core.configuration.settings import Settings

settings = Settings()

# config_env = Config(".env")

PROJECT_NAME = settings.project_name
PROJECT_DESC = settings.project_desc
VERSION = settings.project_version
API_PREFIX = settings.api_prefix

# Initialize APP
def get_application() -> FastAPI:
    
    app = FastAPI(docs_url=None, redoc_url=None,
        title=PROJECT_NAME,
        description=PROJECT_DESC,
        version=VERSION,
        openapi_tags=tags_metadata)
   
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.add_event_handler("startup", tasks.create_start_app_handler(app))
    app.add_event_handler("shutdown", tasks.create_stop_app_handler(app))
    

    return app
    
app = get_application()


