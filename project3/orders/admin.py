from django.contrib import admin
from .models import Regular_pizza, Sicilian_pizza, Topping, Sub, Pasta, Dinner_platter, Salad, Category
# Register your models here.
admin.site.register(Category)
admin.site.register(Regular_pizza)
admin.site.register(Sicilian_pizza)
admin.site.register(Topping)
admin.site.register(Sub)
admin.site.register(Pasta)
admin.site.register(Dinner_platter)
admin.site.register(Salad)