from django.urls import path, include



urlpatterns = [
    path('', include('apps.index.urls')),
    path('note/', include('apps.note.urls')),
]