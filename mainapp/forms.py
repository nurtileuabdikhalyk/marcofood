from django import forms
from .models import Address, Question
from django.contrib.auth.models import User


class AddressForm(forms.ModelForm):
    class Meta:
        CITY = [
            ('ALA', 'Алматы'),
            ('NQZ', 'Нур-Султан'),
            ('CIT', 'Шымкент'),
        ]
        model = Address
        fields = ("phone", "city", "street", "home_number", "floor", "door")
        widgets = {
            "phone": forms.TextInput(attrs={"class": "form-control border", "placeholder": "Телефон №"}),
            "city": forms.Select(attrs={"class": "form-control border", "placeholder": "Город"}),
            "street": forms.TextInput(attrs={"class": "form-control border", "placeholder": "Улица"}),
            # "home_number": forms.IntegerField(),
            "home_number": forms.TextInput(attrs={"class": "form-control border", "placeholder": "Дом №"}),
            "floor": forms.TextInput(attrs={"class": "form-control border", "placeholder": "Этаж №"}),
            "door": forms.TextInput(attrs={"class": "form-control border", "placeholder": "Квартира №"}),

        }


class SignUpForm(forms.ModelForm):
    # first_name=forms.CharField(max_length=30)
    class Meta:
        model = User
        fields = ('first_name', 'username', 'email', 'password',)
        # widgets = {
        #     "name": forms.TextInput(attrs={"class": "common-input mb-20 form-control", "placeholder": "Имя"}),
        #     "email": forms.TextInput(attrs={"class": "form-control border", "placeholder": "Email"}),
        #     "topic": forms.TextInput(attrs={"class": "form-control border", "placeholder": "Тема"}),
        #     "message": forms.Textarea(attrs={"class": "form-control border", "placeholder": "Сообщение"}),
        # }

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = "__all__"

        widgets = {
            "name": forms.TextInput(attrs={"class": "common-input mb-20 form-control", "placeholder": "Имя"}),
            "email": forms.TextInput(attrs={"class": "form-control border", "placeholder": "Email"}),
            "topic": forms.TextInput(attrs={"class": "form-control border", "placeholder": "Тема"}),
            "message": forms.Textarea(attrs={"class": "form-control border", "placeholder": "Сообщение"}),
        }
