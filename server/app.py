from flask import Flask
from flask_restful import Resource, Api, reqparse, abort
from flask_cors import CORS
import connectdata

app = Flask(__name__)
CORS(app)

class City_job_au(Resource):
    @staticmethod
    def get():
        return connectdata.get_CITY_AU(),200

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Accept,Content-Type,AUTH_TOKEN')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response

api = Api(app)
api.add_resource(City_job_au, '/city_job_au', methods=['GET'])

if __name__ == '__main__':
    app.run()
