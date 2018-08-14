from django.db import models
from st_app.models import CommonFields


class Status(CommonFields):
    description = None
    is_active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "Status"
        verbose_name_plural = "Status"
