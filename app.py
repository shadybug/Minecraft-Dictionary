import flask

app = flask.Flask(__name__)

dictionary = {
    "Steve" : "The default player.",
    "Alex" : "An alternate skin for the player.",
}

@app.route('/')
def home():
    return flask.render_template('index.html', item = "Alex", definition = "An alternate skin for the player.")