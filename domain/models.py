class Person:
    def __init__(self, id= None, firstname='', lastname='', dateofbirth='', zipcode=''):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.dateofbirth = dateofbirth
        self.zipcode = zipcode

    def serialize(self):
        return {
            'id': self.id,
            'firstname': self.firstname,
            'lastname': self.lastname,
            'dateofbirth': self.dateofbirth.isoformat(),
            'zipcode': self.zipcode
        }
