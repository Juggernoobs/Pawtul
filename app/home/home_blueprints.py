"""Logged-in page routes."""
import os
import pathlib
from flask import Blueprint, render_template, request, redirect, url_for, session
from flask_login import current_user, login_required
from werkzeug.utils import secure_filename

from app.home.home_models import Client, Pet, Vet, Contact
from app.signup.signup_models import User
from app import db
from uuid import uuid4

# Blueprint Configuration
home_blueprints = Blueprint(
    "home_blueprints", __name__, template_folder="templates", static_folder="static"
)

PARENT_PATH = str(pathlib.Path(__file__).parent.resolve())

UPLOAD_FOLDER = 'app/static/images'


@home_blueprints.route("/", methods=["GET"])
@login_required
def dashboard():
    """Logged-in User Dashboard."""
    return render_template(
        "dashboard.html",
        title="Flask-Login Tutorial",
        template="dashboard-template",
        current_user=current_user,
        body="You are now logged in!",
    )
    


@home_blueprints.route("/clients", methods=["POST", "GET"])
@login_required
def client(search: str = None):
    if request.method == 'POST':
        search = request.form.get('search')
        query_one = Client.query.filter_by(
            firstname=search
        )

        get_data_in_cards = query_one
    else:
        get_data_in_cards = Client.query.all()

    """Logged-in User Dashboard."""
    return render_template(
        "clients.html",
        template="dashboard-template",
        current_user=current_user,
        body="You are now logged in!",
        get_data_in_cards=get_data_in_cards
    )


@ home_blueprints.route("/deleteclient/<int:id>")
@ login_required
def deletecli(id):
    delete_client = Client.query.filter_by(id=id).first()
    db.session.delete(delete_client)
    db.session.commit()

    """Logged-in User Dashboard."""
    return redirect('/clients'
                    )


@ home_blueprints.route("/addclients", methods=["POST", "GET"])
@ login_required
def addclient():
    """Logged-in User Dashboard."""

    if request.method == 'POST':
        UUID = request.form.get('UUID')
        address1 = request.form.get('address1')
        firstname = request.form.get('firstname')
        address2 = request.form.get('address2')
        lastname = request.form.get('lastname')

        address3 = request.form.get('address3')
        email = request.form.get('email')
        address4 = request.form.get('address4')
        phonenumber = request.form.get('phonenumber')
        postcode = request.form.get('postcode')
        account_id=session['_user_id']
        record = Client(
            id=str(uuid4()), 
            account_id=account_id,
            firstname=firstname,
            lastname=lastname,
            email=email,
            phone=phonenumber,
            address1=address1,
            address2=address2,
            address3=address3,
            address4=address4,
            postcode=postcode)
        db.session.add(record)
        db.session.commit()
        return redirect('/clients')

    return render_template(
        "addclient.html",
        template="dashboard-template",
        current_user=current_user,
        body="You are now logged in!",
    )


@ home_blueprints.route("/editclients/<int:uid>", methods=["POST", "GET"])
@ login_required
def editclientss(uid):
    """Logged-in User Dashboard."""

    client_record = Client.query.filter_by(id=uid).first()

    if request.method == 'POST':
        UUID = request.form.get('UUID')
        address1 = request.form.get('address1')
        firstname = request.form.get('firstname')
        address2 = request.form.get('address2')
        lastname = request.form.get('lastname')

        address3 = request.form.get('address3')
        email = request.form.get('email')
        address4 = request.form.get('address4')
        phonenumber = request.form.get('phonenumber')
        postcode = request.form.get('postcode')

        client_record.uuid = UUID
        client_record.firstname = firstname
        client_record.lastname = lastname
        client_record.email = email
        client_record.phone = phonenumber
        client_record.address1 = address1
        client_record.address2 = address2
        client_record.address3 = address3
        client_record.address4 = address4
        client_record.postcode = postcode
        db.session.commit()
        return redirect('/clients')

    return render_template(
        "editclient.html",
        template="dashboard-template",
        current_user=current_user,
        body="You are now logged in!",
        client_record=client_record
    )


@ home_blueprints.route("/viewpets/<int:uid>", methods=["POST", "GET"])
@ login_required
def viewpet(uid):
    """Logged-in User Dashboard."""
    pets_record = Pet.query.filter_by(clients_id=uid).all()
    return render_template('viewpets.html', pets_record=pets_record)


@ home_blueprints.route("/deletepets/<int:uid>", methods=["POST", "GET"])
@ login_required
def deletepet(uid):
    """Logged-in User Dashboard."""
    pets_record = Pet.query.filter_by(clients_id=uid).first()
    db.session.delete(pets_record)
    db.session.commit()

    vets_record = Vet.query.filter_by(clients_id=uid).first()
    db.session.delete(vets_record)
    db.session.commit()

    contacts_record = Contact.query.filter_by(clients_id=uid).first()
    db.session.delete(contacts_record)
    db.session.commit()
    return redirect('/viewpets/' + str(uid))


@ home_blueprints.route("/client_pets/<int:userid>", methods=["POST", "GET"])
@ login_required
def pets(userid):
    """Logged-in User Pets."""

    get_client_for_add_pet = Client.query.filter_by(id=userid).first()
    show_all_client = Client.query.all()

    # uuid, petname, petbreed, dob, microchip, petgender, petgendertype,
    # vaccinated, nature, clientname, profilepic, vaccineprof, clients_id

    if request.method == 'POST':
        UUID = request.form.get('UUID')
        petname = request.form.get('petname')
        petbreed = request.form.get('petbreed')
        dob = request.form.get('dob')
        microchip = request.form.get('microchip')
        profilepicture = request.files['myFile']
        gender = request.form.get('gender')
        gendertype = request.form.get('gendertype')
        vaccinated = request.form.get('vaccinated')
        behaviour = request.form.get('behaviour')
        clientname = request.form.get('clientname')
        vaccineproof = request.files['myFile1']
        profilepicture.save(os.path.join(
            UPLOAD_FOLDER, secure_filename(profilepicture.filename)))
        vaccineproof.save(os.path.join(
            UPLOAD_FOLDER, secure_filename(vaccineproof.filename)))
        record = Pet(uuid=UUID, petname=petname, petbreed=petbreed, dob=dob, microchip=microchip, petgender=gender,
                     petgendertype=gendertype, vaccinated=vaccinated,
                     nature=behaviour, clientname=clientname, profilepic=profilepicture.filename,
                     vaccineprof=vaccineproof.filename, clients_id=userid
                     )
        db.session.add(record)
        db.session.commit()
        return redirect('/vets/' + str(userid))

    return render_template('client_pets.html', client=get_client_for_add_pet, allclient=show_all_client)


@ home_blueprints.route("/vets/<string:userid>")
@ home_blueprints.route("/vets/<int:userid>", methods=["POST", "GET"])
@ login_required
def vets(userid):
    """Logged-in User Vets."""

    get_client_for_add_pet = Client.query.filter_by(id=userid).first()
    show_all_client = Client.query.all()

    if request.method == 'POST':
        vetprectice = request.form.get('vetprectice')
        vetphone = request.form.get('vetphone')
        vetmail = request.form.get('vetmail')
        insured = request.form.get('insured')
        vetaddress1 = request.form.get('vetaddress1')
        vetaddress2 = request.form.get('vetaddress2')
        vetaddress3 = request.form.get('vetaddress3')
        vetaddress4 = request.form.get('vetaddress4')
        postal = request.form.get('postal')

        record = Vet(vetprectice=vetprectice, phone=vetphone, email=vetmail, insured=insured,
                     address1=vetaddress1, address2=vetaddress2, address3=vetaddress3,
                     address4=vetaddress4, postcode=postal, clients_id=userid)
        db.session.add(record)
        db.session.commit()
        return redirect('/contact/' + str(userid))

    return render_template('addvet.html', client=get_client_for_add_pet, allclient=show_all_client)


@ home_blueprints.route("/contact/<string:userid>")
@ home_blueprints.route("/contact/<int:userid>", methods=["POST", "GET"])
@ login_required
def contacts(userid):
    """Logged-in Contacts Pets."""

    get_client_for_add_pet = Client.query.filter_by(id=userid).first()
    show_all_client = Client.query.all()

    if request.method == 'POST':
        emergencyfirstname = request.form.get('emergencyfirstname')
        emergencysecondname = request.form.get('emergencysecondname')
        emergencyphone = request.form.get('emergencyphone')
        emergencyemail = request.form.get('emergencyemail')
        emergencyadd1 = request.form.get('emergencyadd1')
        emergencyadd2 = request.form.get('emergencyadd2')
        emergencyadd3 = request.form.get('emergencyadd3')
        emergencyadd4 = request.form.get('emergencyadd4')
        emergencypostcode = request.form.get('emergencypostcode')

        record = Contact(firstname=emergencyfirstname, lastname=emergencysecondname, email=emergencyemail,
                         phone=emergencyphone, address1=emergencyadd1, address2=emergencyadd2,
                         address3=emergencyadd3, address4=emergencyadd4, postcode=emergencypostcode,
                         clients_id=userid)
        db.session.add(record)
        db.session.commit()
        return redirect('/')

    return render_template('contact.html', client=get_client_for_add_pet, allclient=show_all_client)


@home_blueprints.route("/pets", methods=["POST", "GET"])
@login_required
def pet(search: str = None):
    if request.method == 'POST':
        search = request.form.get('search')
        query_one = Pet.query.filter_by(
            petname=search
        )

        get_data_in_cards = query_one
    else:
        get_data_in_cards = Pet.query.all()

    """Logged-in User Dashboard."""
    return render_template(
        "pets.html",
        template="dashboard-template",
        current_user=current_user,
        body="You are now logged in!",
        get_data_in_cards=get_data_in_cards
    )
