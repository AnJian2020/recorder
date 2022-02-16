from django.urls import path
from .views import *

urlpatterns = [
    path('read', ReadNoteListView.as_view(), name='read_list'),
    path('read/<int:id>/detail', ReadNoteDetailView.as_view(), name='read_detail'),
    path('read/<int:id>/edit', ReadNoteEditView.as_view(), name='read_edit'),
    path('read/<int:id>/delete', ReadNoteDeleteView.as_view(), name='read_delete')
]
