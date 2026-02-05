from django.shortcuts import render
from django.core.paginator import Paginator
from .models import *

def main_page(request):
    aircraft = Aircraft.objects.all()
    context = {
        "aircraft": aircraft
    }
    return render(request, "main_page.html", context)
