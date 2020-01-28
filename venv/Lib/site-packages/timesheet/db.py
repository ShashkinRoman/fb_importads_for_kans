import os
from xdg import (
    XDG_CACHE_HOME,
    XDG_CONFIG_DIRS,
    XDG_CONFIG_HOME,
    XDG_DATA_DIRS,
    XDG_DATA_HOME,
    XDG_RUNTIME_DIR,
)
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import Integer, String, DateTime, Boolean

APPCONFIG_DIR = os.path.join(XDG_DATA_HOME, "timesheet")
if not os.path.isdir(APPCONFIG_DIR):
    os.makedirs(APPCONFIG_DIR)
path_to_db = os.path.join(APPCONFIG_DIR, "db.sqlite")
db_uri = "sqlite:///%s" % path_to_db
engine = create_engine(db_uri)
metadata = MetaData(engine)

table_projects = Table(
    "projects",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String),
    Column("time_created", DateTime),
)
table_tasks = Table(
    "tasks",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("description", String),
    Column("project_id", Integer),
    Column("time_created", DateTime),
)
table_entries = Table(
    "entries",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("task_id", Integer),
    Column("active", Boolean),
    Column("time_start", DateTime),
    Column("time_end", DateTime),
)
