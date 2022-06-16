from django.urls import path
from .views import showform, HotelSystemSuccessView


urlpatterns = [
    path('', showform, name='home'),
    path('success/', HotelSystemSuccessView.as_view(), name='success')
]
