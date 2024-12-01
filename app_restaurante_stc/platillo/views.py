from django.shortcuts import render, redirect
from platillo.models import Platillo
from platillo.forms import PlatilloForm
from django.db.models import Q


# Create your views here.
def platillo_list(request):
    #data_context = Platillo.objects.all()
    query =Q(procedencia='Peru') & Q(precio__gt=40)
    data_context = Platillo.objects.filter(query)
    return render(request, 'platillo/platillo_list.html', context={'data': data_context})

def platillo_details(request):
    data_context=Platillo.objects.all()
    return render(request, 'platillo/platillo_details.html',context={'data':data_context})

def platillo_create(request):
    form = PlatilloForm(request.POST)

    if form.is_valid():
        nombre = form.cleaned_data['nombre']
        precio = form.cleaned_data['precio']
        procedencia = form.cleaned_data['procedencia']

        form.save()
        return redirect('platillo_details')
    else:
        form = PlatilloForm()

    return render(request,'platillo/platillo_create.html',{'form':form})

def platillo_delete15(request):
    platillo = Platillo.objects.get(precio__lt=15)
    platillo.delete()

    return redirect('platillo_details')
