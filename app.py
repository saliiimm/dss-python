from flask import Flask, request, render_template, jsonify
import xml.etree.ElementTree as ET

app = Flask(__name__, template_folder='templates')

# Load data from the XML file
tree = ET.parse('artisteDevoir.xml')
root = tree.getroot()

def find_artist_by_name_partial(name):
    """Search for an artist by checking if their name starts with the given input."""
    matched_artists = []
    for artist in root.findall('artiste'):
        artist_name = artist.get('nom').lower()
        if artist_name.startswith(name.lower()):
            artist_albums = []
            artist_no = artist.get('no')
            for album in root.findall('album'):
                if album.find('ref-artiste').get('ref') == artist_no:
                    artist_albums.append({
                        'title': album.find('titre').text,
                        'year': album.get('annee'),
                        'songs': [song.text for song in album.findall('chansons/chanson')]
                    })
            matched_artists.append({
                'name': artist.get('nom'),
                'albums': artist_albums
            })

            
    return matched_artists

def find_all():
    """Search for an artist by checking if their name starts with the given input."""
    matched_artists = []
    for artist in root.findall('artiste'):
            artist_albums = []
            artist_no = artist.get('no')
            for album in root.findall('album'):
                if album.find('ref-artiste').get('ref') == artist_no:
                    artist_albums.append({
                        'title': album.find('titre').text,
                        'year': album.get('annee'),
                        'songs': [song.text for song in album.findall('chansons/chanson')]
                    })
            matched_artists.append({
                'name': artist.get('nom'),
                'albums': artist_albums
            })     
    return matched_artists

@app.route('/')
def index():
    artists_albums = find_all()
    return  render_template('index.html', artists_albums=artists_albums)
    
@app.route('/search')
def search():
    query = request.args.get('query', '').strip()
    if query:
        artists_albums = find_artist_by_name_partial(query)
    else:
        artists_albums = find_all()
    return jsonify(artists_albums)

if __name__ == '__main__':
    app.run(debug=True)
