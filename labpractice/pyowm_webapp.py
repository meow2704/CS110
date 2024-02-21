# omyaasree.pythonanywhere.com
# omyaasree
# cs 100
# Hosting your Webapp Online
#step1

from flask import Flask
from flask import request
from pyowm import OWM


app = Flask(__name__)

owm = OWM('6d6ed3f63dc6b335a336e93e72e8941c')
mgr = owm.weather_manager()


def getWeather(city, country):
    location = city+','+country
    observation = mgr.weather_at_place(location)
    w = observation.weather    
    return w.temperature('fahrenheit')

@app.route('/')
def main():
    html = '<html><body>'
    html += '<form method="POST" action="form_input">\n'
    html += 'City: <input type="text" name="city" />\n'
    html += '<p>\n'
    html += 'Country: <input type="text" name="country" />\n'
    html += '<p>\n'
    html += '<input type="submit" value="submit" />\n'
    html += '</form>\n'
    html += '</body></html>'
    return html

@app.route('/form_input', methods=['POST'])
def form_input():
    city = request.form['city']
    country = request.form['country']
    temperature = getWeather(city, country)
    html = ''
    html += '<html>\n'
    html += '<body>\n'
    html += 'City: ' + city + ' Country: ' + country + '\n'
    html += '<p>'
    html += 'The max temp is: ' + str(temperature['temp_max']) +'\n'
    html += '<p>'
    html += 'The current temp is: ' + str(temperature['temp']) + '\n'
    html += '<p>'
    html += 'The minimum temp is: ' + str(temperature['temp_min']) + '\n'
    html += '</body>\n'
    html += '</html>\n'
    return html



if __name__ == '__main__':
    app.run()


