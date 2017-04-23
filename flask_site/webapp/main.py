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
	if form.data['image_loc'] and ("grey" == request.form['options']): #check input field and radio button
		imgfile = form.data['image_loc'].split('/')[-1]
		info.append(request.form['options']) #get filter type in list
		info.append(imgfile) #add the image loc to list
		pic = Image.open(form.data['image_loc'])
		pixels = list(pic.getdata())
		gr = []

		for r,g,b in pixels:
			avg = int((r+g+b)/3)
			f = (avg,avg,avg)
			gr.append(f)

		newPic = Image.new(pic.mode, pic.size)
		newPic.putdata(gr)
		newPic.save("static/grey.jpg")
		info.append(form.data)
		info.append(form.data['image_loc'])
		return render_template('base.html',title='Image It', form=form, info=info)
	elif form.data['image_loc'] and ("red" == request.form['options']): #check input field and radio button
		imgfile = form.data['image_loc'].split('/')[-1]
		info.append(request.form['options']) #get filter type in list
		info.append(imgfile) #add the image loc to list
		pic = Image.open(form.data['image_loc'])
		pixels = list(pic.getdata())
		gr = []

		for r,g,b in pixels:
			f = (r*10,g,b)
			gr.append(f)

		newPic = Image.new(pic.mode, pic.size)
		newPic.putdata(gr)
		newPic.save("static/red.jpg")
		info.append(form.data)
		info.append(form.data['image_loc'])
		return render_template('base.html',title='Image It', form=form, info=info)
	elif form.data['image_loc'] and ("green" == request.form['options']): #check input field and radio button
		imgfile = form.data['image_loc'].split('/')[-1]
		info.append(request.form['options']) #get filter type in list
		info.append(imgfile) #add the image loc to list
		pic = Image.open(form.data['image_loc'])
		pixels = list(pic.getdata())
		gr = []

		for r,g,b in pixels:
			f = (r,g*10,b)
			gr.append(f)

		newPic = Image.new(pic.mode, pic.size)
		newPic.putdata(gr)
		newPic.save("static/green.jpg")
		info.append(form.data)
		info.append(form.data['image_loc'])
		return render_template('base.html',title='Image It', form=form, info=info)
	elif form.data['image_loc'] and ("blue" == request.form['options']): #check input field and radio button
		imgfile = form.data['image_loc'].split('/')[-1]
		info.append(request.form['options']) #get filter type in list
		info.append(imgfile) #add the image loc to list
		pic = Image.open(form.data['image_loc'])
		pixels = list(pic.getdata())
		gr = []

		for r,g,b in pixels:
			f = (r,g,b*10)
			gr.append(f)

		newPic = Image.new(pic.mode, pic.size)
		newPic.putdata(gr)
		newPic.save("static/blue.jpg")
		info.append(form.data)
		info.append(form.data['image_loc'])
		return render_template('base.html',title='Image It', form=form, info=info)
	elif form.data['image_loc'] and ("bw" == request.form['options']): #check input field and radio button
		imgfile = form.data['image_loc'].split('/')[-1]
		info.append(request.form['options']) #get filter type in list
		info.append(imgfile) #add the image loc to list
		pic = Image.open(form.data['image_loc'])
		pixels = list(pic.getdata())
		gr = []

		for r,g,b in pixels:
			avg = (r+g+b)/3
			if avg >= 128:
				avg = 255
			else:
				avg = 0
			f = (avg,avg,avg)
			gr.append(f)

		newPic = Image.new(pic.mode, pic.size)
		newPic.putdata(gr)
		newPic.save("static/bw.jpg")
		info.append(form.data)
		info.append(form.data['image_loc'])
		return render_template('base.html',title='Image It', form=form, info=info)
	elif form.data['image_loc'] and ("pink" == request.form['options']): #check input field and radio button
		imgfile = form.data['image_loc'].split('/')[-1]
		info.append(request.form['options']) #get filter type in list
		info.append(imgfile) #add the image loc to list
		pic = Image.open(form.data['image_loc'])
		pixels = list(pic.getdata())
		gr = []

		for r,g,b in pixels:
			f = (r*2,g,b*2)
			gr.append(f)

		newPic = Image.new(pic.mode, pic.size)
		newPic.putdata(gr)
		newPic.save("static/pink.jpg")
		info.append(form.data)
		info.append(form.data['image_loc'])
		return render_template('base.html',title='Image It', form=form, info=info)
	elif form.data['image_loc'] and ("bt" == request.form['options']): #check input field and radio button
		imgfile = form.data['image_loc'].split('/')[-1]
		info.append(request.form['options']) #get filter type in list
		info.append(imgfile) #add the image loc to list
		pic = Image.open(form.data['image_loc'])
		pixels = list(pic.getdata())
		gr = []

		for r,g,b in pixels:
			f = (int(round(r*.5)),int(round(g*0.7777)),b)
			gr.append(f)

		newPic = Image.new(pic.mode, pic.size)
		newPic.putdata(gr)
		newPic.save("static/BedTime.jpg")
		info.append(form.data)
		info.append(form.data['image_loc'])
		return render_template('base.html',title='Image It', form=form, info=info)
	elif form.data['image_loc'] and ("energy" == request.form['options']): #check input field and radio button
		imgfile = form.data['image_loc'].split('/')[-1]
		info.append(request.form['options']) #get filter type in list
		info.append(imgfile) #add the image loc to list
		pic = Image.open(form.data['image_loc'])
		pixels = list(pic.getdata())
		gr = []

		for r,g,b in pixels:
			f = (int(round(r*2)),int(round(g*0.63)),int(round(b*0.2)))
			gr.append(f)

		newPic = Image.new(pic.mode, pic.size)
		newPic.putdata(gr)
		newPic.save("static/energy.jpg")
		info.append(form.data)
		info.append(form.data['image_loc'])
		return render_template('base.html',title='Image It', form=form, info=info)
	elif form.data['image_loc'] and ("blur" == request.form['options']): #check input field and radio button
		imgfile = form.data['image_loc'].split('/')[-1]
		info.append(request.form['options']) #get filter type in list
		info.append(imgfile) #add the image loc to list
		pic = Image.open(form.data['image_loc'])

		newPic = pic.filter(ImageFilter.BLUR)

		newPic.save("static/blur.jpg")
		info.append(form.data)
		info.append(form.data['image_loc'])
		return render_template('base.html',title='Image It', form=form, info=info)
	elif form.data['image_loc'] and ("con" == request.form['options']): #check input field and radio button
		imgfile = form.data['image_loc'].split('/')[-1]
		info.append(request.form['options']) #get filter type in list
		info.append(imgfile) #add the image loc to list
		pic = Image.open(form.data['image_loc'])

		newPic = pic.filter(ImageFilter.CONTOUR)

		newPic.save("static/con.jpg")
		info.append(form.data)
		info.append(form.data['image_loc'])
		return render_template('base.html',title='Image It', form=form, info=info)
	elif form.data['image_loc'] and ("det" == request.form['options']): #check input field and radio button
		imgfile = form.data['image_loc'].split('/')[-1]
		info.append(request.form['options']) #get filter type in list
		info.append(imgfile) #add the image loc to list
		pic = Image.open(form.data['image_loc'])

		newPic = pic.filter(ImageFilter.DETAIL)

		newPic.save("static/detail.jpg")
		info.append(form.data)
		info.append(form.data['image_loc'])
		return render_template('base.html',title='Image It', form=form, info=info)
	elif form.data['image_loc'] and ("edge" == request.form['options']): #check input field and radio button
		imgfile = form.data['image_loc'].split('/')[-1]
		info.append(request.form['options']) #get filter type in list
		info.append(imgfile) #add the image loc to list
		pic = Image.open(form.data['image_loc'])

		newPic = pic.filter(ImageFilter.EDGE_ENHANCE)

		newPic.save("static/edgeE.jpg")
		info.append(form.data)
		info.append(form.data['image_loc'])
		return render_template('base.html',title='Image It', form=form, info=info)
	elif form.data['image_loc'] and ("emb" == request.form['options']): #check input field and radio button
		imgfile = form.data['image_loc'].split('/')[-1]
		info.append(request.form['options']) #get filter type in list
		info.append(imgfile) #add the image loc to list
		pic = Image.open(form.data['image_loc'])

		newPic = pic.filter(ImageFilter.EMBOSS)

		newPic.save("static/emb.jpg")
		info.append(form.data)
		info.append(form.data['image_loc'])
		return render_template('base.html',title='Image It', form=form, info=info)
	elif form.data['image_loc'] and ("smo" == request.form['options']): #check input field and radio button
		imgfile = form.data['image_loc'].split('/')[-1]
		info.append(request.form['options']) #get filter type in list
		info.append(imgfile) #add the image loc to list
		pic = Image.open(form.data['image_loc'])

		newPic = pic.filter(ImageFilter.SMOOTH)

		newPic.save("static/smooth.jpg")
		info.append(form.data)
		info.append(form.data['image_loc'])
		return render_template('base.html',title='Image It', form=form, info=info)
	elif form.data['image_loc'] and ("shar" == request.form['options']): #check input field and radio button
		imgfile = form.data['image_loc'].split('/')[-1]
		info.append(request.form['options']) #get filter type in list
		info.append(imgfile) #add the image loc to list
		pic = Image.open(form.data['image_loc'])

		newPic = pic.filter(ImageFilter.SHARPEN)

		newPic.save("static/sharpen.jpg")
		info.append(form.data)
		info.append(form.data['image_loc'])
		return render_template('base.html',title='Image It', form=form, info=info)
	
	else:
		return render_template('base.html',title='Image It', form=form, info=info)
	'''
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
	'''
	

if __name__ == "__main__":
	app.run(debug=True)
