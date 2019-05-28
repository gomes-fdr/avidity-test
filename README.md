# avidity-test

~~An app to test Marvel API.~~

> ## The Comics test
> 
> Your task is to generate an HTML page that lists the characters from a Marvel-story.
> 
> Using the Marvel API [http://developer.marvel.com/docs], pick a random > story featuring your favorite character (perhaps The Hulk?). Generate an HTML > page with the following characteristics:
> 
> * The story's description
> * A list of names and pictures of the characters that features in the > story
> * The Marvel attribution text
> 
> We are not too fuzzy about the layout or design of the generated HTML > page, but the HTML itself should be well-formatted.
>
> Your solution should highlight your Python programming abilities.
>
> You should supply instructions on how to install and run your project.

## About this project

The Marvel API it was broke, then I made the test using another public API. In the randomUser API, we have no apikey for authentication,  but the project isnt change a lot if it will be necessary, it will be just another parameter.

This is what I used to solve this test:

* Python-Flask in the backend;
* Python requests for http requests in flask
* To obtain the data RandomUser API https://randomuser.me/
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

In the main.js file we have some javascript to make a counter and reload the page after timeout occurs.

In the style.css just a little bit of css for render the data text correctly.

## How to install it...

Step one, install from requirements file
```
 pip install -r requirements.txt
 ```

 Step two, export flask vars
 ```
 export FLASK_APP=app 
 ```

 Step three, run the app
 ```
 flask run app
 ```

Now the app are running in http://127.0.0.1:5000
