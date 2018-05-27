from flask import Flask, jsonify
from flask_cors import CORS
import connectdata

app = Flask(__name__)
CORS(app)

@app.route("/city_job_au", methods=['GET'])
def get_city_au():
    return jsonify(connectdata.get_CITY_AU()),200

@app.route("/city_job_uk", methods=['GET'])
def get_city_uk():
    return jsonify(connectdata.get_CITY_UK()),200

@app.route("/city_job_au/<name>", methods=['GET'])
def retrieve_cityau(name):
    data = connectdata.retrive_CITY_AU(name)
    if data:
        return jsonify(data),200
    else:
        return jsonify({'message':'Invalid city name!'}),400

@app.route("/city_job_uk/<name>", methods=['GET'])
def retrieve_cityuk(name):
    data = connectdata.retrive_CITY_UK(name)
    if data:
        return jsonify(data),200
    else:
        return jsonify({'message':'Invalid city name!'}),400

@app.route("/city_au/<name>", methods=['GET'])
def get_au(name):
    data = connectdata.get_CITY_AU(name)
    if data:
        return jsonify(data),200
    else:
        return jsonify({'message':'Invalid city name!'}),400

@app.route("/city_uk/<name>", methods=['GET'])
def get_uk(name):
    data = connectdata.get_CITY_UK(name)
    if data:
        return jsonify(data),200
    else:
        return jsonify({'message':'Invalid city name!'}),400

@app.route("/work_hours", methods=['GET'])
def get_work_hours():
    return jsonify(connectdata.get_WORK_HOURS()),200

@app.route("/industryAu", methods=['GET'])
def get_industry_au():
    return jsonify(connectdata.get_CATE_AU()),200

@app.route("/industryUk", methods=['GET'])
def get_industry_uk():
    return jsonify(connectdata.get_CATE_UK()),200

@app.route("/informationau/<name>", methods=['GET'])
def get_au_information(name):
    data = connectdata.information_au(name)
    if data:
        return jsonify(data),200
    else:
        return jsonify({'message':'Invalid city name!'}),400

@app.route("/informationuk/<name>", methods=['GET'])
def get_uk_information(name):
    data = connectdata.information_uk(name)
    if data:
        return jsonify(data),200
    else:
        return jsonify({'message':'Invalid city name!'}),400

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Accept,Content-Type,AUTH_TOKEN')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response

if __name__ == "__main__":
    app.run()
