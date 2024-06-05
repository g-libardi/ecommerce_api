import sqlite3 as sql
from flask import current_app, g

def get_db():
    if 'db' not in g:
        g.db = sql.connect(current_app.config['DATABASE'])
        g.db.row_factory = sql.Row
    return g.db

def init_db():
    db = get_db()
    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))

def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()