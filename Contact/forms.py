from django import forms

class loginForm(forms.Form):
	username = forms.CharField(max_length = 25)
	password = forms.CharField(max_length = 13, widget = forms.PasswordInput)
