from flask import Flask, request, jsonify
import requests
app = Flask(__name__)

BASE_URL = "https://api.covid19api.com"

@app.route('/')
def hello_world():
    return 'Hello, World!'

# /api/cases/total?country_code=SG
@app.route('/api/cases/total')
def get_total_cases_by_country_code():

    country_code = request.args.get('country_code')
    get_url = BASE_URL + "/total/country/" + country_code

    response = requests.get(get_url)

    cases_list = response.json()[-1]

    if response.ok:
        return jsonify(cases_list)
    else:
        return jsonify({
            "message": "Something went wrong"
        })

