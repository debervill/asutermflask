from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from app import app

db = SQLAlchemy(app)

ma = Marshmallow(app)

class User(db.Model):
    fio = db.Column(db.String)
    dolgnost = db.Column(db.String)
    zvanie = db.Column(db.String)
    date_created = db.Column(db.DateTime, auto_now_add=True)

    def __repr__(self):
        return '<User %r>' % self.username


class UserSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("fio",  "dolgnost",  "zvanie", "_links")

    # Smart hyperlinking
    _links = ma.Hyperlinks(
        {"self": ma.URLFor("user_detail", id="<id>"), "collection": ma.URLFor("users")}
    )




