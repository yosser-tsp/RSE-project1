from django.urls import path
from . import views

app_name = 'numerique'

urlpatterns = [
    path('saisie/', views.numerique_form, name='numerique_form'),
    # On ajoute la ligne manquante pour la liste
    path('liste/', views.numerique_list, name='numerique_list'), 
]