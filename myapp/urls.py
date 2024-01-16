from django.urls import path
from .views import template_home, root_page, portfolio


urlpatterns = [
    path("home1/", template_home),
    path("portfolio/", portfolio, name='portfolio'),
    path('', root_page, name='root_page'),
]
