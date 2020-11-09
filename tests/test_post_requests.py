import calc
import app 

import pytest
from flask import g
from flask import Flask


def test_register_page_accepts_post_request(client):
    rsp = client.post('/register', data={"todo_text": "do something useful"})
    assert rsp.status == '200 OK'
    assert '<form' in rsp.get_data(as_text=True)


def test_login_page_accepts_post_request(client):
    rsp = client.post('/login', data={"todo_text": "do something useful"})
    assert rsp.status == '200 OK'
    assert '<form' in rsp.get_data(as_text=True)