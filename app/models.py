from django.utils import timezone
from django.db import models

class Note(models.Model):
    title = models.CharField(max_length=100)
    text = models.CharField()
    create_date = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.title
