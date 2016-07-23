from django.db import models
from . import help_texts

class BootstrapCalendarModel(models.Model):

    title = models.CharField(max_length=255)
    url = models.CharField(max_length=255, null=True, blank=True)
    event_class = models.CharField(max_length=255, choices=help_texts.EVENT_CLASS, help_text=help_texts.CLASS_HELP)
    start = models.DateTimeField()
    end = models.DateTimeField()
    desc = models.TextField(null=True, blank=True)

    class Meta:
        abstract = True
