from django import forms

class CountryForm(forms.Form):
	country = forms.CharField( widget=forms.TextInput(attrs={'placeholder': 'E.G United States'}), max_length=500)