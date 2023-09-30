from django.shortcuts import render
from .models import *
from django.views import generic


def index(req):
    numpat = Patient.objects.all().count()
    numdoc = Doctor.objects.all().count()
    nummed = Medicines.objects.all().count()
    data = {'k1': numpat, 'k2': numdoc, 'k3': nummed}
    print()
    return render(req, 'index.html', context=data)


class Patientlist(generic.ListView):
    model = Patient


class PatientDetail(generic.DetailView):
    model = Patient


class Doctorlist(generic.ListView):
    model = Doctor


class Medicineslist(generic.ListView):
    model = Medicines



