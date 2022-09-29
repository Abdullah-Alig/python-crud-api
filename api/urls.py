
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path,include
from api.views import UserViewsSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'user',UserViewsSet)


urlpatterns = [
    path('',include(router.urls))
]
