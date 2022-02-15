from django import forms
from .models import ReadNoteModel


class ReadNoteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['submit_time'].widget.attrs.update(disabled=True)
        self.fields['edit_time'].widget.attrs.update(disabled=True)

    class Meta:
        model = ReadNoteModel
        fields = ['id', 'title', 'submit_time', 'edit_time', 'link']



