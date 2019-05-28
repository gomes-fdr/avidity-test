import requests
import json
import random
from flask import Blueprint
from flask import render_template

bp_user = Blueprint('user', __name__)

@bp_user.route('/')
def index():
    n_user = random.randrange(3,12)
    uri = 'https://randomuser.me/api/?results={}&nat=br&inc=name,location,email,picture'.format(n_user)

    try:
        response = requests.get(uri)
    except requests.ConnectionError:
        return "Connection Error"

    data = json.loads(response.text)

    return render_template('index.html', data=data, n_user=n_user)