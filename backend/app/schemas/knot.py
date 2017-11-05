from .. import ma
from . import cord
from ..models.knot import Knot
from marshmallow import post_dump, pre_load, fields


class KnotSchema(ma.ModelSchema):

    cords = ma.Nested(cord.CordSchema, many=True)

    class Meta:
        model = Knot

    @pre_load(pass_many=True)
    def remove_envelope(self, data, many):
        namespace = 'knots' if many else 'knot'
        return data[namespace]

    @post_dump(pass_many=True)
    def add_envelope(self, data, many):
        namespace = 'knots'
        return {namespace: data}


knot_schema = KnotSchema()
knots_schema = KnotSchema(many=True)
