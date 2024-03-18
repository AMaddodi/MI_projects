import requests


"""
Test case to test create session 
"""
def test_create_session():
    print("test 1")
    url = 'http://127.0.0.1:5000/createSession'
    session_input = {'session_name': 'test1'}
    response = requests.post(url, json = session_input)
    print(response.text)

"""
Test case to delete session
"""
def test_delete_session():
    print("Test 2")
    session_name = 'test1'
    url = 'http://127.0.0.1:5000/deleteSession/'+session_name
    response = requests.delete(url)
    print(response.text)


test_create_session()
test_delete_session()
