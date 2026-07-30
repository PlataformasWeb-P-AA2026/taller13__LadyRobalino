from django.shortcuts import render

from django.contrib.auth.models import User, Group
from rest_framework import permissions, viewsets
from rest_framework.authentication import SessionAuthentication, TokenAuthentication

from administrativo.models import Edificio, Departamento
from administrativo.serializers import (
    UserSerializer,
    GroupSerializer,
    EdificioSerializer,
    DepartamentoSerializer,
)


def index(request):
    edificios = Edificio.objects.all().order_by('nombre')
    departamentos = Departamento.objects.select_related('edificio').all().order_by('nombre_propietario')
    informacion_template = {
        'edificios': edificios,
        'numero_edificios': edificios.count(),
        'departamentos': departamentos,
        'numero_departamentos': departamentos.count(),
    }
    return render(request, 'index.html', informacion_template)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication, SessionAuthentication]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication, SessionAuthentication]


class EdificioViewSet(viewsets.ModelViewSet):
    queryset = Edificio.objects.all()
    serializer_class = EdificioSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication, SessionAuthentication]


class DepartamentoViewSet(viewsets.ModelViewSet):
    queryset = Departamento.objects.select_related('edificio').all()
    serializer_class = DepartamentoSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication, SessionAuthentication]
