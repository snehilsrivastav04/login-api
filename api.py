
from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token

api_blueprint = Blueprint('api', __name__)

@api_blueprint.route('/api/login', methods=['POST'])
def login():
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    if username == 'test' and password == 'test':
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token)
    return jsonify({"msg": "Bad username or password"}), 401
