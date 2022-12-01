from django import forms


class autoForm(forms.Form):
    marca=forms.CharField(max_length=30)
    patente=forms.IntegerField()
    modelo=forms.CharField(max_length=30)