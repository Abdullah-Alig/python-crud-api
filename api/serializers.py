from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from api.models import User

# Create Seriazers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    # Meta Class is basically used to change the behavior of model fields
    id=  serializers.ReadOnlyField()
    class Meta:
        model=User
        # for all fields(fields not field) of User models using __all__
        fields = '__all__'