from django.db import models

class Feed(models.Model): 
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = ("Feed")
        verbose_name_plural = ("Feeds")
