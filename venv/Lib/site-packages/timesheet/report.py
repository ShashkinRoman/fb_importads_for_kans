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
from datetime import datetime


now = datetime.now()


def print_entry(row):
    print(
        "[%s] -- [%s] => %s"
        % (row.time_start, row.time_end, row.time_end - row.time_start)
    )


def print_task_details(row):
    conn = db.engine.connect()
    print("#%s: %s" % (row.id, row.description))
    sql = select(
        [
            db.table_entries.c.id,
            db.table_entries.c.time_start,
            db.table_entries.c.time_end,
        ]
    ).where(db.table_entries.c.task_id == row.id)
    entries = conn.execute(sql)
    total = now
    for entry in entries:
        total = total + (entry.time_end - entry.time_start)
        print_entry(entry)
    print("Total: %s" % (total - now))


def project(project_id):
    conn = db.engine.connect()
    sql = select([db.table_projects.c.id, db.table_projects.c.name]).select_from(
        db.table_projects
    )
    res = conn.execute(sql)
    row = res.fetchone()
    print("== %s ==" % row.name)
    sql = select(
        [
            db.table_tasks.c.id,
            db.table_tasks.c.description,
            db.table_tasks.c.time_created,
            db.table_projects.c.name,
        ]
    ).where(db.table_tasks.c.project_id == project_id)
    res = conn.execute(sql)
    for row in res:
        print_task_details(row)
