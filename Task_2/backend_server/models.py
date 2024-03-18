from . import db
from sqlalchemy.sql import func


"""
    Session Table schema
    id:  primary key
    session_name: name of the session which is unique
    date: Session creation date
"""
class SessionTable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    session_name = db.Column(db.String(150), unique=True)
    date = db.Column(db.DateTime(timezone=True), default=func.now())