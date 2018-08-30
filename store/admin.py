from django.contrib import admin
from .models import Group,Membership


# Register your models here.

admin.site.register(Membership)
admin.site.register(Group)
