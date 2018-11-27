from django.contrib import admin
from accounts.models import User, UserProfile, Contact

admin.site.register(UserProfile)
admin.site.register(Contact)