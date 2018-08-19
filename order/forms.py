from django import forms
import re

class OrderCreateForm(forms.Form):
    customer = forms.CharField()
    phone = forms.CharField(max_length=14)
    email = forms.CharField(widget=forms.EmailInput)
    delivery_service = forms.CharField(widget=forms.TextInput)
    delivery_address = forms.CharField(widget=forms.TextInput)
    payment_method = forms.CharField(widget=forms.TextInput)

    def clean_email(self):
        if not self.data.get("email"):
            raise forms.ValidationError("Email field is required")
        return self.data.get("email")

    def clean_customer(self):
        if not self.data.get("customer"):
            raise forms.ValidationError("First name and last name fields are required")
        return self.data.get("customer")


    def clean_phone(self):
        m = re.match("(\+\d{2})(\s*\d{10})", self.data.get("phone"))
        if m and m.group(1) == "+38" and len(m.group(2)) == 10:
                return self.data.get("phone")
        raise forms.ValidationError("Phone is not correct")

    def clean_delivery_address(self):
        if not self.data.get("delivery_address"):
            raise forms.ValidationError("Delivery address is required")
        return self.data.get("delivery_address")

    def clean_delivery_service(self):
        if not self.data.get("delivery_service"):
            raise forms.ValidationError("Delivery service name is required")
        return self.data.get("delivery_service")

    def clean_payment_method(self):
        if not self.data.get("payment_method"):
            raise forms.ValidationError("Payment method is required")
        return self.data.get("payment_method")

