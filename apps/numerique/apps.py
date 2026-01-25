from django.apps import AppConfig

class NumeriqueConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.numerique'  # <--- TRÈS IMPORTANT : il faut le nom complet
    verbose_name = 'Numérique'