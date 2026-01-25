from django.shortcuts import render, redirect
from django.db.models import Sum
from .models import EquipementNumerique
from .forms import NumeriqueForm
import json

def numerique_form(request):
    if request.method == 'POST':
        form = NumeriqueForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('numerique:numerique_form')
    else:
        form = NumeriqueForm()

    equipements = EquipementNumerique.objects.all()
    
    # Totaux pour dashboard en bas de page
    total_carbone = equipements.aggregate(Sum('empreinte_fabrication'))['empreinte_fabrication__sum'] or 0
    total_conso = equipements.aggregate(Sum('consommation_annuelle'))['consommation_annuelle__sum'] or 0
    
    # Répartition par type d'équipement pour les graphiques
    repartition = equipements.values('type_equipement').annotate(
        total_fab=Sum('empreinte_fabrication'),
        total_conso=Sum('consommation_annuelle')
    ).order_by('-total_fab')
    
    # Construire les données pour les graphiques
    chart_labels = []
    chart_fab_data = []
    chart_conso_data = []
    
    # Mapper les codes vers les noms lisibles
    type_display = dict(EquipementNumerique.TYPE_CHOICES[0][1])
    type_display.update(dict(EquipementNumerique.TYPE_CHOICES[1][1]))
    type_display.update(dict(EquipementNumerique.TYPE_CHOICES[2][1]))
    type_display.update(dict(EquipementNumerique.TYPE_CHOICES[3][1]))
    
    for item in repartition:
        label = type_display.get(item['type_equipement'], item['type_equipement'])
        # Raccourcir le label pour l'affichage
        label = label.split('(')[0].strip()
        chart_labels.append(label)
        chart_fab_data.append(item['total_fab'] or 0)
        chart_conso_data.append(item['total_conso'] or 0)

    return render(request, 'numerique/numerique_form.html', {
        'form': form,
        'equipements': equipements,
        'total_carbone': total_carbone,
        'total_conso': total_conso,
        'chart_labels': json.dumps(chart_labels),
        'chart_fab_data': json.dumps(chart_fab_data),
        'chart_conso_data': json.dumps(chart_conso_data),
    })
from django.shortcuts import render, redirect
from .models import EquipementNumerique

# Garde ta fonction numerique_form...

def numerique_list(request):
    equipements = EquipementNumerique.objects.all()
    return render(request, 'numerique/numerique_list.html', {
        'equipements': equipements
    })