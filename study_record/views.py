from django.shortcuts import render
from django.views.generic import ListView, DeleteView, DetailView
from django.views.generic.edit import UpdateView
from .models import ReadNoteModel
from .forms import ReadNoteForm


class ReadNoteListView(ListView):
    model = ReadNoteModel
    template_name = "study_record/read_note.html"
    context_object_name = "read_note_list"


class ReadNoteDetailView(DetailView):
    # queryset = ReadNoteModel.objects.all()
    model = ReadNoteModel
    template_name = "study_record/read_note.html"
    context_object_name = "read_note_detail"
    pk_url_kwarg = "id"


class ReadNoteEditView(UpdateView):
    model = ReadNoteModel
    template_name = "study_record/read_note.html"
    context_object_name = "read_note_edit_form"
    fields = ['title', 'content', 'link']
    pk_url_kwarg = "id"

