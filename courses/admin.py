from django.contrib import admin

# Register your models here.
from .models import Course, Evaluate


@admin.register(Course)
class AdminCourse(admin.ModelAdmin):
    list_display = ('title', 'url', 'publicated', 'update', 'active')


@admin.register(Evaluate)
class AdminEvaluate(admin.ModelAdmin):
    list_display = ('course', 'name', 'email', 'evaluate',
                    'publicated', 'update', 'active')
