from django.db import models


#title, description, start date, duration, keywords or categories, the amount of funding sought
# Create your models here.
class Project(models.Model):
    AGRO = 'AG'
    TECH = 'TH'
    FINTECH = 'FT'
    OTHER = 'OT'
    CATEGORY_CHOICES = [
        (AGRO, 'Agro'),
        (TECH, 'Tech'),
        (FINTECH, 'Fintech'),
        (OTHER, 'Other'),
    ]
    title       = models.CharField(max_length=120,blank=False)
    description = models.TextField(blank=False)
    startDate   = models.DateField(blank=False)
    duration    = models.IntegerField(blank=False)
    keywords    = models.TextField(blank=False)
    categories  = models.CharField(max_length=2,choices=CATEGORY_CHOICES,default=OTHER,blank=False)
    amount      = models.DecimalField(max_digits=1000, decimal_places=10,blank=False)
