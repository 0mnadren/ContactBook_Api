from django.urls import path
from . import views

app_name = 'contact_book'

urlpatterns = [
    path('persons/', views.persons_list, name='persons'),
    path('persons/<int:id>', views.person_detail, name='person_detail'),
    path('contacts/', views.contacts_list, name='contacts'),
    path('contacts/<int:id>', views.contact_detail, name='contact_detail'),
]
