from django import forms

class ReservationForm(forms.Form):
    name = forms.CharField(label='Name', widget=forms.TextInput(attrs={'class': 'reservationinput'}), required=True)
    countryCode = forms.CharField(label='Country Code', widget=forms.TextInput(attrs={'class': 'reservationinput', 'style': 'width: 25%;'}), required=True)
    phone = forms.CharField(label='Phone', widget=forms.TextInput(attrs={'class': 'reservationinput'}), required=True)
    people = forms.IntegerField(label='People', widget=forms.NumberInput(attrs={'class': 'reservationinput'}), required=True)