from flask import Flask, render_template
from pymongo import MongoClient


app = Flask(__name__)

client = MongoClient()
db = client.Playlister
playlists = db.playlists
#@app.route('/')

#def index():
    #return render_template('home.html', msg='Flask is cool!!')

# Our mock array of projects

    #playlists = [
        #{ 'title': 'Cat Videos', 'description': 'Cats acting weird' },
        #{ 'title': '80\'s Music', 'description': 'Don\'t stop believing!' },
        #{ 'title': 'Skate videos', 'description': 'Don\'t not wear a helmet'}
        #]
'''playlists = [
{ 'title': 'stoney street', 'artist': 'Amon Tobin' },
{ 'title': 'glantz graf', 'artist': 'Autechre' }
]'''

@app.route('/')
def playlists_index():
    """Show all playlists."""
    return render_template('playlists_index.html', playlists=playlists.find())

@app.route('/playlists/new')
def playlists_new():


    return render_template('playlists_new.html')


if __name__ == '__main__':
    app.run(debug=True)
