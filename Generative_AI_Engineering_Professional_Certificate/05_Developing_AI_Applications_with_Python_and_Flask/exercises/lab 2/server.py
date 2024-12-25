# Import the Flask class from the flask module
from flask import Flask, make_response

# Create an instance of the Flask class, passing in the name of the current module
app = Flask(__name__)

# Define a route for the root URL ("/")
@app.route("/")
def index():
    # Function that handles requests to the root URL
    # Return a plain text response
    return "Kitt, te necesito!"

# Define a route for the "/no_content" URL
@app.route("/no_content")
def no_content():
    # return 'No content found' with a status of 204
    # Returns:
       # string: No content found
       # status code: 204
    # Create a dictionary with a message and return it with a 204 No Content status code
    return ({"message": "No content found"}, 204)

# Define a route for the "/exp" URL
@app.route("/exp")
def index_explicit():
    """Return 'Kitt, te necesito!' message with a status code of 200.
    Returns:
        response: A response object containing the message and status code 200.
    """
    # Create a response object with the message "Kitt, the necesito!""
    resp = make_response({"message": "Kitt, te necesito!"})
    # Set the status code of the response to 200
    resp.status_code = 200
    # Return the response object
    return resp