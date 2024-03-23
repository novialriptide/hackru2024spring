from dotenv import load_dotenv
import os

load_dotenv("./.env")

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY")
    DATABASE_NAME = os.getenv("DATABASE_NAME")
    DATABASE_PORT = os.getenv("DATABASE_PORT")
    HOSTNAME = os.getenv("HOSTNAME")
    MONGO_URI = f"mongodb://{HOSTNAME}:{DATABASE_PORT}/"
    RUN_DEBUG_MODE = os.getenv("RUN_DEBUG_MODE") == "True"