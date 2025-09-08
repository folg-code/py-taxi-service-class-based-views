from django.shortcuts import render

from django.views import generic
from taxi.models import Driver, Car, Manufacturer


def index(request):
    """View function for the home page of the site."""

    context = {
        "num_drivers": Driver.objects.count(),
        "num_cars": Car.objects.count(),
        "num_manufacturers": Manufacturer.objects.count(),
    }

    return render(request, "taxi/index.html", context=context)


class ManufacturerListView(generic.ListView):
    """View function for the home page of the site."""
    model = Manufacturer
    queryset = Manufacturer.objects.all().order_by("name")
    paginate_by = 5


class CarListView(generic.ListView):
    """View function for the home page of the site."""
    model = Car
    queryset = Car.objects.select_related("manufacturer").all()
    paginate_by = 5


class CarDetailView(generic.DetailView):
    """View function for the home page of the site."""
    model = Car


class DriverListView(generic.ListView):
    """View function for the home page of the site."""
    model = Driver
    paginate_by = 5


class DriverDetailView(generic.DetailView):
    """View function for the home page of the site."""
    model = Driver
    queryset = Driver.objects.prefetch_related("cars__manufacturer")
