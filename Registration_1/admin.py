from django.contrib import admin

from Registration_1.models import Course, Batch, Student
# Register your models here.
admin.site.register(Course)
admin.site.register(Batch)
admin.site.register(Student)