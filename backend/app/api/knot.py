import os
from . import api
from .. import io
from .. import db
from ..models.knot import Knot
from ..schemas.knot import knot_schema, knots_schema
from flask_jwt_extended import jwt_required
from flask_io import fields
from sqlalchemy_utils.functions import sort_query


@api.route('/knots', methods=['GET'])
@io.from_query('order_by', fields.String(missing='name'))
@io.marshal_with(knots_schema)
def get_knots(order_by):
    query = Knot.query

    if order_by:
        query = sort_query(query, order_by)

    knots = query.all()
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
@jwt_required
def create_knot(knot):
    db.session.add(knot)
    db.session.commit()
    return knot


@api.route('/knots/<int:id>', methods=['PUT'])
@io.from_body('new_knot', knot_schema)
@io.marshal_with(knot_schema)
@jwt_required
def update_knot(id, new_knot):
    knot = Knot.query.get(id)

    if not knot:
        return io.not_found('Knot not found: ' + str(id))

    if knot.image and knot.image != new_knot.image:
        # delete old image
        os.remove(os.path.join(os.path.dirname(os.path.realpath(__file__)) +
                               '/../../static/img', knot.image))

    # delete old/unsued cords if there are any
    for cord in knot.cords:
        if cord not in new_knot.cords:
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
@jwt_required
def delete_knot(id):
    knot = Knot.query.get(id)
    if not knot:
        return io.not_found('Knot not found: ' + str(id))
    db.session.delete(knot)
    db.session.commit()
    return io.no_content()
