from django.urls import path
from .views import *

urlpatterns = [
    path('read', ReadNoteListView.as_view()),
    path('read/<int:id>/detail', ReadNoteDetailView.as_view()),
    path('read/<int:id>/edit', ReadNoteEditView.as_view())
]