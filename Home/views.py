from django.shortcuts import render
from django.http import HttpResponse

# Create your Home views here.
def index(request):
	return render(request, 'Home/index.html')
