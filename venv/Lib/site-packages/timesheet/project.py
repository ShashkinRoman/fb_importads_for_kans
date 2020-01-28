from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import MetaData
from sqlalchemy import String
from sqlalchemy import Table
from sqlalchemy import create_engine
from sqlalchemy import select
from tabulate import tabulate
from . import db


def add(project_name):
    ins = db.table_projects.insert().values(name=project_name)
    conn = db.engine.connect()
    conn.execute(ins)


def list():
    print("listing projet")
    select_st = select([db.table_projects.c.id, db.table_projects.c.name]).select_from(
        db.table_projects
    )
    conn = db.engine.connect()
    res = conn.execute(select_st)
    print(tabulate(res, headers=["id", "project name"]))
