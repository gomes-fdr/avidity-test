import os
import re
import requests
import json
from flask import Blueprint
from flask import render_template

bp_user = Blueprint('user', __name__)

@bp_user.route('/')
@bp_user.route('/<page>')
def index(page=1):
    api_token = os.environ['TOKEN_API']
    api_uri = 'https://api.github.com'
    repo_url = api_uri + '/repos/turicas/brasil.io'
    commits_url = repo_url + '/commits' + '?page={}'.format(page)

    try:
        response = requests.get(repo_url, headers={'Authorization': 'token ' + api_token})
    except requests.ConnectionError:
        return 'Connection Error', 500

    repo = json.loads(response.text)

    try:
        response = requests.get(commits_url, headers={'Authorization': 'token ' + api_token})
    except requests.ConnectionError:
        return 'Connection Error', 500

    link = response.headers.get('link')
    if link is not None:
        expr = 'page=([^&>]+)'
        list_links = link.split(',')
        pages = int(re.findall(expr, list_links[1])[0])
    else:
        pages=1

    commits = json.loads(response.text)

    return render_template('index.html', repo=repo, commits=commits, pages=pages)