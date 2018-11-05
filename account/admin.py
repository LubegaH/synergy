from django.contrib import admin
from .models import Profile

# Models registered here

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth', 'interest', 'bio', 'photo']
