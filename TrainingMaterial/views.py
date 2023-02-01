from django.shortcuts import render
from django.http import HttpResponse

# Create your Home views here.
def TrainingMaterial(request):
	return render(request, 'TrainingMaterial/TrainingMaterial.html')
