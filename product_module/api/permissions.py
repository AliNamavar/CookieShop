# permissions.py
from rest_framework.permissions import BasePermission

class IsStaffUser(BasePermission):
    message = 'دسترسی فقط برای کاربران ادمین مجاز است.'

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.is_staff)
