from fastapi import FastAPI

from back.api import router
from database.redis import get_redis_client
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(docs_url="/api/docs", redoc_url="/api/redoc", openapi_url="/api/openapi.json")
app.include_router(router)
redis = get_redis_client()

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["http://localhost:5173/*"],  # Frontend URL (or "*" for all origins)
#     allow_credentials=True,
#     allow_methods=["*"],  # Allow all methods
#     allow_headers=["*"],  # Allow all headers
# )
