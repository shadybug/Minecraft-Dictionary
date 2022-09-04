import flask

app = flask.Flask(__name__)

dictionary = {
    "Leopard Gecko" : "A desert-dwelling lizard with dark spots. Unlike most geckos, they have eyelids.",
    "Ball Python" : 'A snake species common for beginner pet owners. Known for their tendency to "ball up" when nervous, which gives them their name.',
    "Hognose Snake" : "A burrowing snake species, that uses its pointed snout like a shovel. They play dead when threatened.",
    "Iguana" : "A bright green lizard that lives in tropical environments. Difficult to keep in captivity, as they grow very large and need a lot of space.",
    "Red-eared Slider" : "A turtle species that lives in ponds and lakes. They were named for the red stripes on the side of their head, and are the most commonly kept species of turtle.",
}

@app.route('/')
def home():
    return flask.render_template('index.html')

@app.route('/def/<item>')
def lookup(item):
    return flask.render_template('index.html', item = item, definition = dictionary[item])