# omyaasree balaji
# CS110
# Final project
# HarmonyHub
# hosted online on - https://exuberant-pointy-pastry.glitch.me


from flask import Flask, request, render_template_string, render_template, session
import requests
import json



app = Flask(__name__)



#API and SECRET key taken from LAST.FM music app
LAST_FM_API_KEY = '6e807c90d0ed6e1e41356e734ac382c3'
app.secret_key = '473b63bd33c2a50762c546dcf126f2c8' 



# function to get a keyword from the user and assign all the output songs to particular indices
def get_search_form(track_checkboxes):

    # styled using CSS and html
    html = '<style>'
    html += 'body {'
    html += '  background: linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab);'
    html += '  background-size: 400% 400%;'
    html += '  animation: gradient 7s ease infinite;'
    html += '  height: 100vh;'
    html += '}'
    html += '@keyframes gradient {'
    html += '  0% {'
    html += '    background-position: 0% 50%;'
    html += '  }'
    html += '  50% {'
    html += '    background-position: 100% 50%;'
    html += '  }'
    html += '  100% {'
    html += '    background-position: 0% 50%;'
    html += '  }'
    html += '}'
    html += '</style>'

    html += '<title>HarmonyHub Search page</title>' # setting the title of the page

    html += '<form method="POST" action="/form_input">\n'
    html += '   <h2> Keyword: <input type="text" name="keyword" /></h2>\n'

    html += '<table>\n'
    html += '  <tr>\n'
    html += '    <th colspan="2"><h1>The COOL experience for the COOL you^-^</h1></th>\n'
    html += '  </tr>\n'
    html += '  <tr>\n'
    html += '    <td colspan="2">You will receive stats which include Name, Artist, and popularity</td>\n'
    html += '  </tr>\n'
    html += '  <tr>\n'
    html += '    <td>CS110</td>\n'
    html += '  </tr>\n'
    html += '</table>\n'



    #The code iterates over each track_checkbox in the track_checkboxes list.Each row will contain a checkbox and information about the track
    for track_checkbox in track_checkboxes:
        html += '    <tr>\n'
        html += f'        <td><input type="checkbox" name="selected_tracks" value="{track_checkbox["index"]}" /></td>\n'
        html += f'        <td>{track_checkbox["name"]}</td>\n'
        html += f'        <td>{track_checkbox["artist"]}</td>\n'
        html += f'        <td>{track_checkbox["listeners"]}</td>\n'
        html += '    </tr>\n'

    html += '</table>\n'
    html += '<input type="submit" value="Submit" />\n' # assigning a submit button which will take the input from the user to provide results in the next page
    html += '</form>\n'
    return html



# main function that calls the get_search_form() function
@app.route('/welcome', methods = ['POST'])
def main():
    return get_search_form(track_checkboxes=[])



# welcome() function definition that is responsible for the hosting of welcome page
# uses the file welcome.html to run
@app.route('/', methods=['GET', 'POST'])
def welcome():
    return render_template('welcome.html')

    if request.method == 'POST':
        return redirect(url_for('main'))  



# defining the form_input() function that make a request to last.fm to provide ordered results of the provided keyword
# uses form_input.html file to run and process the keyword
@app.route('/form_input', methods=['POST'])
def form_input():
    keyword = request.form['keyword'] #text input function

    # Last.fm API endpoint for track search and url
    url = f'http://ws.audioscrobbler.com/2.0/?method=track.search&track={keyword}&api_key={LAST_FM_API_KEY}&format=json'

    # Make the API request
    response = requests.get(url)
    data = response.json()

    # Check if any tracks are found
    if 'results' in data and 'trackmatches' in data['results']:
        tracks = data['results']['trackmatches']['track']

        track_checkboxes = []
        for track in tracks:
            track_checkboxes.append({
                'name': track["name"],
                'artist': track["artist"],
                'listeners': track["listeners"]
            })

        # Store track_checkboxes in the session
        session['track_checkboxes'] = track_checkboxes

        return render_template('form_input.html', keyword=keyword, track_checkboxes=track_checkboxes)
    else:
        return "No tracks found for the provided keyword."



# defining a selected_songs() function that 
@app.route('/selected_songs', methods=['POST'])
def selected_songs():
    # Retrieve selected tracks from the form data
    selected_indices = request.form.getlist('selected_tracks')

    # Retrieve track_checkboxes from the session
    track_checkboxes = session.get('track_checkboxes', [])

    # Initialize an empty list to store selected tracks
    selected_tracks = []

    # Use a for loop to iterate over selected_indices and append corresponding track_checkboxes to selected_tracks
    for index in selected_indices:
        # Convert index to an integer before using it to access the corresponding element in the 'track_checkboxes' list
        int_index = int(index)
        
        # Check if the index is valid before accessing the element
        if 0 <= int_index < len(track_checkboxes):
            selected_tracks.append(track_checkboxes[int_index])

    # Initialize an empty string to concatenate the song information
    song_info_output = ""


    # Return a response to the client with the song information

    # Print the desired output for each selected track
    for track_info in selected_tracks:
        song_info_output += f'<h4>name: {track_info["name"]}<br></h4>'
        song_info_output += f'<h4>artist: {track_info["artist"]}<br></h4>'
        song_info_output += f'<h4>popularity: {track_info["listeners"]}<br><br></h4>'



#styled using css and htmk
    html = '<html>'
    html += '<title>Your playlist</title>'
    html = '<style>'
    html += 'body {'
    html += '  background: linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab);'
    html += '  background-size: 400% 400%;'
    html += '  animation: gradient 7s ease infinite;'
    html += '  height: 100vh;'
    html += '}'

    html += '@keyframes gradient {'
    html += '  0% {'
    html += '    background-position: 0% 50%;'
    html += '  }'
    html += '  50% {'
    html += '    background-position: 100% 50%;'
    html += '  }'
    html += '  100% {'
    html += '    background-position: 0% 50%;'
    html += '  }'
    html += '}'
    html += '</style>'
    html += '<body>'
    html += '<td><center>Thank you for using HarmonyHub!!</center></td>'
    html += '<h1> Here are the songs you selected </h1>'
    html += song_info_output
    html += '<a href=https://exuberant-pointy-pastry.glitch.me>click to start again<br>'
    html += '</body>'
    html += '</html>'

    return html



if __name__ == '__main__':
    app.run()