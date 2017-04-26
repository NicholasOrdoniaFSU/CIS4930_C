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
	info = []
	#return request.form['options']
	#return render_template('base.html',title='Image It', form=form, info=len(form.data))
	if form.data['image_loc']: #check input field and radio button
		imgfile = form.data['image_loc'].split('/')[-1]
		info.append(request.form['options']) #get filter type in list
		info.append(imgfile) #add the image loc to list
		pic = Image.open(form.data['image_loc'])
		pixels = list(pic.getdata())
		gr = []
		if ("original" == request.form['options']):
			newPic = Image.new(pic.mode, pic.size)
			newfile = imgfile
			info.append(form.data)
			info.append(newfile)
			return render_template('base.html',title='Image It', form=form, info=info)
		else:
			newPic = Image.new(pic.mode, pic.size)
			if ("grey" == request.form['options']):
				for r,g,b in pixels:
					avg = int((r+g+b)/3)
					f = (avg,avg,avg)
					gr.append(f)
			elif ("red" == request.form['options']):
				for r,g,b in pixels:
					f = (r*10,g,b)
					gr.append(f)
			elif ("green" == request.form['options']):
				for r,g,b in pixels:
					f = (r,g*10,b)
					gr.append(f)
			elif ("blue" == request.form['options']):
				for r,g,b in pixels:
					f = (r,g,b*10)
					gr.append(f)
			elif ("bw" == request.form['options']):
				for r,g,b in pixels:
					avg = (r+g+b)/3
					if avg >= 128:
						avg = 255
					else:
						avg = 0
					f = (avg,avg,avg)
					gr.append(f)
			elif ("pink" == request.form['options']):
				for r,g,b in pixels:
					f = (r*2,g,b*2)
					gr.append(f)
			elif ("bt" == request.form['options']):
				for r,g,b in pixels:
					f = (int(round(r*.5)),int(round(g*0.7777)),b)
					gr.append(f)
			elif ("energy" == request.form['options']):
				for r,g,b in pixels:
					f = (int(round(r*2)),int(round(g*0.63)),int(round(b*0.2)))
					gr.append(f)
			elif ("blur" == request.form['options']):
				pic = Image.open(form.data['image_loc'])
				newPic = pic.filter(ImageFilter.BLUR)
			elif ("con" == request.form['options']):
				pic = Image.open(form.data['image_loc'])
				newPic = pic.filter(ImageFilter.CONTOUR)
			elif ("det" == request.form['options']):
				pic = Image.open(form.data['image_loc'])
				newPic = pic.filter(ImageFilter.DETAIL)
			elif ("edge" == request.form['options']):
				pic = Image.open(form.data['image_loc'])
				newPic = pic.filter(ImageFilter.EDGE_ENHANCE)
			elif ("emb" == request.form['options']):
				pic = Image.open(form.data['image_loc'])
				newPic = pic.filter(ImageFilter.EMBOSS)
			elif ("smo" == request.form['options']):
				pic = Image.open(form.data['image_loc'])
				newPic = pic.filter(ImageFilter.SMOOTH)
			elif ("shar" == request.form['options']):
				pic = Image.open(form.data['image_loc'])
				newPic = pic.filter(ImageFilter.SHARPEN)
			newPic.putdata(gr)
			newPic.save("static/" + request.form['options'] + "_" + imgfile)
			newfile = request.form['options'] + "_" + imgfile
			info.append(form.data)
			info.append(newfile)
			return render_template('base.html',title='Image It', form=form, info=info)
	else:
		#do original image
		info = []
		return render_template('base.html',title='Image It', form=form, info=info)
	
	
	

if __name__ == "__main__":
	app.run(debug=True)
