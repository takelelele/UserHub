import uvicorn
from litestar import Litestar
from routes.users import router as users_router

app = Litestar(route_handlers=[users_router])

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000
    )
