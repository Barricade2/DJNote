from django.urls import path
from . import views
from .views import NoteView, NoteDetail

app_name = 'note'
urlpatterns = [
    path('', NoteView.as_view(), name='note'),
    path('<int:pk>/', NoteDetail.as_view(), name='note-detail'),
]