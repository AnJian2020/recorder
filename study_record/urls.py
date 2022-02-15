from django.urls import path
from .views import *

urlpatterns = [
    path('read', ReadNoteView.as_view())
]