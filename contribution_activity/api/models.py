from django.db import models

# Create your models here.
class Action(models.Model):
    date = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=10, null=False)

    class Meta:
        unique_together = ('date', 'name')

