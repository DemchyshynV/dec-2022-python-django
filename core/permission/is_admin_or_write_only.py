from rest_framework.permissions import BasePermission
from rest_framework.request import Request

from core.dataclasses.user_dataclass import UserDataClass


class IsAdminOrWriteOnlyPermission(BasePermission):
    def has_permission(self, request: Request, view):
        if request.method == 'POST':
            return True
        user: UserDataClass = request.user
        return user.is_staff
