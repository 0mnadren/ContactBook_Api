from django.shortcuts import render
from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, generics, mixins
from .models import Person, Contact
from .serializers import PersonSerializer, ContactSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated


######## PERSON ###########
class PersonApiView(generics.GenericAPIView,
                    mixins.ListModelMixin,
                    mixins.CreateModelMixin):

    serializer_class = PersonSerializer
    queryset = Person.objects.filter(active=True)
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class PersonApiDetail(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self, id):
        try:
            return Person.objects.get(id=id)
        except Person.DoesNotExist:
            raise Http404

    def get(self, request, id):
        person = self.get_object(id)
        serializer = PersonSerializer(person)
        return Response(serializer.data)

    def put(self, request, id):
        person = self.get_object(id)
        serializer = PersonSerializer(person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        person = self.get_object(id)
        serializer = PersonSerializer(person, data={'active': False}, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


######### CONTACT ###########
class ContactApiView(generics.GenericAPIView,
                    mixins.ListModelMixin,
                    mixins.CreateModelMixin):

    serializer_class = ContactSerializer
    queryset = Contact.objects.filter(active=True)
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class ContactApiDetail(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self, id):
        try:
            return Contact.objects.get(id=id)
        except Contact.DoesNotExist:
            raise Http404

    def get(self, request, id):
        contact = self.get_object(id)
        serializer = ContactSerializer(contact)
        return Response(serializer.data)

    def put(self, request, id):
        contact = self.get_object(id)
        serializer = ContactSerializer(contact, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        contact = self.get_object(id)
        serializer = ContactSerializer(contact, data={'active': False}, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


######### ADDRESS #####################
class AddressApiView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if request.query_params.get('is_older_than'):
            is_older_than = request.query_params.get('is_older_than')

            persons = Person.objects.filter(birthdate__lt=is_older_than)
            serializer_per = PersonSerializer(persons, many=True)

            contacts = Contact.objects.filter(birthdate__lt=is_older_than)
            serializer_cont = ContactSerializer(contacts, many=True)

            return Response([serializer_per.data, serializer_cont.data])
        return Response(status=status.HTTP_400_BAD_REQUEST)



