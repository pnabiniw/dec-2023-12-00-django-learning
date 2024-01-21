from django.urls import path
from .views import classroom, delete_classroom, student, delete_student


urlpatterns = [
    path('classroom/', classroom, name='classroom'),
    path('student/', student, name='crud_student'),
    path('delete-classroom/<int:id>/', delete_classroom, name='delete_classroom'),
    path('delete-student/<int:id>/', delete_student, name='delete_student'),
]
