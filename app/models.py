from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length = 64)

    def __str__(self):
        return str(self.name)

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

class Donation(models.Model):
    quantity = models.IntegerField()
    categories = models.ManyToManyField(Category) 
    institution = models.ForeignKey(Institution, on_delete=models.SET_NULL, null = True)
    address =  models.CharField(max_length = 255)
    phone_number = models.CharField(max_length = 20)
    city = models.CharField(max_length = 64)
    zip_code = models.CharField(max_length = 20)
    pick_up_date = models.DateTimeField() 
    pick_up_time = models.DateTimeField() 
    pick_up_comment = models.CharField(max_length = 255)
    user = models.ForeignKey(User, default= None, null=True, on_delete=models.SET_NULL)
