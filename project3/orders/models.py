from django.db import models

# Create your models here.
#to create different pizza models
class type_of_pizza(models.model):
    name = models.CharField(max_length=64)

    def __str__ (self):
        return f"{self.name}"

#to create regular pizza model
class regular_pizza(models.model):
    name = models.ForeignKey(type_of_pizza, on_delete=CASCADE)
    small = models.DecimalField(max_digits=4,decimal_places=2)
    large = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"{self.name}-{self.small}-{self.large}"

#to create sicilian pizza
class sicilian_pizza(models.model):
    name = models.ForeignKey(type_of_pizza, on_delete=CASCADE)
    small = models.DecimalField(max_digits=4, decimal_places=2)
    large = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"{self.name}-{self.small}-{self.large}"



