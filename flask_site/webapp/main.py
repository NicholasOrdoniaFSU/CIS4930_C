from flask import Flask, request, render_template, redirect, url_for
import os
from werkzeug.utils import secure_filename
from forms import ModifyImage

app = Flask(__name__)
app.config.from_object('config')
'''
@app.route('/') # '/' is the root homepage
def index():
	return render_template("base.html",title='Image It', form=form, info=info)
'''
@app.route('/', methods=['GET','POST'])
def search():
	info = None
	form = ModifyImage()
	if form.validate_on_submit():
		image_loc = form.image_loc.data
		info - get_info(image_loc)
	return render_template('base.html',title='Image It', form=form, info=info)
'''
UPLOAD_FOLDER = '/path/to/the/uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
'''

if __name__ == "__main__":
	app.run(debug=True)