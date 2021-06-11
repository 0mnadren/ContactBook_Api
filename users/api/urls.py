from django.urls import path
from users.api import views
from rest_framework.authtoken.views import obtain_auth_token

app_name = 'users_api'

urlpatterns = [
    path('register/', views.registration_view, name='register_api'),
    path('login/', obtain_auth_token, name='login_api'),
]
