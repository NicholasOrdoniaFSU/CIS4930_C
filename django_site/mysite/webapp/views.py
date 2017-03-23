from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	return HttpResponse("<h2>upload image</h2><br /><br /> <input name='imgfile' type='text' /><br /><input name='submit' value='Submit' type='submit' />")