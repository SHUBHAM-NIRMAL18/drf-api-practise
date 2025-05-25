from django.urls import path
from .api import *



urlpatterns = [
    path('create', CreateUserApi),
    path('protected', ProtectedUserApi),
    
]

