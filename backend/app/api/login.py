from flask import jsonify, request, json
from flask_jwt_extended import jwt_required, create_access_token, create_refresh_token, jwt_refresh_token_required, get_jwt_identity

from . import api
from .. import io
from .. import db
from ..models.user import User
from ..schemas.user import user_schema, users_schema
from ..helpers.jwt_esat import jwt_esat_refresh_token_required


@api.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data['username']
    password = data['password']
    user = User.query.filter_by(username=username).first()
    if user is not None and user.verify_password(password):
        ret = {
            'access_token': create_access_token(identity=username),
            'refresh_token': create_refresh_token(identity=username)
        }
        return jsonify(ret), 200
    else:
        return False

@api.route('/refresh', methods=['POST'])
@jwt_esat_refresh_token_required
def refresh():
    current_user = get_jwt_identity()
    ret = {
        'access_token': create_access_token(identity=current_user),
        'refresh_token': create_refresh_token(identity=current_user)
    }
    return jsonify(ret), 200

@api.route('/logout', methods=['POST'])
def logout():
    logout_user()
    return True
