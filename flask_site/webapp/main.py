from flask import Flask, request, render_template, redirect, url_for
import os, sys
from werkzeug.utils import secure_filename
from forms import ModifyImage
from PIL import ImageFilter, Image

app = Flask(__name__)
app.config.from_object('config')

@app.route('/', methods=['GET','POST'])
def search():
	form = ModifyImage()
	#return render_template('base.html',title='Image It', form=form, info=len(form.data))
	if form.data['image_loc_bw'] is not None and len(form.data['image_loc_bw']) > 4:
		pic = Image.open(form.data['image_loc_bw'])
		pixels = list(pic.getdata())
		gr = []

		for r,g,b in pixels:
			avg = int((r+g+b)/3)
			f = (avg,avg,avg)
			gr.append(f)

		newPic = Image.new(pic.mode, pic.size)
		newPic.putdata(gr)
		newPic.save("static/bw.jpg")
		return render_template('base.html',title='Image It', form=form, info=form.data['image_loc_red'])

	elif form.data['image_loc_red'] is not None and len(form.data['image_loc_red']) > 4:
		pic = Image.open(form.data['image_loc_red'])
		pixels = list(pic.getdata())
		gr = []

		for r,g,b in pixels:
			#avg = int((r+g+b)/3)
			f = (r*10,g,b)
			gr.append(f)

		newPic = Image.new(pic.mode, pic.size)
		newPic.putdata(gr)
		newPic.save("static/red.jpg")
		return render_template('base.html',title='Image It', form=form, info=form.data['image_loc_blue'])

	elif form.data['image_loc_blue'] is not None and len(form.data['image_loc_blue']) > 4:
		pic = Image.open(form.data['image_loc_blue'])
		pixels = list(pic.getdata())
		gr = []

		for r,g,b in pixels:
			#avg = int((r+g+b)/3)
			f = (r,g,b*10)
			gr.append(f)

		newPic = Image.new(pic.mode, pic.size)
		newPic.putdata(gr)
		newPic.save("static/blue.jpg")
		return render_template('base.html',title='Image It', form=form, info=newPic)

	else:
		return render_template('base.html',title='Image It', form=form, info="None")

if __name__ == "__main__":
	app.run(debug=True)
