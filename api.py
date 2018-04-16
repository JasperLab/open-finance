import flask
from flask import Flask
from flask import jsonify
from flask_restful import Resource, Api
import sys, traceback
import notes
import pandas as pd

app = Flask(__name__)
api = Api(app)

class Index(Resource):
    def get(self):
        return {'message': 'Welcome to open finance!'}

api.add_resource(Index, '/')

class Note(Resource):
    def get(self, symbol):
        try:
            f = getattr(__import__("notes.%s" % (symbol), fromlist=['notes']), 'response')
            r = f()
            # assert app.debug == False
            return pd.Series.to_json(r.portfolio, date_format='iso')
        except ModuleNotFoundError:
            app.logger.error("Module for %s not found." % symbol)
            return {'message': "Pricing for %s not found." % symbol}, 404

api.add_resource(Note, '/notes/<symbol>')


if __name__ == '__main__':
    app.run(debug=True)
