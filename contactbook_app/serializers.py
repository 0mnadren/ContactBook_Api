from rest_framework import serializers
from .models import Person, Contact


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'address', 'email', 'birthdate', 'active', 'person']

