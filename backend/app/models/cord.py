from .. import db


class Cord(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    knot_id = db.Column(db.Integer, db.ForeignKey('knot.id'))
    name = db.Column(db.String)
    factor = db.Column(db.Float)
    quantity = db.Column(db.Integer)


    def __repr__(self):
        return 'Cord {}>'.format(self.id)
