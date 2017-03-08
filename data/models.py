from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Person(db.Model):
    __tablename__ = 'people'
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(20))
    lastname = db.Column(db.String(20))
    dateofbirth = db.Column(db.DateTime)
    zipcode = db.Column(db.String(20))

    def __init__(self, id=None, firstname=None, lastname=None,
                 dateofbirth=None, zipcode=None):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.dateofbirth = dateofbirth
        self.zipcode = zipcode
