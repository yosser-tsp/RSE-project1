from django import forms
from .models import EquipementNumerique

class NumeriqueForm(forms.ModelForm):
    class Meta:
        model = EquipementNumerique
        # On ne garde que les champs que l'utilisateur doit remplir
        fields = ['nom', 'type_equipement', 'quantite', 'duree_vie']
        widgets = {
            'type_equipement': forms.Select(attrs={'class': 'form-control'}),
            'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ex: PC Portable Dell'}),
            'quantite': forms.NumberInput(attrs={'class': 'form-control', 'min': '1'}),
            'duree_vie': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'en années'}),
        }