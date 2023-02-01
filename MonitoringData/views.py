from django.shortcuts import render
from django.http import HttpResponse

# Create your Home views here.
def MonitoringData(request):
	return render(request, 'MonitoringData/MonitoringData.html')

# https://api.openweathermap.org/data/2.5/onecall?lat={22.338703}&lon={103.848252}&exclude={hourly}&appid={c797b4f25f10e0d6466d9c626c623120}