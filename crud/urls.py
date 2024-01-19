from django.urls import path
from .views import classroom, delete_classroom


urlpatterns = [
    path('classroom/', classroom, name='classroom'),
    path('delete-classroom/<int:id>/', delete_classroom, name='delete_classroom'),
]
