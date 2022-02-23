from django.db import models


class Arguments(models.Model):
    arguments = models.JSONField()
