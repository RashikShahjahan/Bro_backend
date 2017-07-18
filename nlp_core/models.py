# -*- coding: utf-8 -*-
from __future__ import unicode_literals 
from django.db import models


# Create your models here.

class Data(models.Model):
    input = models.CharField(max_length=500)

    def __str__(self):
        return self.input

    
