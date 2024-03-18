from . import db
from .models import SessionTable


"""
Method to process the create session request
"""
def process_create_request(name):
    try:
        new_session = SessionTable(session_name=name)
        db.session.add(new_session)
        db.session.commit()
        print("Session info added to DB")
        return True
    except:
        print("Create Failed")
    return False

"""
Method to process delete session request
"""
def process_delete_request(session_name):
    try:
        db.session.query(SessionTable).filter(SessionTable.session_name == session_name).delete()
        db.session.commit()
        print("Session deleted")
        return True
    except:
        print("Delete Failed")

    return False