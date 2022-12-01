from django import forms


class autoForm(forms.Form):
    marca=forms.CharField(max_length=30)
    patente=forms.IntegerField()
    modelo=forms.CharField(max_length=30)


class MotosForm(forms.Form):
    marca=forms.CharField(max_length=30)
    cilindrada=forms.IntegerField()
    tipo=forms.CharField(max_length=30)


class Pickup_suv_Form(forms.Form):
    marca=forms.CharField(max_length=30)
    tipo_motor=forms.CharField(max_length=30)
    rodado=forms.IntegerField()