from django.db import models
import json
# Create your models here.

from django.db import models

class pokemon(models.Model):
  poke_id = models.IntegerField(null = 'false')
  name = models.CharField(max_length=30)



  