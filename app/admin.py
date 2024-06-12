from django.contrib import admin
from .models import Animal,AnimalType,User,AdoptingRequest
# Register your models here.
admin.site.register(Animal)
admin.site.register(AnimalType)
admin.site.register(User)
admin.site.register(AdoptingRequest)
