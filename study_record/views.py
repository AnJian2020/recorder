from django.shortcuts import render
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from .models import ReadNoteModel
from .forms import ReadNoteForm


class ReadNoteListView(ListView):
    model = ReadNoteModel
    template_name = 'study_record/read_note.html'
    context_object_name = 'my_read_note'


class ReadNoteView(ListView,CreateView,UpdateView,DeleteView):
    model = ReadNoteModel
    template_name = 'study_record/read_note.html'
    context_object_name = 'my_read_note'