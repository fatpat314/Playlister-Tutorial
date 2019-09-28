#ALWAYS RUN MONGOD WHEN RUNNING THE SERVER!!!!!!!


from pymongo import MongoClient

client = MongoClient()
db = client.Playlister
playlists = db.playlists

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


#@app.route('/')

#def index():
    #return render_template('home.html', msg='Flask is cool!!')

# Our mock array of projects

    #playlists = [
        #{ 'title': 'Cat Videos', 'description': 'Cats acting weird' },
        #{ 'title': '80\'s Music', 'description': 'Don\'t stop believing!' },
        #{ 'title': 'Skate videos', 'description': 'Don\'t not wear a helmet'}
        #]
#'''playlists = [
#{ 'title': 'stoney street', 'artist': 'Amon Tobin' },
#{ 'title': 'glantz graf', 'artist': 'Autechre' }
#]'''

@app.route('/')
def playlists_index():
    """Show all playlists."""
    return render_template('playlists_index.html', playlists=playlists.find())

@app.route('/playlists/new')
def playlists_new():
    """Creat a new playlist"""
    return render_template('playlists_new.html')

@app.route('/playlists', methods=['POST'])
def playlists_submit():
    """Submit a new playlist."""
    playlist = {
        'title': request.form.get('title'),
        'description': request.form.get('description'),
        'videos': request.form.get('videos').split()
    }
    playlist.insert_one(playlist)
    #print(request.form.to_dict())
    return redirect(url_for('playlists_index'))




    #return render_template('playlists_new.html')


if __name__ == '__main__':
    app.run(debug=True)
