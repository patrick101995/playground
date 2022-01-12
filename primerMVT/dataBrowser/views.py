from django.shortcuts import render
from django.http import HttpResponse
from dataBrowser.models import Familiar


# Create your views here.

def familiares(request):
    
    miembros = Familiar.objects.all

    return render(request,'datosFamiliar.html', {'miembros':miembros})