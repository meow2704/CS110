#omyaasree.pythonanywhere.com
#Omyaasree
#cs110
# cs 100
# Hosting your Webapp Online
#step2

from flask import Flask, request
import tmdbsimple as tmdb

app = Flask(__name__)

tmdb.API_KEY = "2528c5ee8dd6917c833643e6b6c7fc1e"  # Replace with your TMDb API key

@app.route('/')
def main():
    html = '<html><body>'
    html += '<form method="POST" action="form_input">\n'
    html += 'Movie: <input type="text" name="movie" />\n'
    html += '<p>\n'
    html += '<input type="submit" value="Submit" />\n'
    html += '</form>\n'
    html += '</body></html>'
    return html

@app.route('/form_input', methods=['POST'])
def form_input():
    movie_name = request.form['movie']
    
    search = tmdb.Search()
    response = search.movie(query=movie_name)

    # Check if any movies are found
    if not response['results']:
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

    for movie in response['results']:
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
