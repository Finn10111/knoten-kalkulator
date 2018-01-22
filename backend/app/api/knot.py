from flask import jsonify, request

import os
from . import api
from .. import io
from .. import db
from ..models.knot import Knot
from ..schemas.knot import knot_schema, knots_schema
from flask_login import login_required
from flask_jwt_extended import jwt_required

@api.route('/knots', methods=['GET'])
@io.marshal_with(knots_schema)
def get_knots():
    knots = Knot.query.all()
    return knots


@api.route('/knots/<int:id>', methods=['GET'])
@io.marshal_with(knot_schema)
def get_knot(id):
    knot = Knot.query.get(id)
    if not knot:
        return io.not_found('Knot not found: ' + str(id))
    return knot


@api.route('/knots', methods=['POST'])
@io.from_body('knot', knot_schema)
@io.marshal_with(knot_schema)
def create_knot(knot):
    db.session.add(knot)
    db.session.commit()
    return knot


@api.route('/knots/<int:id>', methods=['PUT'])
@io.from_body('new_knot', knot_schema)
@io.marshal_with(knot_schema)
def update_knot(id, new_knot):
    knot = Knot.query.get(id)

    if not knot:
        return io.not_found('Knot not found: ' + str(id))

    if knot.image and knot.image != new_knot.image:
        # delete old image
        os.remove(os.path.join(os.path.dirname(os.path.realpath(__file__))+'/../../static/img', knot.image))

    # delete old/unsued cords if there are any
    for cord in knot.cords:
        if not cord in new_knot.cords:
            db.session.delete(cord)

    knot.name = new_knot.name
    knot.image = new_knot.image
    knot.width = new_knot.width
    knot.thickness = new_knot.thickness
    knot.cords = new_knot.cords

    db.session.add(knot)
    db.session.commit()
    return knot


@api.route('/knots/<int:id>', methods=['DELETE'])
@io.marshal_with(knot_schema)
def delete_knot(id):
    knot = Knot.query.get(id)
    if not knot:
        return io.not_found('Knot not found: ' + str(id))
    db.session.delete(knot)
    db.session.commit()
    return io.no_content()
