from flask import Flask
from flask import request

app = Flask(__name__)
app.debug = True

@app.route('/')
def form_example():
    html = ''
    html += '<html>\n'
    html += '<body>\n'
    html += '<form method="POST" action="form_input">\n'
    html += 'Temperature in Fahrenheit: <input type="number" name="fahrenheit" />\n'
    html += '<p>\n'
    html += '<input type="submit" value="submit" />\n'
    html += '</form>\n'
    html += '</body>\n'
    html += '</html>\n'
    return html

@app.route('/form_input', methods=['POST'])
def form_input():
    fahrenheit = int(request.form['fahrenheit'])
    celsius = (fahrenheit-32)*5/9
    html = ''
    html += '<html>\n'
    html += '<body>\n'
    html += 'temperature in celcius: ' + str(round(celsius,2)) + '°C\n'
    html += '</body>\n'
    html += '</html>\n'
    return html

if __name__ == '__main__':
    app.run()