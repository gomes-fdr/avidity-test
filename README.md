# avidity-test

> Your task is to generate an HTML page that lists commits and shows some information from a public repository from Github.
> 
> Using the Github API (https://developer.github.com/v3/), choose a public repository, perhaps from  you favorite library and generate an HTML page with the following information:
> - Repository's full name ({owner}/{repo} e.g. avidity/some-repo) and description
> - List of recent commits including author's name and email as well as commit SHA, date and message
> 
> 
> Requests to the API must use authentication (even though for public repositories it's not required by Github).
> 
> We are not too fuzzy about the layout or design of the generated HTML page, but the HTML itself  should be well-formatted.
> 
> Your solution should highlight your programming abilities.
> 
> You should supply instructions on how to install and run your project.

## About this project

This is what I used to solve this test:

* Python-Flask in the backend;
* Python requests for http requests in flask
* To *builtify* the page, I used Bulmacss framework https://bulma.io/

The project follows this structure:

```
.
├── app
│   ├── __init__.py
│   ├── static
│   │   ├── css
│   │   │   ├── bulma.min.css
│   │   │   └── style.css
│   │   └── js
│   │       └── main.js
│   ├── templates
│   │   └── index.html
│   └── user.py
├── LICENSE
├── README.md
└── requirements.txt

5 directories, 9 files
```

This project use a factory pattern for flask apps.

It use a flask blueprints to isolate your routes.

## How to install it...

Step one, install from requirements file
```
 pip install -r requirements.txt
 ```

 Step two, export flask vars
 ```
 export FLASK_APP=app
 export TOKEN_API=" a valid token"
 ```

 Step three, run the app
 ```
 flask run app
 ```

Now the app are running in http://127.0.0.1:5000
