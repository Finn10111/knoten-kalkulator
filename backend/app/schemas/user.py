from .. import ma
from ..models.user import User


class userSchema(ma.ModelSchema):

    class Meta:
        model = User


user_schema = userSchema()
users_schema = userSchema(many=True)
