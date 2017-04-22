from flask import Flask, request, render_template, redirect, url_for
import os, sys
from werkzeug.utils import secure_filename
from forms import ModifyImage

app = Flask(__name__)
app.config.from_object('config')

@app.route('/', methods=['GET','POST'])
def search():
	info = None
	form = ModifyImage()	
	if form.validate_on_submit():
		info = form.image_loc.data
		#info = do pil stuff khere and pass info 
	return render_template('base.html',title='Image It', form=form, info=info)

if __name__ == "__main__":
	app.run(debug=True)
