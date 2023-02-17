from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField
from wtforms.validators import Optional, InputRequired, URL

class AddPetForm(FlaskForm):
    """form for adding pets"""

    name = StringField("Pet Name", validators= [InputRequired()])
    species = StringField("Species", validators= [InputRequired()])
    photo_url = StringField("Photo URL", validators = [Optional(), URL()] )
    age = IntegerField("Age", validators = [Optional()] )
    notes = StringField("Additional Notes", validators=[Optional()])

class EditPetForm(FlaskForm):
     photo_url = StringField("Photo URL", validators = [Optional(), URL()] )
     notes = StringField("Additional Notes", validators=[Optional()])
     available = BooleanField("Available?")