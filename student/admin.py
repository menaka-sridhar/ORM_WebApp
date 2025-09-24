from django.contrib import admin
from.models import StudentDetail, StudentDetailsAdmin

# Register your models here.

admin.site.register(StudentDetail, StudentDetailsAdmin)
