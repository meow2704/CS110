#https://super-vigorous-utahraptor.glitch.me (live link)
#omyaasree
#CS110
#Lab 7 - Web Applications

import requests
from flask import Flask, request

def getStock(symbol):
    baseURL = 'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&datatype=csv'
    keyPart = '&apikey=' + "XLUKKY7GEV5W7090"  # Add API key
    symbolPart = '&symbol=' + symbol
    stockResponse = requests.get(baseURL + keyPart + symbolPart)
    return stockResponse.text  # Return only text part of the response

app = Flask(__name__)
app.debug = True

@app.route('/')
def form_example():
    html = ''
    html += '\n <html> \n'
    html += '<title> stock input </title>'
    html += '<body bgcolor = tomato > \n'
    html += '<form method = "POST" action = "form_input"> \n'
    html += 'stock symbol: <input type = "text" name = "stock_symbol" />\n'
    html += '<br>'
    html += '<input type = "checkbox" id = "opening_price" name = "opening_price" value = "op"> \n'
    html += '<label for = "opening_price"> the opening price is </label> <br> \n'
    html += '<input type = "checkbox" id = "high_price" name = "high_price" value = "hp"> \n'
    html += '<label for = "high_price"> the high price is </label> <br> \n'
    html += '<input type = "checkbox" id = "low_price" name = "low_price" value = "lp"> \n'
    html += '<label for = "low_price"> the low price is </label> <br> \n'
    html += '<input type = "checkbox" id = "current_price" name = "current_price" value = "cp"> \n'
    html += '<label for = "current_price"> the current price is </label> <br> <br> \n'
    html += '<input type = "submit" value = "Submit"> \n'
    html += '</form> \n'
    html += '</body> \n'
    html += '</html> \n'
    return html

@app.route('/form_input', methods = ['POST'])
def form_input():
    stock_symbol = request.form['stock_symbol']
    opening_price = str(request.form.getlist('opening_price'))
    high_price = str(request.form.getlist('high_price'))
    low_price = str(request.form.getlist('low_price'))
    current_price = str(request.form.getlist('current_price'))
    stock_symbol = stock_symbol.upper()
    stockString = getStock(stock_symbol)
    html = ''
    html += '<html>'    
    html += '<title> stock information </title>'
    html += '<body bgcolor="violet">'
    if stockString != '{}':
        stockList = stockString.split(',')
        html += '<h2> The value for ' + stock_symbol + ' is as follows: </h2>'
        if opening_price == '[\'op\']':
            html += '<p> Opening Price: ' + stockList[10] + '</p>'
        if high_price == '[\'hp\']':
            html += '<p> High: ' + stockList[11] + '</p>'
        if low_price == '[\'lp\']':
            html += '<p> Low: ' + stockList[12] + '</p>'
        if current_price == '[\'cp\']':
            html += '<p> Current Price: ' + stockList[13] + '</p>'
    else:
        html += '<p> ERROR! PLEASE ENTER A VALID STOCK! </p>'
    html += '<a href="https://super-vigorous-utahraptor.glitch.me  ">click to go Back</a>'
    html += '</body>'
    html += '</html>'
    return html


if __name__ == '__main__':
    app.run()