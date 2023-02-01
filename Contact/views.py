from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .forms import loginForm

class Contact(View):
	def get(sefl, request):
		LF = loginForm
		return render(request, 'Contact/Contact.html', {'LF': LF})
	def post(seft, request):
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return render(request, 'Contact/Sendalarm.html')
		else:
			return HttpResponse('Đăng nhập không thành công')




