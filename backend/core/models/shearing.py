from django.db import models

from .sheep import Sheep
from .user import User

class Shearing(models.Model):
    sheep = models.ForeignKey(Sheep, on_delete=models.PROTECT, related_name="shearing")
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name="shearing")
    date = models.DateField()
    amountOfWool =  models.FloatField()

    def __str__(self):
        return self.date
    class Meta:
        verbose_name = ("Shearing")
        verbose_name_plural = ("Shearings")
