from django.forms import model_to_dict
from rest_framework.response import Response
from rest_framework.utils import json

from .models import *
from rest_framework import serializers, status


class PersonSerializer(serializers.Serializer):
    class Meta:
        model = Person
        fields = ['__all__']

    def is_valid(self, raise_exception=True):
        if not self.initial_data.get('f_name'):
            res = {"code": status.HTTP_400_BAD_REQUEST, "message": "Missing First Name"}
            return Response(data=json.dumps(res), status=status.HTTP_400_BAD_REQUEST)
        if not self.initial_data.get('l_name'):
            res = {"code": status.HTTP_400_BAD_REQUEST, "message": "Missing Last Name"}
            return Response(data=json.dumps(res), status=status.HTTP_400_BAD_REQUEST)
        if not self.initial_data.get('gender'):
            res = {"code": status.HTTP_400_BAD_REQUEST, "message": "Missing Gender"}
            return Response(data=json.dumps(res), status=status.HTTP_400_BAD_REQUEST)

        res = {"code": status.HTTP_200_OK, "message": "Person Added successfully"}
        return Response(data=json.dumps(res), status=status.HTTP_200_OK)

    def save(self, **kwargs):
        person = Person.objects.create(f_name=self.initial_data['f_name'], l_name=self.initial_data['l_name'], gender=self.initial_data['gender'])
        return person

    def to_representation(self, instance):
        return model_to_dict(instance)