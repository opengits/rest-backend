from rest_framework import viewsets
from sharedorm.models import User
from rest_framework.response import Response

class UserViewSet(viewsets.ViewSet):
    def list(self, request):
        users = User.objects.all()
        user_data = [{"first_name": user.first_name, "last_name": user.last_name, "email": user.email} for user in users]
        return Response(user_data)
