#ALWAYS RUN MONGOD WHEN RUNNING THE SERVER!!!!!!!

from flask import Flask, render_template, request, redirect, url_for
from bson.objectid import ObjectId
from pymongo import MongoClient
import os

host = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/Playlister')
client = MongoClient(host=f'{host}?retryWrites=false')
db = client.get_default_database()
playlists = db.playlists


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

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT',5000))

@app.route('/playlists/new')
def playlists_new():
    """Creat a new playlist"""
    return render_template('playlists_new.html', playlist={}, title='New Playlist')

@app.route('/playlists', methods=['POST'])
def playlists_submit():
    """Submit a new playlist."""
    playlist = {
        'title': request.form.get('title'),
        'description': request.form.get('description'),
        'videos': request.form.get('videos').split()
    }
    #playlist.insert_one(playlist)
    #print(request.form.to_dict())
    playlist_id = playlists.insert_one(playlist).inserted_id
    return redirect(url_for('playlists_show', playlist_id=playlist_id))

@app.route('/playlists/<playlist_id>')  #!!!!!!!
def playlists_show(playlist_id):
    """Show a single playlist."""
    playlist = playlists.find_one({'_id': ObjectId(playlist_id)})
    return render_template('playlists_show.html', playlist=playlist)

@app.route('/playlists/<playlist_id>/edit')
def playlists_edit(playlist_id):
    """Show the edit form for a playlist"""
    playlist = playlists.find_one({'_id': ObjectId(playlist_id)})
    return render_template('playlists_edit.html', playlist=playlist, titel='Edit Playlist')

@app.route('/playlists/<playlist_id>', methods=['POST'])
def playlists_update(playlist_id):
    """Submit an edited playlist"""
    update_playlist = {
        'title': request.form.get('title'),
        'description': request.form.get('description'),
        'videos': request.form.get('videos').split()
    }
    playlists.update_one(
        {'_id': ObjectId(playlist_id)},
        {'$set': update_playlist})
    return redirect(url_for('playlists_show', playlist_id=playlist_id))

@app.route('/playlists/<playlist_id>/delete', methods=['POST'])
def playlists_delete(playlist_id):
        """Delete one playlist."""
        playlists.delete_one({'_id': ObjectId(playlist_id)})
        return redirect(url_for('playlists_index'))



    #return render_template('playlists_new.html')
