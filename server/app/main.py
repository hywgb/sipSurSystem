from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .core.config import settings
from .core.logging import setup_logging
from .routers import agents as agents_router
from .routers import conversations as convs_router
from .routers import ai as ai_router

setup_logging()
app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    openapi_tags=[
        {"name": "agents", "description": "座席管理"},
        {"name": "conversations", "description": "会话/消息"},
        {"name": "ai", "description": "知识/摘要/质检（占位）"},
    ],
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # TODO: tighten in prod
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(agents_router.router)
app.include_router(convs_router.router)
app.include_router(ai_router.router)


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.get("/version")
async def version():
    return {"name": settings.app_name, "version": settings.app_version}