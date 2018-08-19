from django.db import models
from django.contrib.auth.models import User
from django.core.validators import EmailValidator
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save

# from django.contrib.auth.hashers import make_password, check_password
from django.db import transaction


class BaseAccount(models.Model):
    ACCOUNT_TYPES = (
        (0, "made order"),
        (1, "registered")
    )
    customer = models.OneToOneField(User, related_name="customer", on_delete=models.CASCADE, primary_key=True)
    customer_type = models.IntegerField(blank=True, null=True, choices=ACCOUNT_TYPES)
    fl_name = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=14,blank=True, null=True)

    def __str__(self):
        return "{}".format(self.customer)

    class Meta:
        abstract = True


class RegisteredAccount(models.Model):
    class Meta:
        abstract = True


class SocialAccount(models.Model):
    social_profile = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        abstract = True


class Customer(RegisteredAccount, SocialAccount, BaseAccount):

    class Meta:
        db_table = "Customer"
        verbose_name_plural = "Customer"

    def clean(self):
        pass

