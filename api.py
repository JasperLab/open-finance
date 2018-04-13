from flask import Flask
app = Flask(__name__)

import notes

@app.route('/')
def index():
    return 'Welcome to open finance!'

@app.route('/note/<string:symbol>', methods=['GET'])
def note(symbol):
    f = getattr(__import__("notes.%s" % (symbol), fromlist=['notes']), 'response')
    r = f()
    return r
