from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    message = 'Вы не являетесь автором!'

    def has_object_permission(self, request, view, instance):
        if request.user == instance.user:
            return True
        return False
