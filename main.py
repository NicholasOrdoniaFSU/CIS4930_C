from flask import Flask, request, render_template, redirect, url_for
from PIL import ImageFilter, Image
import os
from werkzeug.utils import secure_filename
from forms import ModifyImage

app = Flask(__name__)
app.config.from_object('config')


@app.route('/', methods=['GET','POST'])
def search():
	info = None
	form = ModifyImage()
	if form.validate_on_submit():
		image_loc = form.image_loc.data
		info = greyScale(form.data.image_loc)
	return render_template('base.html',title='Image It', form=form, info=info)
	
def greyScale(loc):
	pic = Image.open(loc)
	pixels = list(pic.getdata())
	gr = []

	for r,g,b in pixels:
		avg = (r+g+b)/3
		f = (avg,avg,avg)
		gr.append(f)

	newPic = Image.new(pic.mode, pic.size)
	newPic.putdata(gr)
	newPic.save("static/new.jpeg")
	return "new.jpeg"
	
if __name__ == "__main__":
	app.run(debug=True)
