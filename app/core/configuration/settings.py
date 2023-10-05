import os

from pydantic import BaseSettings
#from dotenv import load_dotenv
#load_dotenv()

from fastapi.security import OAuth2PasswordBearer

class Settings(BaseSettings):

    project_name: str = os.getenv('PROJECT_NAME', default="Fonoma Backend Developer Test")
    project_desc: str = os.getenv('PROJECT_DESC', default="Fonoma Backend Developer Test")
    project_version: str = os.getenv('VERSION', default="1.0.0")
    api_prefix: str = os.getenv('API_PREFIX', default="/api/v1")
   
    redis_host: str = os.getenv('REDIS_HOST', default="localhost")
    redis_port: str = os.getenv('REDIS_PORT', default="6379")
    redis_url: str = os.getenv('REDIS_URL', default="redis://localhost:6379")
