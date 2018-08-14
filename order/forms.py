from django import forms
from .models import Order
from django.contrib.auth.models import User
from customer.models import Customer
from django.utils.translation import gettext as _


class OrderCreateForm(forms.Form):
    customer = Customer.fl_name
    phone = Customer.phone
    email = forms.EmailField()
    delivery_service = Order.delivery_service
    delivery_address = Order.delivery_address
    payment_method = Order.payment_method

    def clean_email(self):
        user_model = User  # your way of getting the User
        try:
            user_model.objects.get(email__iexact=self.data.get("email"))
        except user_model.DoesNotExist:
            raise forms.ValidationError(_(""))
        return self.data.get("email")

    def clean_phone(self):
        user_model = Customer  # your way of getting the User
        try:
            user_model.objects.get(phone__iexact=self.data.get("phone"))
        except user_model.DoesNotExist:
            return self.data.get("phone")
        raise forms.ValidationError(_("Эта номер телефона уже используется. Если это ваш номер, войдите в аккаунт"))
