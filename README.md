# Simple Test POST API

## Description:
Send a POST request to the server with a JSON object in the body. The key for the JSON object is "string_to_split". The value is any valid string, including empty strings. If the request contains invalid JSON, does not include the required string_to_split key, or does not contain a string value, a 400 Bad Request response will be returned. Otherwise, a response with a JSON body will be returned. The response will contain the key "return_string" and a string value containing every third character of the string to split.

### Setup
You should have at least Python3.7. These instructions are for Linux or Mac.

Clone this repo and navigate to the home directory.

Create a virtual environment
`python3 -m venv .venv`

Activate the virtual environment.
`. .venv/bin/activate`

Install the requirements.
`pip install -r requirements.txt`

Run the tests.
`pytest`

Configure flask app
`export FLASK_APP=src/flaskr/app.py`

Run the flask server from the root directory of this project.
`flask run`

**If `flask run` doesn't work, try updating the python path:**
`export PYTHONPATH=`pwd``

Try submitting a post request on your local machine:
`curl -X POST http://127.0.0.1:5000/test --data '{"string_to_cut": "iamyourlyftdriver"}' -H 'Content-Type: application/json'`

When you are done, deactivate the Python3 virtual environment.
`deactivate`
