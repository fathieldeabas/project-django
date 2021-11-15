from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(cars)
admin.site.register(emp)
admin.site.register(project)