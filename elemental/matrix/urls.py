from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addTechnique/', views.addTechnique, name='addTechnique'),
    path('addSigma/', views.addSigma, name='addSigma'),
    path('technique/<str:pk>', views.individualTechnique, name='individualTechnique'),
    #path('updateNotesPerTech/<str:pk>', views.updateNotesPerTech, name='updateNotesPerTech'),
    #path('elements/', views.index, name='index'),
    #path('sigma_rules/', views.sigma_rules.as_view(), name='sigma_rules'),
    #path('alltactics/', views.alltactics, name='alltactics'),
    #path('tactics/', views.TacticListView.as_view(), name='tactics'),
    #path('tactics/<str:pk>', views.TacticDetailView.as_view(), name='tactic-detail'),
    #path('techniques/', views.TechniqueListView.as_view(), name='techniques'),
    #path('alltechniques/', views.alltechniques, name='alltechniques'),
    #path('techniques/<str:pk>', views.TechniqueDetailView.as_view(), name='technique-detail'),
    #path('allTechPerTactic', views.allTechPerTactic, name="allTechPerTactic"),
    #path('atomics/<str:pk>', views.atomics, name='atomics'),
    #path('notesPerTech/<str:pk>', views.notesPerTech, name='notesPerTech'),

    # These are for notes functions
    path('addnote/<str:pk>', views.addnote, name='note'),
    path('note/<int:pk>', views.NoteDetailView.as_view(), name='note-detail'),
    path('addnote/<str:pk>', views.NoteCreate.as_view(), name='note_create'),
    path('note/<str:pk>/delete/', views.NoteDelete.as_view(), name='note_delete'),
    path('note/<str:pk>/update/', views.NoteUpdate.as_view(), name='note_update'),
    #path('noteCreator/<str:pk>', views.noteCreator, name='noteCreator'),
    #path('note/<str:pk>', views.notesPerTech, name='notesPerTech'),
    #path('note/create/<str:pk>', views.NoteCreate.as_view(), name='note_create'),
]
