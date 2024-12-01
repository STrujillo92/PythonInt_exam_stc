from django.shortcuts import render, redirect
from mesero.models import Mesero
from django.db.models import Q, F

# Create your views here.
def mesero_list(request):
    #data_context = Mesero.objects.all()
    query = Q(nacionalidad='peruana') & Q(edad__lt=30)
    data_context = Mesero.objects.filter(query)
    return render(request, 'mesero/mesero_list.html', context={'data': data_context})

def mesero_details(request):
    data_context=Mesero.objects.all()
    return render(request, 'mesero/mesero_details.html',context={'data':data_context})

def mesero_age_update(request):
    Mesero.objects.all().update(edad=F('edad')+5)
    return redirect('mesero_details.html')


