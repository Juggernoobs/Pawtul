"""Database models."""

from uuid import uuid4
from app import db


class Client(db.Model):
    """User account model."""
    __tablename__ = "clients"
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String(100), nullable=False, unique=False)
    firstname = db.Column(db.String(100), nullable=False, unique=False)
    lastname = db.Column(db.String(100), nullable=False, unique=False)
    email = db.Column(db.String(100), nullable=False, unique=False)
    phone = db.Column(db.String(100), nullable=False, unique=False)
    address1 = db.Column(db.String(100), nullable=False, unique=False)
    address2 = db.Column(db.String(100), nullable=False, unique=False)
    address3 = db.Column(db.String(100), nullable=False, unique=False)
    address4 = db.Column(db.String(100), nullable=False, unique=False)
    postcode = db.Column(db.String(100), nullable=False, unique=False)

    def __init__(self, uuid, firstname, lastname, email, phone, address1, address2, address3, address4,
                 postcode
                 ):
        self.uuid = uuid
        if self.uuid == "":
            self.uuid = str(uuid4())
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.phone = phone
        self.address1 = address1
        self.address2 = address2
        self.address3 = address3
        self.address4 = address4
        self.postcode = postcode


class Pet(db.Model):
    """User Pet model."""
    __tablename__ = "pets"
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String(100), nullable=False, unique=False)
    petname = db.Column(db.String(100), nullable=False, unique=False)
    petbreed = db.Column(db.String(100), nullable=False, unique=False)
    dob = db.Column(db.String(100), nullable=False, unique=False)
    microchip = db.Column(db.String(100), nullable=False, unique=False)
    petgender = db.Column(db.String(50), nullable=False, unique=False)
    petgendertype = db.Column(db.String(50), nullable=False, unique=False)
    vaccinated = db.Column(db.String(50), nullable=False, unique=False)
    nature = db.Column(db.String(50), nullable=False, unique=False)
    clientname = db.Column(db.String(50), nullable=False, unique=False)
    profilepic = db.Column(db.String(50), nullable=False, unique=False)
    vaccineprof = db.Column(db.String(50), nullable=False, unique=False)
    clients_id = db.Column(db.Integer, db.ForeignKey(
        'clients.id', ondelete="CASCADE"), nullable=False)

    def __init__(self, uuid, petname, petbreed, dob, microchip, petgender, petgendertype, vaccinated, nature,
                 clientname, profilepic, vaccineprof, clients_id
                 ):
        self.uuid = uuid
        self.petname = petname
        self.petbreed = petbreed
        self.dob = dob
        self.microchip = microchip
        self.petgender = petgender
        self.petgendertype = petgendertype
        self.vaccinated = vaccinated
        self.nature = nature
        self.clientname = clientname
        self.profilepic = profilepic
        self.vaccineprof = vaccineprof
        self.clients_id = clients_id


class Vet(db.Model):
    """User Vet model."""
    __tablename__ = "vets"
    id = db.Column(db.Integer, primary_key=True)
    vetprectice = db.Column(db.String(100), nullable=False, unique=False)
    phone = db.Column(db.String(100), nullable=False, unique=False)
    email = db.Column(db.String(100), nullable=False, unique=False)
    insured = db.Column(db.String(100), nullable=False, unique=False)
    address1 = db.Column(db.String(100), nullable=False, unique=False)
    address2 = db.Column(db.String(100), nullable=False, unique=False)
    address3 = db.Column(db.String(100), nullable=False, unique=False)
    address4 = db.Column(db.String(100), nullable=False, unique=False)
    postcode = db.Column(db.String(100), nullable=False, unique=False)
    clients_id = db.Column(db.Integer, db.ForeignKey(
        'clients.id', ondelete="CASCADE"), nullable=False)

    def __init__(self, vetprectice, phone, email, insured, address1, address2, address3, address4,
                 postcode, clients_id
                 ):
        self.vetprectice = vetprectice
        self.phone = phone
        self.insured = insured
        self.email = email
        self.phone = phone
        self.address1 = address1
        self.address2 = address2
        self.address3 = address3
        self.address4 = address4
        self.postcode = postcode
        self.clients_id = clients_id


class Contact(db.Model):
    """User Contact model."""
    __tablename__ = "contact"
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100), nullable=False, unique=False)
    lastname = db.Column(db.String(100), nullable=False, unique=False)
    email = db.Column(db.String(100), nullable=False, unique=False)
    phone = db.Column(db.String(100), nullable=False, unique=False)
    address1 = db.Column(db.String(100), nullable=False, unique=False)
    address2 = db.Column(db.String(100), nullable=False, unique=False)
    address3 = db.Column(db.String(100), nullable=False, unique=False)
    address4 = db.Column(db.String(100), nullable=False, unique=False)
    postcode = db.Column(db.String(100), nullable=False, unique=False)
    clients_id = db.Column(db.Integer, db.ForeignKey(
        'clients.id', ondelete="CASCADE"), nullable=False)

    def __init__(self, firstname, lastname, email, phone, address1, address2, address3, address4,
                 postcode, clients_id
                 ):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.phone = phone
        self.address1 = address1
        self.address2 = address2
        self.address3 = address3
        self.address4 = address4
        self.postcode = postcode
        self.clients_id = clients_id
