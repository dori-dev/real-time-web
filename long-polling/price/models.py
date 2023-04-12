from django.db import models


class Currency(models.Model):
    title = models.CharField(
        max_length=255,
    )
    code = models.CharField(
        max_length=8,
    )

    def __str__(self) -> str:
        return self.code


class PriceAction(models.Model):
    currency = models.ForeignKey(
        Currency,
        on_delete=models.CASCADE,
    )
    price = models.IntegerField()
    created = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self) -> str:
        return f"{self.currency} - {self.price}"
