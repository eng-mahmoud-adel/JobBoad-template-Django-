from django.contrib import admin
from .models import Job, Category, ApplyForJob

# Register your models here.
admin.site.register(Job)
admin.site.register(Category)
admin.site.register(ApplyForJob)