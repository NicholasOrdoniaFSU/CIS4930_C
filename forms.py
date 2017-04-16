from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class ModifyImage(FlaskForm):
	image_loc = StringField('image_loc', validators=[DataRequired()])