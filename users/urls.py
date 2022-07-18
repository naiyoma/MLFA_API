from django.urls import path
from .views import UserViewSet


app_name='users'

urlpatterns = [
    path('list', UserViewSet.as_view({'get': 'list'})),
]