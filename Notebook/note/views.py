from django.views.generic import edit, list
from django.urls import reverse
from .models import Note
from .forms import NoteForm


class NoteListView(list.ListView):
    template_name = 'index.html'
    model = Note
    queryset = Note.objects.order_by('-updated_at')


class NoteCreateView(edit.CreateView):
    template_name = 'index.html'
    form_class = NoteForm

    def get_success_url(self):
        return reverse('note:note-list')
