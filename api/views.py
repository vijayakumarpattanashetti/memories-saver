from rest_framework import generics, permissions
from .permissions import IsOwner
from .serializers import MemoriesSerializer, UserSerializer
from django.contrib.auth.models import User
from .models import Memories
from django.http import HttpResponse


class CreateView(generics.ListCreateAPIView):
    #define create behavior of the rest api
    queryset = Memories.objects.all()
    serializer_class = MemoriesSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner)

    def perform_create(self, serializer):
        #save the post data when creating a new memory
        serializer.save(owner=self.request.user)

class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    #handle the http GET, PUT and DELETE requests
    queryset = Memories.objects.all()
    serializer_class = MemoriesSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner)


class UserView(generics.ListAPIView):
    #view to list the user queryset
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailsView(generics.RetrieveAPIView):
    #view to retrieve a user instance
    queryset = User.objects.all()
    serializer_class = UserSerializer


def Home(x):
    return HttpResponse("Welcome to Memories Saver! Go to /memories")
