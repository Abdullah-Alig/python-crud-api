import imp
from django.shortcuts import render
from rest_framework import viewsets
from api.models import User
from api.serializers import UserSerializer

# Create your views here.

class UserViewsSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
