from flask import Blueprint
from flask import request
from .manage_session import process_create_request, process_delete_request

session = Blueprint('session', __name__)

"""
This method to route the request to create session
"""
@session.route('/createSession', methods=['POST'])
def create_session():
    print(request.json)
    if process_create_request(request.json['session_name']) == True:
        return "Success"
    return "Failed"

"""
This method to route the request to delete the session
"""
@session.route('/deleteSession/<session_name>', methods= ['DELETE'])
def delete_session(session_name):
    print(session_name)
    if process_delete_request(session_name) == True:
        return "Success"
    return "Failed"