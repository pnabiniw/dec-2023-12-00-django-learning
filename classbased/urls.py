from django.urls import path
from .views import HomeView, ClassRoomView


urlpatterns = [
    path('classroom/', ClassRoomView.as_view(), name="classbased_classroom"),
    path('', HomeView.as_view(), name='classbased_home')
]


# DjangoIsAnAwesomeFramework  => Camel Case
# django_is_an_awesome_language => Snake Case