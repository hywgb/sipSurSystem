from fastapi import FastAPI

app = FastAPI(title="ITACATI Contact Center", version="0.1.0")


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.get("/version")
async def version():
    return {"name": "ITACATI Contact Center", "version": app.version}