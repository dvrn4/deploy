from django.db import models

class Notebook(models.Model):
    model = models.CharField(max_length=120)
    color = models.CharField(max_length=80)
    photo = models.ImageField(upload_to='exam/images/')
    price = models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return f"({self.model})"


