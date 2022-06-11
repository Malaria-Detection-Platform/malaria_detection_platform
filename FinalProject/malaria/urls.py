from django.urls import path
from django.views.generic import TemplateView


app_name = 'malaria'

urlpatterns = [
    path('', TemplateView.as_view(template_name='malaria/index.html'))
]
