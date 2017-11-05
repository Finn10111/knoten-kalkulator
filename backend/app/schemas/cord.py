from .. import ma
from ..models.cord import Cord
from marshmallow import post_dump, pre_load
from marshmallow_sqlalchemy import field_for


class CordSchema(ma.ModelSchema):

    class Meta:
        model = Cord

    #knot_id = field_for(Cord, 'knot_id', dump_only=False)

"""
    @pre_load(pass_many=True)
    def remove_envelope(self, data, many):
        namespace = 'cords' if many else 'cords'
        return data[namespace]

    @post_dump(pass_many=True)
    def add_envelope(self, data, many):
        namespace = 'cords'
        return {namespace: data}
"""

cord_schema = CordSchema()
cords_schema = CordSchema(many=True)
