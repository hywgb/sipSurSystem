from fastapi import FastAPI
from .core.config import settings
from .core.logging import setup_logging
from .routers import agents as agents_router
from .routers import conversations as convs_router

setup_logging()
app = FastAPI(title=settings.app_name, version=settings.app_version)

# Routers
app.include_router(agents_router.router)
app.include_router(convs_router.router)
from .routers import ai as ai_router
app.include_router(ai_router.router)


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.get("/version")
async def version():
    return {"name": settings.app_name, "version": settings.app_version}