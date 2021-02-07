from django.contrib import messages
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.models import Group
from django.shortcuts import redirect


class RealtorPermissionMixin:

    def has_permission(self):
        """
        Override this method to customize the way permissions are checked.
        """
        realtor_group = Group.objects.get(name='realtor')
        return realtor_group in self.request.user.groups.all()

    def dispatch(self, request, *args, **kwargs):
        if not self.has_permission():
            messages.error(request, "У Вас нет доступа доля данного действия, нужно быть риэлтором.")
            return redirect(request.META.get('HTTP_REFERER'))
        return super().dispatch(request, *args, **kwargs)
