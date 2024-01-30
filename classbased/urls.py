from django.urls import path
from .views import HomeView, ClassRoomView, ClassRoomUpdateView, ClassRoomDeleteView


urlpatterns = [
    path('classroom/', ClassRoomView.as_view(), name="classbased_classroom"),
    path('classroom-update/<int:pk>/', ClassRoomUpdateView.as_view(), name="classbased_classroom_update"),
    path('classroom-delete/<int:pk>/', ClassRoomDeleteView.as_view(), name="classbased_classroom_delete"),
    path('', HomeView.as_view(), name='classbased_home')
]


# DjangoIsAnAwesomeFramework  => Camel Case
# django_is_an_awesome_language => Snake Case
