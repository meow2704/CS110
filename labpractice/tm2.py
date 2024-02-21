# Import necessary modules
from flask import Flask, request
import tmdbsimple as tmdb

# Set your TMDb API key
tmdb.API_KEY = 'e2ff98ce434e270b9dbf924b25a060e6'

# Create a Flask web app
app = Flask(__name__)

# Define the main route for the web app
@app.route('/')
def main():
    html = '<html><body>'
    html += '<form method="POST" action="/form_input">\n'  # Use a forward slash before "form_input"
    html += 'Movie: <input type="text" name="movie" />\n'
    html += '<p>\n'
    html += '<input type="submit" value="Submit" />\n'  # Changed "submit" to "Submit"
    html += '</form>\n'
    html += '</body></html>'
    return html

# Define the route to handle the form submission
@app.route('/form_input', methods=['POST'])
def form_input():
    movie_title = request.form['movie']
    search = tmdb.Search()
    response = search.movie(query=movie_title)

    html = '<html><body>'
    html += '<table border="1">'  # Moved this line outside of the loop
    html += '<tr>'
    html += '<td>Name</td>'
    html += '<td>Popularity</td>'
    # html += '<td>id</td>'
    html += '<td>Release Date</td>'
    html += '</tr>'

    for movie in response['results']:
        html += '<tr>'
        html += '<td>' + movie['title'] + '</td>'
        html += '<td>' + str(movie['popularity']) + '</td>'
        # html += '<td>' + movie['id'] + '</td>' # Cast popularity to a string
        html += '<td>' + movie['release_date'] + '</td>'
        html += '</tr>'

    html += '</table>'  # Close the table
    html += '</body></html>'
    return html

# Run the web app if this script is executed
if __name__ == '__main__':
    app.run()
