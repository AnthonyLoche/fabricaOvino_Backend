from django.db import models
class Lots(models.Model):
    name = models.CharField(max_length=255, default=None)
    date = models.DateTimeField()

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = ("Lot")
        verbose_name_plural = ("Lots")
