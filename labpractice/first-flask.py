from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    html = ''
    html += '<html>\n'
    html += '<body>\n'
    html += '<p>Hello, World! Welcome to CS 110!!!!</p>\n'
    html += '</body>\n'
    html += '</html>\n'
    return html

if __name__ == '__main__':
    app.run()