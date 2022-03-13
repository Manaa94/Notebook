from django.views.generic import edit, list, UpdateView
from django.urls import reverse
from .models import Note
from .forms import NoteForm


class NoteListView(list.ListView):
    template_name = 'index.html'
    model = Note
    queryset = Note.objects.order_by('-updated_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = NoteForm()
        return context


class NoteCreateView(edit.CreateView):
    template_name = 'index.html'
    form_class = NoteForm

    def get_success_url(self):
        return reverse('note:note-list')


class NoteUpdateView(UpdateView):
    template_name = 'index.html'
    form_class = NoteForm
    queryset = Note.objects.all()


class NoteDeleteView(edit.DeleteView):
    template_name = 'index.html'
    form_class = NoteForm
    queryset = Note.objects.all()


class NoteDetailView(edit.DeleteView):
    template_name = 'index.html'
    model = Note

