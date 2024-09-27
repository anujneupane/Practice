from django.contrib import admin

# Register your models here.
from .models import Student

# creating model admin class
@admin.register(Student)  #using decorator
class StudentAdmin(admin.ModelAdmin):
    list_display = ('stuid','stuname','stumail','stupass')
    
# admin.site.register(Student,StudentAdmin)