from sqlalchemy import func
from sqlalchemy import and_
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import select
from tabulate import tabulate
from . import db
from sqlalchemy.orm import sessionmaker


def add(project_id, task_name):
    conn = db.engine.connect()
    ins = db.table_tasks.insert().values(
        description=task_name, project_id=project_id, time_created=func.now()
    )
    conn.execute(ins)


def list(project_id):
    conn = db.engine.connect()
    join_obj = db.table_tasks.join(
        db.table_projects, db.table_projects.c.id == db.table_tasks.c.project_id
    )
    select_st = (
        select(
            [
                db.table_tasks.c.id,
                db.table_tasks.c.description,
                db.table_tasks.c.time_created,
                db.table_projects.c.name,
            ]
        )
        .where(db.table_tasks.c.project_id == project_id)
        .select_from(join_obj)
    )
    res = conn.execute(select_st)
    print(tabulate(res, headers=["id", "task name", "created", "project name"]))


def start(task_id):
    conn = db.engine.connect()
    sql = db.table_entries.insert().values(
        task_id=task_id, time_start=func.now(), active=True
    )
    conn.execute(sql)


def end(task_id):
    conn = db.engine.connect()
    stmt = (
        db.table_entries.update()
        .where(
            and_(
                db.table_entries.c.task_id == task_id, db.table_entries.c.active == True
            )
        )
        .values(active=False, time_end=func.now())
    )
    res = conn.execute(stmt)
    print(res)
