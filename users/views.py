from users.models import MyUser
from .serializers import UserSerializer
from rest_framework import viewsets
from rest_framework.response import Response
# from rest_framework.permissions import IsAdminUser

class UserViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = MyUser.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)