from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=150)
    age = models.PositiveIntegerField(default=10)

    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.name
