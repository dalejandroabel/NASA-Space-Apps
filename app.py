"""
A sample Hello World server.
"""
import os

from flask import Flask, render_template, jsonify, request

# pylint: disable=C0103
app = Flask(__name__)


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    message = "epa"

    """Get Cloud Run environment variables."""
    service = os.environ.get('K_SERVICE', 'Unknown service')
    revision = os.environ.get('K_REVISION', 'Unknown revision')

    return render_template('index.html',
        message=message,
        Service=service,
        Revision=revision)

@app.route('/getDisastersData',methods=["GET"])
def handle_get():
    if request.method == 'GET':
        country = request.args['country']
        city = request.args['city']
        year = request.args['year']
        disasterType = request.args['disasterType']
        # Traer los datos con PD, Procesarlos con funciones y retornar un json como:



        
        #Pueden usar pd.df.to_json() o sino construirlo como diccionario y usar JSONIFY:
        data = {
            "id" : 1,
            "country" : country,
            "city" : city,
            "year" : year,
            "dissasterType" : disasterType
        }
        return jsonify(data)

if __name__ == '__main__':
    server_port = os.environ.get('PORT', '8080')
    app.run(debug=True, port=server_port, host='0.0.0.0')
