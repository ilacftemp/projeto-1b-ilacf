from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('notes/tags.html', views.tags, name='tags'),
    path('tag/<str:title>', views.tag, name='tag'),
    path('tag/delete/<int:id>', views.delete_pag_tag, name='delete'),
    path('tag/edit/<int:id>', views.edit_pag_tag, name='edit'),
    path('notes/tag/<str:title>', views.tag, name='tag'),
    path('notes/tag/delete/<int:id>', views.delete_pag_tag, name='delete'),
    path('notes/tag/edit/<int:id>', views.edit_pag_tag, name='edit'),
    path('notes/delete/<str:title>', views.delete_tag, name='delete'),
    path('api/notes/<int:note_id>/', views.api_update_note),
    path('api/notes/', views.api_create_note)
]