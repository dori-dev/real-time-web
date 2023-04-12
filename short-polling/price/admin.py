from django.contrib import admin
from price import models

admin.site.register(models.Currency)
admin.site.register(models.PriceAction)
