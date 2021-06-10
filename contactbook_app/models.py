from django.db import models


class AddressEntry(models.Model):
    GENDER_CHOICES = (
        ('m', 'male'),
        ('f', 'female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='f')
    name = models.CharField(max_length=125)
    firstname = models.CharField(max_length=125)
    birthdate = models.DateField()
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Person(AddressEntry):
    lastname = models.CharField(max_length=125)
    job = models.CharField(max_length=125, blank=True)

    def __str__(self):
        return f'{self.firstname} {self.lastname} -- {self.birthdate}'


class Contact(AddressEntry):
    address = models.CharField(max_length=225)
    email = models.EmailField(max_length=225, blank=True)

    def __str__(self):
        return f'{self.firstname} -- Address: {self.address} {self.email}'


