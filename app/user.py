import requests
import json
from flask import Blueprint
from flask import render_template

bp_user = Blueprint('user', __name__)

def get_param_from_url(url, param_name):
    return [i.split("=")[-1] for i in url.split("?", 1)[-1].split("&") if i.startswith(param_name + "=")][0]

@bp_user.route('/')
@bp_user.route('/<page>')
def index(page=1):
    api_token = 'c45269a16cf3f992410bab84109026551ebd9a35'
    api_uri = 'https://api.github.com'
    repo_url = api_uri + '/repos/turicas/brasil.io'
    commits_url = api_uri + '/repos/turicas/brasil.io/commits' + '?page={}'.format(page)

    try:
        response = requests.get(repo_url, headers={'Authorization': 'token ' + api_token})
    except requests.ConnectionError:
        return "Connection Error"

    repo = json.loads(response.text)

    try:
        response = requests.get(commits_url, headers={'Authorization': 'token ' + api_token})
    except requests.ConnectionError:
        return "Connection Error"

    link = response.headers.get('link')
    if link is not None:
        total = link.split(',')
        pages = int(get_param_from_url(total[1].split(';')[0].replace('>', ''), 'page'))
    else:
        pages=1

    print(page)
    print(commits_url)
    commits = json.loads(response.text)

    return render_template('index.html', repo=repo, commits=commits, pages=pages)