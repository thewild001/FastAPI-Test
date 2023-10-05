import logging
from fastapi import Request, Response
from fastapi_redis_cache import FastApiRedisCache, cache
from app.core.configuration.settings import Settings

settings = Settings()

from fastapi_redis_cache.util import (
    ONE_DAY_IN_SECONDS,
    ONE_HOUR_IN_SECONDS,
    ONE_MONTH_IN_SECONDS,
    ONE_WEEK_IN_SECONDS,
    ONE_YEAR_IN_SECONDS,
)


logger = logging.getLogger(__name__)

REDIS_URL = settings.redis_url

def redis_cache_init():
    redis_cache = FastApiRedisCache()
    
    try:
        redis_cache.init(
            host_url= str(REDIS_URL),
            prefix="myapi-cache",
            response_header="X-MyAPI-Cache",
            ignore_arg_types=[Request, Response]
        )
        print('------ REDIS CACHE INITIALIZED SUCCESSFULL ------')
    except Exception as err:
        # do whatever you need
        print(err)
        logger.warn("--- REDIS CACHE ERROR ---")
        logger.warn(err)
        logger.warn("--- REDIS CACHE ERROR ---")
    