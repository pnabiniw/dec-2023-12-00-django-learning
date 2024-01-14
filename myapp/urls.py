from django.urls import path
from .views import home, template_home


urlpatterns = [
    path("home1/", template_home),
    path('', home),
]
