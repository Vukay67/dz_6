from django.urls import path
from .views import main_page, aircraft_page

urlpatterns = [
    path('', main_page, name="main_page"),
    path('aircraft/<int:id>/', aircraft_page, name="aircraft_page")
]