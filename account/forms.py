from django import forms
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
import re

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.TextInput)


class UserRegistrationForm(forms.Form):
    phone_number = forms.CharField(max_length=14,widget=forms.TextInput(attrs={"class":"form-control"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))
    email = forms.CharField(widget=forms.EmailInput(attrs={"class":"form-control"}))
    full_name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))


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
        m = re.match("(\+\d{2})(\s*\d{10})",self.data.get("phone_number"))
        if m.group(1) == "+38" and len(m.group(2)) == 10:
            return self.data.get("phone_number")

