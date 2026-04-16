import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql+psycopg://postgres:Terraria12@127.0.0.1:5432/enfermeria_db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"client_encoding": "utf8"}
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)