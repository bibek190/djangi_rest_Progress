from django.shortcuts import render
from rest_framework import viewsets,filters
from .models import Server
from .serializers import ServerSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer


class ServerViewSet(viewsets.ModelViewSet):
    queryset = Server.objects.all()
    serializer_class = ServerSerializer
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]

# filtering
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ["is_active"]
    search_fields = ['name','location']