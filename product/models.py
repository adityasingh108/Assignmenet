from django.db import models

class product(models.Model):
    name = models.CharField(max_length=100)
    weight = models.DecimalField(max_digits = 5,decimal_places = 2)
    price = models.IntegerField(default = 0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.name
    