from sqlalchemy import URL
from dotenv import load_dotenv
import os

load_dotenv()

DEBUG = os.environ.get("DEBUG", "True").lower() == "true"

APPLICATION_HOST = "localhost" if DEBUG else os.getenv("APPLICATION_HOST")
APPLICATION_PORT = os.getenv("APPLICATION_PORT")

SQLALCHEMYURL = URL.create(
    drivername="postgresql+asyncpg",
    host=os.getenv("DB_HOST", "localhost"),
    port=os.getenv("DB_PORT"),
    username=os.getenv("DB_USERNAME"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)
