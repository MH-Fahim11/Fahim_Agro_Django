from django.contrib import admin

# Register your models here.
from .models import Coustomer
class CoustomerAdmin(admin.ModelAdmin):
  list_display = ("firstname", "lastname", "joined_date",)
admin.site.register(Coustomer, CoustomerAdmin)