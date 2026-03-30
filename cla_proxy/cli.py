import uvicorn

from cla_proxy.config import Settings


def serve():
    settings = Settings()
    uvicorn.run(
        "cla_proxy.api:app",
        host=settings.server.host,
        port=settings.server.port,
        reload=settings.server.reload,
        workers=settings.server.workers,
        log_level=settings.logging.level.lower(),
    )
