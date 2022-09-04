import flask

app = flask.Flask(__name__)

dictionary = {
    "LeopardGecko" : "A desert-dwelling lizard with dark spots. Unlike most geckos, they have eyelids.",
    "BallPython" : 'A snake species common for beginner pet owners. Known for their tendency to "ball up" when nervous, which gives them their name.',
    "Hognose Snake" : "A burrowing snake species, that uses its pointed snout like a shovel. They play dead when threatened.",
    "Iguana" : "A bright green lizard that lives in tropical environments. Difficult to keep in captivity, as they grow very large and need a lot of space.",
    "Red-earedSlider" : "A turtle species that lives in ponds and lakes. They were named for the red stripes on the side of their head, and are the most commonly kept species of turtle.",
    "Test" : "This is a test!",
}

@app.route('/')
def home():
    return flask.render_template('main.html', entries = dictionary)

@app.route('/def/<item>')
def lookup(item):
    return flask.render_template('index.html', item = item, definition = dictionary[item])