from django.shortcuts import render
from django.core.paginator import Paginator
from .models import *

def main_page(request):
    aircraft = Aircraft.objects.all()

    n_model = request.GET.get("name")
    n_company = request.GET.get("company")
    price = request.GET.get("price")

    if n_model is not None and len(n_model) > 0:
        aircraft = aircraft.filter(model__icontains =n_model)

    if n_company is not None:
        if n_company == "Airbus":
            aircraft = aircraft.filter(companys__icontains =n_company)
        elif n_company == "Boeing":
            aircraft = aircraft.filter(companys__icontains =n_company)
        elif n_company == "Embraer":
            aircraft = aircraft.filter(companys__icontains =n_company)
        elif n_company == "Bombardier":
            aircraft = aircraft.filter(companys__icontains =n_company)
        elif n_company == "ATR":
            aircraft = aircraft.filter(companys__icontains =n_company)
        elif n_company == "Сухой":
            aircraft = aircraft.filter(companys__icontains =n_company)
        elif n_company == "Иркут":
            aircraft = aircraft.filter(companys__icontains =n_company)
        elif n_company == "COMAC":
            aircraft = aircraft.filter(companys__icontains =n_company)
        elif n_company == "Gulfstream":
            aircraft = aircraft.filter(companys__icontains =n_company)
        elif n_company == "Dassault":
            aircraft = aircraft.filter(companys__icontains =n_company)
        elif n_company == "Cessna":
            aircraft = aircraft.filter(companys__icontains =n_company)

    if price is not None:
        if price == "price_asc":
            aircraft = aircraft.order_by('current_rate')
        elif price == "price_desc":
            aircraft = aircraft.order_by('-current_rate')

    context = {
        "aircraft": aircraft
    }
    return render(request, "main_page.html", context)
