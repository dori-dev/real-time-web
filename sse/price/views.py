from datetime import timedelta

from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from django.utils.timezone import now

from price import models


class PriceView(View):
    async def get(self, request):
        return render(request, 'price/index.html')


class Data(View):
    def get(self, request):
        items = models.PriceAction.objects.filter(
            created__gt=now() - timedelta(days=1),
        )
        return JsonResponse(list(items.values()), safe=False)
