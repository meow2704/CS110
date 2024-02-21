# omyaasree.pythonanywhere.com
# omyaasree
# cs 100
# Hosting your Webapp Online

from flask import Flask
from flask import request
from pyowm import OWM
import tmdbsimple as tmdb


app = Flask(__name__)

tmdb.API_KEY = "2528c5ee8dd6917c833643e6b6c7fc1e"

def movie_name():
    while True:
        user_input = str(input("\nwhich movie do you want to search for :\n"))

        search = tmdb.Search()
        response = search.movie(query = user_input)

        for s in search.results:
            print(s['title'],  s['id'],  s['release_date'],  s['popularity'])



@app.route('/')
def main():
    html = '<html><body>'
    html += '<form method="POST" action="form_input">\n'
    html += 'movie: <input type="text" name="movie" />\n'
    html += '<p>\n'
    html += '<input type="submit" value="submit" />\n'
    html += '</form>\n'
    html += '</body></html>'
    return html

@app.route('/form_input', methods=['POST'])
def form_input():
    movie = request.form['movie']
    
    search = tmdb.Search()
    response = search.movie_name(moviename)

    if not response:
        return "No movies found for the provided name."

    html = '<html>\n'
    html += '<body>\n'
    html += '<table border="1">'
    html += '<tr>'
    html += '<th>Movie Name</th>'
    html += '<th>ID</th>'
    html += '<th>Popularity</th>'
    html += '<th>Release Date</th>'
    html += '</tr>'

    for movie in response:
        html += f'<tr>'
        html += f'<td>{movie["title"]}</td>'
        html += f'<td>{movie["id"]}</td>'
        html += f'<td>{movie["popularity"]}</td>'
        html += f'<td>{movie["release_date"]}</td>'
        html += f'</tr>'
    
    html += '</table>'
    html += '</body>\n'
    html += '</html>\n'
    return html



if __name__ == '__main__':
    app.run()


