from django.contrib import admin
from django.db.models import Model
from Final_Project import models

for model in dir(models):
    model_instance = getattr(models, model)
    if isinstance(model_instance, Model):
        admin.site.register(model_instance)
