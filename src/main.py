import uvicorn
from litestar import Litestar
from litestar.openapi import OpenAPIConfig

from routes.users import router as users_router
from userhub import settings

app = Litestar(
    route_handlers=[users_router],
    openapi_config=OpenAPIConfig(
        title="UserHub API",
        version="1.0.0",
        use_handler_docstrings=True,
    ),
    debug=settings.DEBUG,
)

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.APPLICATION_HOST,
        port=8000
    )
