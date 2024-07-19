from django import forms
from .models import Reservation

class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['table', 'date', 'time', 'party_size']
        widgets = {
            'date': DateInput(),
            'time': TimeInput(),
        }
