from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('roll_no', 'name', 'email', 'course', 'marks', 'grade', 'is_active')
    list_filter = ('course', 'is_active')
    search_fields = ('roll_no', 'name', 'email')
    list_editable = ('is_active',)
    ordering = ('roll_no',)