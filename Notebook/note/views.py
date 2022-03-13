from django.views.generic import list
from .models import Note


class NoteListView(list.ListView):
    template_name = 'index.html'
    model = Note
    queryset = Note.objects.order_by('-updated_at')
