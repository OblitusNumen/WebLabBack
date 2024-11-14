
from fastapi import FastAPI

from back.api import router
from database.redis import RedisDB, get_redis_client

app = FastAPI(docs_url="/api/docs", redoc_url="/api/redoc", openapi_url="/api/openapi.json")
app.include_router(router)
redis = get_redis_client()