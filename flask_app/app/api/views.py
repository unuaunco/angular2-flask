from flask import Blueprint, request, jsonify, make_response, current_app as app
from . import api

@api.route('/test_data/', methods=['GET'])
def get_test_data():

    return jsonify({
        "state": "success",
        "data": "The data here"
    })