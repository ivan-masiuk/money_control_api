from django.db import models


class Transaction(models.Model):
    """
    Money moving (transactions)
    """
    customer_fk = models.ForeignKey(
        "user.Customer", on_delete=models.CASCADE, blank=True, null=True,
    )
    amount = models.PositiveIntegerField(default=0)
    TYPE_CHOICES = [
        ("income", "Income"),
        ("expense", "Expense"),
    ]
    type = models.CharField(
        default="income",
        max_length=25,
        blank=True,
        null=True,
        verbose_name="Type transaction",
        choices=TYPE_CHOICES,
    )
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True, blank=True, null=True)
