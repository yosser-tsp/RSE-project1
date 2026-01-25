from django.db import models

class EquipementNumerique(models.Model):
    TYPE_CHOICES = [
        ('1. Hardware (Terminaux)', (
            ('LAPTOP', 'Ordinateur Portable (250kg CO2e)'),
            ('DESKTOP_SCREEN', 'Ordinateur Fixe + Écran (350kg CO2e)'),
            ('SMARTPHONE', 'Smartphone / Tablette (50kg CO2e)'),
        )),
        ('2. Réseau', (
            ('BORNE_WIFI', 'Borne Wi-Fi (20kg CO2e)'),
            ('SWITCH', 'Switch réseau (80kg CO2e)'),
        )),
        ('3. Cloud & Services', (
            ('CLOUD_INSTANCE', 'Instance Cloud / Serveur virtuel (500kg CO2e)'),
            ('CLOUD_STORAGE', 'Stockage Cloud 1 To (150kg CO2e)'),
        )),
        ('4. Périphériques', (
            ('PRINTER', 'Imprimante Laser (500kg CO2e)'),
            ('SCREEN_EXTRA', 'Écran supplémentaire (200kg CO2e)'),
        )),
    ]
    
    # Données ADEME (Fabrication en kg CO2e)
    FAB_CO2 = {
        'LAPTOP': 250, 
        'DESKTOP_SCREEN': 350, 
        'SMARTPHONE': 50,
        'BORNE_WIFI': 20, 
        'SWITCH': 80,
        'CLOUD_INSTANCE': 500, 
        'CLOUD_STORAGE': 150,
        'PRINTER': 500, 
        'SCREEN_EXTRA': 200,
    }
    # Consommation moyenne (kWh/an)
    CONSO_MOYENNE = {
        'LAPTOP': 30, 
        'DESKTOP_SCREEN': 170, 
        'SMARTPHONE': 5,
        'BORNE_WIFI': 50, 
        'SWITCH': 100,
        'CLOUD_INSTANCE': 0,  # Consommation cloud non comptée localement
        'CLOUD_STORAGE': 0,   # Consommation cloud non comptée localement
        'PRINTER': 200, 
        'SCREEN_EXTRA': 50,
    }

    nom = models.CharField(max_length=100)
    type_equipement = models.CharField(max_length=30, choices=TYPE_CHOICES)
    quantite = models.PositiveIntegerField(default=1)
    duree_vie = models.PositiveIntegerField(default=5)
    
    # Champs calculés automatiquement
    empreinte_fabrication = models.FloatField(default=0, editable=False)
    consommation_annuelle = models.FloatField(default=0, editable=False)

    def save(self, *args, **kwargs):
        # Calcul Fabrication
        facteur_fab = self.FAB_CO2.get(self.type_equipement, 0)
        self.empreinte_fabrication = facteur_fab * self.quantite
        
        # Calcul Consommation (Usage)
        facteur_conso = self.CONSO_MOYENNE.get(self.type_equipement, 0)
        self.consommation_annuelle = facteur_conso * self.quantite
        
        super().save(*args, **kwargs)