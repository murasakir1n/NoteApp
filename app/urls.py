from . import views
from django.urls import path


urlpatterns = [
    path('', views.note_list, name='note-list'),
    path('note_detail/<int:note_id>', views.note_detail, name = 'note-detail'),
    path('create/', views.note_create, name = 'note-create'),
    path('api/notes/', views.note_list_api, name = 'note-list-api')
]