from django import forms
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
import re
from django.contrib.auth.hashers import make_password, check_password


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.TextInput)


class PersonalInfoChange(forms.Form):
    full_name = forms.CharField(max_length=50)
    email = forms.CharField(widget=forms.EmailInput)
    phone = forms.CharField(max_length=14, widget=forms.TextInput)
    old_pass = forms.CharField(widget=forms.PasswordInput)
    new_pass = forms.CharField(widget=forms.PasswordInput, required=False)
    new_pass2 = forms.CharField(widget=forms.PasswordInput, required=False)

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(PersonalInfoChange, self).__init__(*args, **kwargs)

    def clean_old_pass(self):

        if not check_password(self.data.get("old_pass"), User.objects.get(email=self.user.email).password):
            raise forms.ValidationError('Password is wrong. Carefully!')
        return self.data.get("old_pass")

    def clean_new_pass2(self):
        cd = self.cleaned_data
        if cd['new_pass'] != cd['new_pass2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['new_pass']

    def clean_phone(self):
        m = re.match("(\+\d{2})(\s*\d{10})", self.data.get("phone"))

        if m and m.group(1) == "+38" and len(m.group(2)) == 10:
            try:
                User.objects.get(customer__phone=self.data.get("phone"))
            except User.DoesNotExist:
                return self.data.get("phone")
            raise forms.ValidationError("Phone already is used")
        raise forms.ValidationError("Phone is not correct")

    def clean_email(self):
        if self.data.get("email") == self.user.email:
            return self.data.get("email")
        try:
            User.objects.get(email__iexact=self.data.get("email"))
        except User.DoesNotExist:
            return self.data.get("email")
        raise forms.ValidationError(_("This email already is used."))


class UserRegistrationForm(forms.Form):
    phone_number = forms.CharField(max_length=14, widget=forms.TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))
    email = forms.CharField(widget=forms.EmailInput(attrs={"class": "form-control"}))
    full_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={"class": "form-control"}))

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']

    def clean_email(self):
        try:
            User.objects.get(email__iexact=self.data.get("email"))
        except User.DoesNotExist:
            return self.data.get("email")
        raise forms.ValidationError(_("This email already is used."))

    def clean_phone_number(self):
        m = re.match("(\+\d{2})(\s*\d{10})", self.data.get("phone_number"))
        if m.group(1) == "+38" and len(m.group(2)) == 10:
            return self.data.get("phone_number")
        raise forms.ValidationError("Phone is not correct")
