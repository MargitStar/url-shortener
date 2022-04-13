import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def get_env_vars():
    return (
        os.environ.get("URL_SHORTENER_DB_USER"),
        os.environ.get("URL_SHORTENER_DB_PASSWORD"),
        os.environ.get("URL_SHORTENER_DB_HOST"),
        os.environ.get("URL_SHORTENER_DB_NAME"),
    )


def create_engine_psql():
    env_vars_tuple = get_env_vars()
    return create_engine(
        f"postgresql+psycopg2://{env_vars_tuple[0]}:{env_vars_tuple[1]}@{env_vars_tuple[2]}/{env_vars_tuple[3]}"
    )


def create_session():
    engine = create_engine_psql()
    return sessionmaker(bind=engine)()
