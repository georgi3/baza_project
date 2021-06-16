from django import forms
from .models import Booking
import datetime
from django import template
from django.core.validators import validate_integer
from django.contrib.auth.models import User
register = template.Library()


@register.filter(is_safe=False)
class DateInput(forms.DateInput):
    input_type = 'date'


@register.filter(is_safe=False)
class BookingForm(forms.ModelForm):
    def clean(self):
        data = self.cleaned_data
        starting_date = data['starting_date']
        ending_date = data['end_date']

        if starting_date and ending_date:
            if starting_date >= ending_date:
                raise forms.ValidationError('Конец не может быть раньше начала.')
        today = datetime.datetime.today()
        if starting_date < datetime.date(today.year, today.month, today.day):
            raise forms.ValidationError('Начало не может быть в прошлом.')

        return data

    def clean_last_name(self):
        data = self.cleaned_data['last_name']
        if not data.isalpha():
            raise forms.ValidationError('Фамилия может иметь только буквы.')
        return data

    def clean_first_name(self):
        data = self.cleaned_data['first_name']
        if not data.isalpha():
            raise forms.ValidationError('Имя может иметь только буквы')
        return data
    # foreign key to user's username
    # foreign key to the living place

    class Meta:
        model = Booking
        fields = ['first_name', 'last_name', 'email', 'phone', 'starting_date', 'end_date']
        exclude = ('total_sum', 'choice')
        widgets = {
            'starting_date': DateInput(attrs={'class': 'picker'}),
            'end_date': DateInput()
        }
