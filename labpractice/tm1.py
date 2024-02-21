#Caterina Ponti
#CS110
#Hosting your Webapp Online
#https://caterinaponti05.pythonanywhere.com/


from flask import Flask
from flask import request
import tmdbsimple as tmdb

tmdb.API_KEY = 'e2ff98ce434e270b9dbf924b25a060e6' #API key

app = Flask(__name__)


@app.route('/')
def main():
    html = '<html><body>'
    html += '<form method="POST" action="form_input">\n'
    html += 'Movie: <input type="text" name="movie" />\n'
    html += '<p>\n'
    html += '<input type="submit" value="submit" />\n'
    html += '</form>\n'
    html += '</body></html>'
    return html

@app.route('/form_input', methods=['POST'])

def form_input():

    movie_title = request.form['movie']
    search = tmdb.Search()
    response = search.movie(query = movie_title)

    html = '<html><body>'
    html += '<table border = "1">'
    html += '<tr>'
    html += '<td>Name</td>'
    html += '<td>Popularity</td>'
    html += '<td>Release Date</td>'
    html += '</tr>'
    html += '</table>'
    html += '</body></html>'
    return html

    for movie in response['results']:
        html += '<tr>'
        html += '<td>' +  movie['title'] + '</td>'
        html += '<td>' + movie['id'] + '</td>'
        html += '<td>' + movie['release_date'] + '</td>'
        html += '<td>' + movie['popularity'] + '</td>'
        html += '</tr>'
        return html

if __name__ == '__main__':
    app.run()





