from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    message = "The user is not the owner of the resource."

    def has_object_permission(self, request, view, obj):
        # If request is safe (OPTIONS, HEAD, GET), just allow it
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user == obj.owner
