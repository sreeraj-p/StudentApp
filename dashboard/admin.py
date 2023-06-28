from django.contrib import admin
from .models import Notes,Homework

@admin.register(Notes)
class NotesAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'description')

@admin.register(Homework)
class HomeworkAdmin(admin.ModelAdmin):
    list_display=('user','subject','title','description','due')
