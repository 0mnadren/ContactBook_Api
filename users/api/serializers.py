from rest_framework import serializers
from django.contrib.auth.models import User


class RegistrationSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(
        style={'input_type': 'email'}
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        write_only_fields = ('password',)

    def create(self, validated_data):
        user = User.objects.create(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
        )

        user.set_password(validated_data['password'])
        user.save()

        return user
