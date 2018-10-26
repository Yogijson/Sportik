from django.contrib import admin
from .models import Sport, Equipment, UserProfile, MyCart

admin.site.register(Sport)
admin.site.register(Equipment)
admin.site.register(UserProfile)
admin.site.register(MyCart)
