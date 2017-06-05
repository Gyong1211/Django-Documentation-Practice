from django.contrib import admin
#from introduction_to_models.models import Person
from .models import Person
# Register your models here.

admin.site.register(Person)