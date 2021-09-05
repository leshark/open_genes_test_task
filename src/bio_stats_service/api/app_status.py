import os

from fastapi import APIRouter, HTTPException

status_router = APIRouter(prefix="/api", tags=["status"])


async def _ping_all():
    not_working_services = {}

    # ... ping all services here and add to not_working_services if they don't work

    return not_working_services


@status_router.get("/ping")
def ping():
    return "ok"


@status_router.get("/healthz")
async def check_health():
    not_working_services = await _ping_all()

    if not_working_services:
        raise HTTPException(status_code=500, detail=not_working_services)
    return "ok"


@status_router.get("/config")
def config():
    return {
        "app_version": os.getenv("APP_VERSION", default="DEV"),
        "commit": os.getenv("COMMIT", default="DEV"),
    }
