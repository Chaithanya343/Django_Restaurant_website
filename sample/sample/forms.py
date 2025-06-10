from django import forms

class ReservationForm(forms.Form):
    name = forms.CharField(label='Name', widget=forms.TextInput(attrs={'class': 'reservationinput','style': 'width: 80%;'}), required=True)
    countryCode = forms.CharField(label='Country Code', widget=forms.TextInput(attrs={'class': 'reservationinput', 'style': 'width: 10%;'}), required=True)
    phone = forms.CharField(label='Phone', widget=forms.TextInput(attrs={'class': 'reservationinput', 'style': 'width: 50%;' }), required=True)
    people = forms.IntegerField(label='Number Of People', widget=forms.NumberInput(attrs={'class': 'reservationinput', 'style': 'width: 65%;'}), required=True)