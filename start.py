from flask import Flask, request, session, g, redirect, url_for, \
                  abort, render_template, flash, json, send_from_directory, \
                  jsonify

import data.person
from data.models import db

import domain.models

from werkzeug.contrib.fixers import ProxyFix

import os

from dateutil import parser

# create app!
app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('PERSONTRACKER_SETTINGS')

app.wsgi_app = ProxyFix(app.wsgi_app)

# Initialize Database
db.init_app(app)

SITE_ROOT = os.path.realpath(os.path.dirname(__file__))

def vue_template(path):
    return open(os.path.join(SITE_ROOT, 'vues', path)).read()

@app.route('/')
def get_people():
    people = data.person.get_all()
    return render_template(
        'layout.html',
        vue = vue_template('people.html'),
        jsfilename = 'people.js',
        model = {
            'people': [person.serialize() for person in people],
            'status': None
        }
    )

@app.route('/<int:id>', methods=['POST'])
def save_person(id):
    newperson = request.get_json();
    dateofbirth = parser.parse(newperson['dateofbirth'])
    person = domain.models.Person(
        id = id,
        firstname = newperson['firstname'],
        lastname = newperson['lastname'],
        dateofbirth = dateofbirth,
        zipcode = newperson['zipcode']
    )
    person
    data.person.update(person)
    return ''

@app.route('/', methods=['PUT'])
def add_person():
    newperson = request.get_json();
    dateofbirth = parser.parse(newperson['dateofbirth'])
    person = domain.models.Person(
        firstname = newperson['firstname'],
        lastname = newperson['lastname'],
        dateofbirth = dateofbirth,
        zipcode = newperson['zipcode']
    )
    id = data.person.add(person);
    return jsonify(id)

@app.route('/<int:id>')
def get_person(id):
    return render_template(
        'layout.html',
        vue = vue_template('person.html'),
        jsfilename = 'person.js',
        model = data.person.get(id).serialize()
    )

if __name__ == '__main__':
    app.run();
