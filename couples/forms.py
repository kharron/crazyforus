from django import forms

class UploadMainPic(forms.Form):
		hero_image = forms.FileField(label='Select an Image')
