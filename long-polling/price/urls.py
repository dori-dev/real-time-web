from django.urls import path
from . import views

app_name = 'price'
urlpatterns = [
    path('', views.PriceView.as_view(), name='index'),
    path('data/', views.Data.as_view(), name='data'),
    path('new-data/', views.NewData.as_view(), name='new_data'),
]
