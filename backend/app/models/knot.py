from .. import db
from . import cord


class Knot(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    image = db.Column(db.String)
    width = db.Column(db.Float)
    thickness = db.Column(db.Float)
    cords = db.relationship("Cord")

    def __repr__(self):
        return 'Knot {}>'.format(self.id)
