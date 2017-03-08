from data.models import Person, db
import domain.models as domain_models

def get(id):
    person = db.session.query(Person).filter(Person.id == id).first()
    if person is None: return None
    return domain_models.Person(
        id = person.id,
        firstname = person.firstname,
        lastname = person.lastname,
        dateofbirth = person.dateofbirth,
        zipcode = person.zipcode
    )

def update(newperson):
    person = db.session.query(Person).filter(Person.id == newperson.id).first()
    if person is None: return False
    person.firstname = newperson.firstname
    person.lastname = newperson.lastname
    person.dateofbirth = newperson.dateofbirth
    person.zipcode = newperson.zipcode
    db.session.commit()
    return True

def add(person):
    newperson = Person(
        firstname = person.firstname,
        lastname = person.lastname,
        dateofbirth = person.dateofbirth,
        zipcode = person.zipcode
    )
    db.session.add(newperson)
    db.session.flush()
    id = newperson.id
    db.session.commit()
    return id

def get_all():
    people = db.session.query(Person).all()
    return [domain_models.Person(
        id = person.id,
        firstname = person.firstname,
        lastname = person.lastname,
        dateofbirth = person.dateofbirth,
        zipcode = person.zipcode
    ) for person in people]
