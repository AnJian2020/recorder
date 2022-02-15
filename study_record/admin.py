from django.contrib import admin
from .models import ReadNoteModel


@admin.register(ReadNoteModel)
class ReadNoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'submit_time', 'edit_time', 'link')
