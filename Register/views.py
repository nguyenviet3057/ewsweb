from django.shortcuts import render
from django.http import HttpResponse
from .forms import Registerform
from .models import Registermodel

# Create your views here.
def Register(request):
	context = {'RF': Registerform}
	return render(request, 'Register/Register.html', context)
def getRegister(request):
	if request.method == "POST":
		RF = Registerform(request.POST)
		if RF.is_valid():
			saveRF = Registermodel(
				username = RF.cleaned_data['username'],
				email = RF.cleaned_data['email'],
				company = RF.cleaned_data['company'],
				phonenumber = RF.cleaned_data['phonenumber'],
				password = RF.cleaned_data['password'],
				address = RF.cleaned_data['address'])
			saveRF.save()
			return HttpResponse('Đăng kí thành công')
		else:
			return HttpResponse('Đăng kí không thành công')
