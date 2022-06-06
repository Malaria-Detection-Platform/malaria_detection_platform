from rest_framework.permissions import BasePermission, SAFE_METHODS


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


class hasWritePermission(BasePermission):
    message = "You do not have permission to override this."

    def has_object_permission(self, request, view, obj):

        if request.method in SAFE_METHODS:
            return True

        return obj.user == request.user


class isEmployee(BasePermission):
    message = "This personnel is not accessible to you."

    def has_object_permission(self, request, view, obj):

        if request.method in SAFE_METHODS:
            return True

        return obj.hospital == request.user


class isOwnerPersonnel(BasePermission):
    message = "You do not have permission to override this."

    def has_object_permission(self, request, view, obj):

        if request.method in SAFE_METHODS:
            return True

        return obj.hospital == request.hospital


class isDoctorOfPatient(BasePermission):
    message = "You do not have permission to override this."

    def has_object_permission(self, request, view, obj):

        if request.method in SAFE_METHODS:
            return True

        return obj.doctor == request.user


class isPrescriptionOfDoctor(BasePermission):
    message = "You do not have permission to override this."

    def has_object_permission(self, request, view, obj):

        if request.method in SAFE_METHODS:
            return True

        return obj.doctor == request.user


class hasChecupListAccess(BasePermission):
    message = "You do not have permission to override this."

    def has_object_permission(self, request, view, obj):

        if request.method in SAFE_METHODS:
            return True

        patient = obj.patient
        doctor = patient.doctor
        return doctor == request.user
