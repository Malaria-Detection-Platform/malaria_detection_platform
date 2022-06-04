from rest_framework.permissions import BasePermission


class isDoctor(BasePermission):
    def has_permission(self, request, view):

        return bool(request.user.role == ("doctor") and request.user)


class isHospital(BasePermission):
    def has_permission(self, request, view):

        return bool(request.user.role == ("hospital") and request.user)


class isAdmin(BasePermission):
    def has_permission(self, request, view):

        return bool(request.user.role == ("admin") and request.user)


class isLabTech(BasePermission):
    def has_permission(self, request, view):

        return bool(request.user.role == ("lab_tech") and request.user)


class isReceptionist(BasePermission):
    def has_permission(self, request, view):

        return bool(request.user.role == ("receptionist") and request.user)
