import logging

from fastapi import Path


from app.models.user import User

from dotenv import load_dotenv
from psycopg2 import Error
from psycopg2.extras import RealDictCursor
import psycopg2

import os

from typing import (
    Final, 
    List
)

from datetime import datetime
import email

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy import (
    Column, 
    Integer, 
    String, 
    DateTime, 
    Boolean
)

logger = logging.getLogger(__name__)
logger.level = logger.setLevel(logging.INFO)
DATABASE_CONNECTION_ERROR: Final = "Error while connecting to PostgreSQL"
CLOSED_DATABASE_MESSAGE: Final = "PostgreSQL connection is closed"
CONNECTING_DB_MESSAGE: Final = "Connecting PostgreSQL database======"


class Database:
    def __init__(self):
        self.database_user = os.getenv("DATABASE_USER")
        self.database_password = os.getenv("DATABASE_PASSWORD")
        self.database_host = os.getenv("DATABASE_HOST")
        self.database_port = os.getenv("DATABASE_PORT")
        self.database_name = os.getenv("DATABASE_NAME")

    def get_engine(self):
        user = self.database_user
        password = self.database_password
        host = self.database_host
        port = self.database_port
        database = self.database_name
        url = f"postgresql://{user}:{password}@{host}:{port}/{database}"
        engine = create_engine(url)
        return engine

    def connect(self):
        try:
            engine = self.get_engine()
            self.connection = engine.connect() 
        except Exception as error:
            logging.error(DATABASE_CONNECTION_ERROR, error) 
        return

    def get_session(self):
        engine = self.get_engine()
        Session = sessionmaker(engine)
        session = Session()
        return session

    def disconnect(self):
        self.connection.close()
        logging.info(CLOSED_DATABASE_MESSAGE)
        return

    def get_all_active_users(self) -> List[RealDictCursor]:
        users = []
        self.connect()
        session = self.get_session()
        users = session.query(
            User.id, 
            User.username, 
            User.email, 
            User.created_at, 
            User.updated_at,
            User.is_active
        ).all()
        self.disconnect()
        return users

