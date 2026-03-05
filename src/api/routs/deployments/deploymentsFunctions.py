import datetime
import uuid

import sqlalchemy as db
from pymongo import MongoClient
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, session

from src.api.routs.deployments.postgres_row import DeploymentRow


def create_new_deployment_postgres():
    engine = create_engine("postgresql://origa:password@localhost/postgres", echo=True)
    meta = MetaData()
    new_table = db.Table("deployment", meta, db.Column('id', db.String, primary_key=True),
                         db.Column('db_name', db.String),
                         db.Column('status', db.String),
                         db.Column('username', db.String),
                         db.Column('creation_time', db.DateTime, server_default=db.func.now(), onupdate=db.func.now(),
                                   nullable=False))
    meta.create_all(engine)

def IsNameOk(db_name: str,username: str) -> bool:
    if db_name.startswith(username) and len(username) >= 3:
        return True
    else:
        return False

def create_new_deployment_mongo(db_name: str):
    client = MongoClient("mongodb://admin:123456@localhost:27017/?authSource=admin")
    new_db = client[db_name]
    new_db = new_db.create_collection("main")


def add_new_row_to_deployment(db_name: str, username: str,) -> str:
    engine = create_engine("postgresql://origa:password@localhost/postgres", echo=True)
    table_id = str(uuid.uuid4())
    row = DeploymentRow(id=table_id, db_name=db_name, status="CREATED" ,username=username ,creation_time=datetime.datetime.now())
    Session = sessionmaker(bind=engine)
    session = Session()
    session.add(row)
    session.commit()
    return table_id






