from django.urls import path
from . import views

app_name = 'contact_book'

urlpatterns = [
    path('persons/', views.PersonApiView.as_view(), name='persons'),
    path('persons/<int:id>', views.PersonApiDetail.as_view(), name='person_detail'),
    path('contacts/', views.ContactApiView.as_view(), name='contacts'),
    path('contacts/<int:id>', views.ContactApiDetail.as_view(), name='contact_detail'),
    path('addresses/', views.AddressApiView.as_view(), name='addresses'),
]
