import DBcm

db_details = "CoachDB.sqlite3"

from queries import *

def get_swim_sessions():
    with DBcm.UseDatabase(db_details) as db:
        db.execute(SQL_SESSIONS)
        results = db.fetchall()
    return results

def get_session_swimmers(date):
    with DBcm.UseDatabase(db_details) as db:
        db.execute(SQL_SWIMMERS_BY_SESSION, (date,))
        results = db.fetchall()
    return results

def get_swimmers_events(name, age, date):
    with DBcm.UseDatabase(db_details) as db:
        db.execute(SQL_SWIMMERS_EVENTS_BY_SESSION, (name, age, date,))
        results = db.fetchall()
    return results

def get_swimmers_times(name, age, distance, stroke, date):
    with DBcm.UseDatabase(db_details) as db:
        db.execute(SQL_CHART_DATA_BY_SWIMMER_EVENT_SESSION, (name, age, distance, stroke, date,))
        results = db.fetchall()
    return results