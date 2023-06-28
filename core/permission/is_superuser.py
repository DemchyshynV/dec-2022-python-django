from rest_framework.permissions import BasePermission, IsAdminUser


# class IsSuperUser(IsAdminUser):
class IsSuperUser(BasePermission):
    # def has_permission(self, request, view):
    #     return bool(super().has_permission(request, view) and request.user.is_superuser)

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_staff and request.user.is_superuser)
