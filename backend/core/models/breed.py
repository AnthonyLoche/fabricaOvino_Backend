from django.db import models
class Breed(models.Model):
    name = models.CharField(max_length=255)
    nickname = models.CharField(max_length=100, blank=True, null=True, default=None)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = ("Breed")
        verbose_name_plural = ("Breeds")