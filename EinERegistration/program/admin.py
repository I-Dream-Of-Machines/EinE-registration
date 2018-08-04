from django.contrib import admin
from .models import Program
from .models import Iteration
from .models import ProgramLevel

# Register your models here.
admin.site.register(Program)
admin.site.register(Iteration)
admin.site.register(ProgramLevel)
