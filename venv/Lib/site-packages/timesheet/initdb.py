from . import db


def run():
    db.metadata.create_all()
    for table in db.metadata.tables:
        print("Table: %s" % table)
