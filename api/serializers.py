from rest_framework import serializers
from .models import Memories
from django.contrib.auth.models import User


class MemoriesSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Memories
        fields = ('id', 'text', 'owner', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')

class UserSerializer(serializers.ModelSerializer):
    """A user serializer to aid in authentication and authorization."""
    memories = serializers.PrimaryKeyRelatedField(
    many=True, queryset=Memories.objects.all())

    class Meta:
        """Map this serializer to the default django user model."""
        model = User
        fields = ('id', 'username', 'memories')
