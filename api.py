import flask
from flask import Flask, request, render_template, Response, jsonify
#from flask_restful import Resource, Api
import sys, traceback
import notes
import pandas as pd

app = Flask(__name__)

def request_wants_json():
    best = request.accept_mimetypes \
        .best_match(['application/json', 'text/html'])
    return best == 'application/json' and \
        request.accept_mimetypes[best] > \
        request.accept_mimetypes['text/html']

@app.route('/', methods=['GET'])
def index():
    if request_wants_json():
        return jsonify({'endpoints': [ 
            {'/': 'Index'},
            {'/notes/<symbol>': 'Single structured note historical value'}
            ]} )
    else:
        return '''
        <html>
            <head>Welcome to Open Finance</head>
            <body>
                Available end-points (HTML or JSON depending on specified accepted MIME type header):
                <br/>
                <ol>
                    <li><b>/</b> -this page</li>
                    <li><b>/notes/&lt;symbol&gt;</b> -single structured note historical value</li>
                </ol>
            </body>
        </html>
        '''

@app.route('/notes/<symbol>')
def note():
    pass


#api = Api(app)

#@api.representation('application/json')
#def output_json(data, code, headers=None):
#    resp = make_response(json.dumps(data), code)
#    resp.headers.extend(headers or {})
#    return resp
#
#@api.representation('application/html')
#def output_html(data, code, headers=None):
#
#
#class Index(Resource):
#    def get(self):
#        return Response(render_template('index.html', mimetype='text/html'))
#
#api.add_resource(Index, '/')
#
#class Note(Resource):
#    def get(self, symbol):
#        try:
#            f = getattr(__import__("notes.%s" % (symbol), fromlist=['notes']), 'response')
#            r = f()
#            # assert app.debug == False
#            return pd.Series.to_json(r.portfolio, orient='split', date_format='iso')
#        except ModuleNotFoundError:
#            app.logger.error("Module for %s not found." % symbol)
#            return {'message': "Pricing for %s not found." % symbol}, 404
#
#api.add_resource(Note, '/notes/<symbol>')


if __name__ == '__main__':
    app.run(debug=True)
