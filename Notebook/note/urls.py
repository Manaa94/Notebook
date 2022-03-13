from django.urls import path
from .views import NoteListView

app_name = 'note'
urlpatterns = [
    path('', NoteListView.as_view(), name='note-list'),
]
