from django.shortcuts import render, redirect
from mesero.models import Mesero
from django.db.models import Q, F

from django.core import serializers as ssr
from django.http import HttpResponse

from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from mesero.forms import MeseroForm

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from mesero.serializers import MeseroSerializer

from rest_framework import status
from rest_framework.permissions import IsAuthenticated

# Create your views here.
def mesero_list(request):
    data_context = Mesero.objects.all()
    #query = Q(nacionalidad='peruana') & Q(edad__lt=30)
    #data_context = Mesero.objects.filter(query)
    return render(request, 'mesero/mesero_list.html', context={'data': data_context})

def mesero_details(request):
    data_context=Mesero.objects.all()
    return render(request, 'mesero/mesero_details.html',context={'data':data_context})

def mesero_age_update(request):
    Mesero.objects.all().update(edad=F('edad')+5)
    return redirect('mesero_details.html')

def ListMeseroSerializer25(request):
    query = Q(edad__gt=25)
    list_mesero = ssr.serialize('json', Mesero.objects.filter(query),fields=['nombre','nacionalidad','edad','dni'])
    return HttpResponse(list_mesero, content_type='application/json')

class MeseroCreate(CreateView):
    model = Mesero
    form_class = MeseroForm
    template_name = 'mesero/mesero_create.html'
    success_url = reverse_lazy('mesero_list')

class MeseroListP(ListView):
    model = Mesero
    template_name = 'mesero/mesero_listp_vbc.html'

class MeseroUpdate(UpdateView):
    model = Mesero
    form_class = MeseroForm
    template_name = 'mesero/mesero_update_vbc.html'
    success_url = reverse_lazy('mesero_list')

class MeseroDelete(DeleteView):
    model = Mesero
    success_url = reverse_lazy('mesero_list')
    template_name = 'mesero/mesero_confirm_delete.html'

def ListMeseroSerializer(request):
    list_mesero = ssr.serialize('json', Mesero.objects.all(),fields=['nombre','nacionalidad','edad','dni'])
    return HttpResponse(list_mesero, content_type='application/json')

@api_view(['GET','POST'])
def mesero_api_view(request):
    if request.method == 'GET':
        queryset = Mesero.objects.all()
        serializers_class = MeseroSerializer(queryset, many=True)
        return Response(serializers_class.data)

    elif request.method == 'POST':
        serializers_class = MeseroSerializer(data=request.data)
        if serializers_class.is_valid():
            serializers_class.save()
            return Response(serializers_class.data)
        return Response(serializers_class.errors)

@api_view(['GET','PUT','DELETE'])
@permission_classes([IsAuthenticated])
def mesero_details_view(request,pk):
    mesero = Mesero.objects.get(id=pk)
    if mesero:
        if request.method == 'GET':
            serializer_class = MeseroSerializer(mesero)
            return Response(serializer_class.data,status=status.HTTP_200_OK)
        elif request.method == 'PUT':
            serializer_class = MeseroSerializer(mesero,data=request.data)
            if serializer_class.is_valid():
                serializer_class.save()
                return Response(serializer_class.data,status=status.HTTP_202_ACCEPTED)
            return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            mesero.delete()
            return Response('Mesero ha sido eliminado correctamente de la BD.',status=status.HTTP_202_ACCEPTED)


