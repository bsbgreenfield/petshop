from flask import Flask, render_template, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import connect_db, db, Pet
from forms import AddPetForm, EditPetForm


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pet_shop'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

app.config['SECRET_KEY'] = 'benji'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)

app.app_context().push()

connect_db(app)


@app.route('/')
def homepage():
    all_pets = Pet.query.all()
    return render_template('pet_list.html', all_pets = all_pets)

@app.route('/add')
def view_add_pet():
    form = AddPetForm()
    return render_template('add_pet.html', form = form)

@app.route('/add', methods = ['POST'])
def submit_add_pet():
    form = AddPetForm()
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        new_pet = Pet(name = name, species = species, photo_url = photo_url, age = age, notes = notes)
        db.session.add(new_pet)
        db.session.commit()
        return redirect('/')
    else:
        return render_template('/add', form=form)

@app.route('/<int:pet_id>', methods = ['GET', 'POST'])
def view_pet(pet_id):
    selected_pet = Pet.query.get(pet_id)
    edit_form = EditPetForm(obj=selected_pet)
    if edit_form.validate_on_submit():
        selected_pet.photo_url = edit_form.photo_url.data
        selected_pet.notes = edit_form.notes.data
        selected_pet.available = edit_form.available.data
        db.session.add(selected_pet)
        db.session.commit()
        flash(f'{selected_pet.name} has been updated!')
    return render_template('view_pet.html', pet = selected_pet, form = edit_form)
