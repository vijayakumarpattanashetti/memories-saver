from rest_framework.permissions import BasePermission
from .models import Memories


class IsOwner(BasePermission):
    """Custom permission class to allow only owners to edit."""

    def has_object_permission(self, request, view, obj):
        #grant permission if owner
        if isinstance(obj, Memories):
            return obj.owner == request.user
        return obj.owner == request.user
