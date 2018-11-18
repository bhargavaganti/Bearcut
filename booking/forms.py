from django import forms
from django.contrib.auth.forms import UserChangeForm
from phonenumber_field.formfields import PhoneNumberField
from account.models import User
from .models import Book


class BookForm(forms.ModelForm):

    date = forms.DateField(widget=forms.SelectDateWidget())
    time = forms.TimeField(widget=forms.TimeInput(format='%H:%M'))
    phone_number = PhoneNumberField()

    class Meta:
        fields = ('date','time','phone_number',)
        model = Book


class ConfirmForm(forms.ModelForm):

    PAYMENT = [
        ('cash','CASH'),
        ('credit_card','CREDIT CARD')
    ]

    payment_type = forms.ChoiceField(choices=PAYMENT, widget=forms.RadioSelect())

    class Meta:
        fields = ('payment_type',)
        model = Book


class NameForm(UserChangeForm):
    password = None

    class Meta:
        model = User
        fields = ('first_name','last_name',)
