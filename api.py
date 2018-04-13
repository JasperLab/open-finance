import sys, traceback
from flask import Flask
from flask import jsonify
app = Flask(__name__)

import notes

@app.route('/')
def index():
    return 'Welcome to open finance!'

@app.route('/note/<string:symbol>', methods=['GET'])
def note(symbol):
    try:
        f = getattr(__import__("notes.%s" % (symbol), fromlist=['notes']), 'response')
        r = f()
        return r.to_json()
    except ModuleNotFoundError:
        app.logger.error("Module for %s not found." % symbol)
        return "Pricing for %s not found" % symbol, 404
    except :
        m, e, t = sys.exc_info()
        app.logger.error(traceback.print_tb(t))
        app.logger.error(e)
        return 'Internal error occurred.', 500
