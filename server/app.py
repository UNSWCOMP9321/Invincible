from flask import Flask
from flask_restful import Resource, Api, reqparse, abort
import connectdata

app = Flask(__name__)

class City_job_au(Resource):
    @staticmethod
    def get():
        data=connectdata.get_CITY_AU()
        print(data)
        return data,200

api = Api(app)
api.add_resource(City_job_au, '/city_job_au', methods=['GET'])

if __name__ == '__main__':
    app.run()
