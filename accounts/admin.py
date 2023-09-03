from django.contrib import admin
from .models import UserDetails


# Register your models with the custom admin class
admin.site.register(UserDetails)
