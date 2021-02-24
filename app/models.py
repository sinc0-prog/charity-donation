from django.db import models

class Category(models.Model):
    name = models.CharField(max_length = 64)

INSTITUTION = (
    ('fundacja', 'fundacja'),
    ('organizacja pozarządowa', 'organizacja pozarządowa'),
    ('zbiórka lokalna', 'zbiórka lokalna'),
)


class Institution(models.Model):
    name = models.CharField(max_length = 128)
    description = models.CharField(max_length = 255)
    type_of = models.CharField(max_length = 64, choices = INSTITUTION, default = 'fundacja')
    categories = models.ManyToManyField(Category)
