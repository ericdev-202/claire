from django.shortcuts import render
from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
# Create your views here.

def index(request):
	return render(request,'index.html')