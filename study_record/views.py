from django.shortcuts import render
from django.views.generic import ListView, DeleteView, DetailView
from django.views.generic.edit import UpdateView, CreateView
from .models import ReadNoteModel
from django.urls import reverse_lazy


def index(request):
    return render(request, template_name="study_record/read.html")


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
    context_object_name = "read_note_edit"
    template_name = "study_record/read_note.html"
    fields = ['title', 'content', 'link']
    pk_url_kwarg = "id"

    def get_context_data(self, **kwargs):
        context = super(ReadNoteEditView, self).get_context_data(**kwargs)
        context['read_note_edit_form'] = context.get('form')
        return context


class ReadNoteDeleteView(DeleteView):
    model = ReadNoteModel
    success_url = reverse_lazy('read_list')
    pk_url_kwarg = 'id'
    context_object_name = "read_note_delete"
    template_name = "study_record/read_note.html"

    def get_context_data(self, **kwargs):
        context = super(ReadNoteDeleteView, self).get_context_data(**kwargs)
        context['read_note_delete_form'] = context.get('form')
        return context


class ReadNoteCreateView(CreateView):
    model = ReadNoteModel
    template_name = "study_record/read_note.html"
    fields = ['title', 'content', 'link']
    success_url = reverse_lazy('read_list')

    def get_context_data(self, **kwargs):
        context = super(ReadNoteCreateView, self).get_context_data(**kwargs)
        context['read_note_create_form'] = context.get('form')
        context['read_note_create'] = True
        return context

