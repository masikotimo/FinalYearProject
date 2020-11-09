import calc
import app 

import pytest
from flask import g
from flask import Flask
from flask import session
from splinter import Browser

@pytest.yield_fixture(scope='session')
def browser():
    b = Browser()
    yield b
    b.quit()

url = 'http://localhost:5000/register'

def test_check_register(browser):
    browser.visit(url)
    assert 'Register' in browser.title


def test_index(app, client):
    url ='/'
    response = client.get(url)
    print(response)

    assert response.status_code == 200
    assert response.get_data() == b'hey you dashboard'
    

def test_register_page_returns_correct_html(app,client):
    url ='/register'
    response = client.get(url)
    assert response.status == '200 OK'
    html = response.get_data(as_text=True)
    assert '<form' in html
    assert '<input' in html


def test_register_page_accepts_post_request(client):
    rsp = client.post('/register', data={"todo_text": "do something useful"})
    assert rsp.status == '200 OK'
    assert '<form' in rsp.get_data(as_text=True)