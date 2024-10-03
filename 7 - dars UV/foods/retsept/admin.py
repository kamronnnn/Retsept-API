from django.contrib import admin
from .models import Food, Retsept, Comment

# Register your models here.

admin.site.register(Food)
admin.site.register(Retsept)
admin.site.register(Comment)
