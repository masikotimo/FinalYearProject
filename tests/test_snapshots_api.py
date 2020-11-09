import requests

def test_register_api_snapshots(snapshot):
    response = requests.get('http://localhost:5000/register')
    snapshot.assert_match(response)

def test_login_api_snapshots(snapshot):
    response = requests.get('http://localhost:5000/login')
    snapshot.assert_match(response)