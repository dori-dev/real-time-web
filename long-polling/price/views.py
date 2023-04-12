from datetime import timedelta
import asyncio

from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from django.utils.timezone import now
from asgiref.sync import sync_to_async

from price import models


class PriceView(View):
    async def get(self, request):
        return render(request, 'price/index.html')


@sync_to_async
def get_content(from_date):
    return models.PriceAction.objects.filter(
        created__gt=from_date,
    )


class Data(View):
    def get(self, request):
        items = models.PriceAction.objects.filter(
            created__gt=now() - timedelta(days=1),
        )
        return JsonResponse(list(items.values()), safe=False)


class NewData(View):
    async def get(self, request):
        from_date = request.GET.get('from')
        if from_date is None:
            return JsonResponse([], safe=False)
        items = []
        for _ in range(8):
            result = await get_content(from_date)
            if result.count():
                items = list(result.values())
                break
            await asyncio.sleep(5)
        return JsonResponse(items, safe=False)
