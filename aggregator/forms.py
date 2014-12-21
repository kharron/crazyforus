from django import forms

class Aggregator(forms.Form):
		title = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Title'}))
		article_text = forms.CharField(widget=forms.Textarea(attrs={'name': 'article-body', 'class': 'admin-textarea', 'rows': '10', 'placeholder': 'Article Text'}))
		source_name = forms.CharField(max_length=64, widget=forms.TextInput(attrs={'placeholder': 'Site Name'}))
		source_link = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Link to article'}))
		article_image = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Link to image'}), max_length=255)
		publish_datetime = forms.DateTimeField(widget=forms.DateTimeInput())

class TagsForm(forms.Form):
		tags = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Tags separated by comma'}), max_length=512)
		
