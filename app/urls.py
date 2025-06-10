from tkinter.font import names

from . import views
from django.urls import path


urlpatterns = [
    path('', views.note_list, name='note-list'),
    path('note_detail/<int:note_id>', views.note_detail, name = 'note-detail'),
    path('create/', views.note_create, name = 'note-create'),
    path('api/notes/', views.note_list_api, name = 'note-list-api'),
    path('register/', views.register_view, name = 'register'),
    path('login/', views.login_view, name = 'login'),
    path('logout/', views.logout_view, name = 'logout'),
    path('login/', views.login_view, name='login'),
    path('profile/', views.profile_view, name = 'profile'),
    path('note/edit/<int:note_id>/', views.edit_note, name = 'note-edit'),
    path('note/delete/<int:note_id>/', views.delete_note, name = 'note-delete')
]