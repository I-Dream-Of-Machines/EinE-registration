from django.contrib import admin
from .models import RegionalMember, Guardian

# Register your models here.
admin.site.register(RegionalMember)
admin.site.register(Guardian)