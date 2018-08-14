from django import forms
from django.contrib.auth.models import User
from django.utils.translation import gettext as _

class NewUserValidation(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    password = forms.CharField(max_length=30)
    password2 = forms.CharField(max_length=30)

    class Meta:
        model = User
        fields = ('username')

    def clean_username(self):
        user_model = User # your way of getting the User
        try:
            user_model.objects.get(username__iexact=self.data.get("username"))
        except user_model.DoesNotExist:
            return self.data.get("username")
        raise forms.ValidationError(_("Пользователь с таким именем существует."))

    def clean_email(self):
        user_model = User  # your way of getting the User
        try:
            user_model.objects.get(email__iexact=self.data.get("email"))
        except user_model.DoesNotExist:
            return self.data.get("email")
        raise forms.ValidationError(_("Эта электронная почта уже используется."))
