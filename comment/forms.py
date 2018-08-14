from django import forms
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
from item.models import Item
from .models import Comment
#
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("name","phone_email","text")











#
#
# class NewCommentValid(forms.Form):
#     username = forms.CharField(max_length=100)
#     email = forms.EmailField(max_length=100)
#     item = forms.CharField()
#     comment = forms.Textarea()
#
#     def clean_username(self):
#         user_model = User  # your way of getting the User
#         try:
#             user_model.objects.get(username__iexact=self.data.get("username"))
#         except user_model.DoesNotExist:
#             raise forms.ValidationError(_("Пользователя не существует или аккаунт неактивен."))
#         return self.data.get("username")
#
#     def clean_email(self):
#         user_model = User  # your way of getting the User
#         try:
#             user_model.objects.get(email__iexact=self.data.get("email"))
#         except user_model.DoesNotExist:
#             raise forms.ValidationError(_("Почта не существует или аккаунт неактивен."))
#         return self.data.get("email")
#
#     def clean_item(self):
#         item_model = Item
#         try:
#             item_model.objects.get(id=int(self.data.get("item")))
#         except item_model.DoesNotExist:
#             raise forms.ValidationError(_("Несуществующий товар"))
#         return self.data.get("item")
#
#     def clean_comment(self):
#         return self.data.get("comment")
