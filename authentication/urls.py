from django.urls import path
from . import views

app_name = 'authentication'
urlpatterns = [
    path('sign-up', views.SignUpView.as_view(), name = 'signup'),
    path('logout', views.logout_view, name='logout'),
]