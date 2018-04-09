from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome to open finance!'

@app.route('/struct-notes/<string:symbol>')
def structured_note_quote(symbol):
    return 'Will return data for %s' % symbol
