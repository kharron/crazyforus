from django import forms
from register.states import *

class RegisterForm(forms.Form):
		email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder':'Email'})) 
		bfirstname = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Bride First Name'}))
		blastname = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Bride Last Name'}))
		gfirstname = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Grooms First Name'}))
		glastname = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Grooms Last Name'}))
		weddingdate = forms.DateField(widget=forms.DateInput())
		websitename = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'(i.e. ChrisandMarie)'}))
		password = forms.CharField(widget=forms.PasswordInput())		
		zipcode = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'current or wedding'}))
		city = forms.CharField(max_length=50)
		state = forms.ChoiceField(widget=forms.Select, choices=STATES)

		def confirm_password(self):
				clean_password = self.cleaned_data['password']
				confirm_clean_password = self.cleaned_data['confirm_password']
				if clean_password != confirm_clean_password:
						raise forms.ValidationError("Passwords do not match!")
				return clean_password
