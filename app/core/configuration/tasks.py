from typing import Callable
from fastapi import FastAPI, BackgroundTasks
from app.core.configuration.redis import redis_cache_init

def create_start_app_handler(app: FastAPI) -> Callable:
    def start_app() -> None:
        redis_cache_init()
    return start_app


def create_stop_app_handler(app: FastAPI) -> Callable:
    def stop_app() -> None:
        return stop_app


