from django.urls import path
from .views import classroom, delete_classroom, student, delete_student, update_student, \
    student_profile, update_profile, detail_profile


urlpatterns = [
    path('classroom/', classroom, name='classroom'),
    path('student/', student, name='crud_student'),
    path('student-profile/', student_profile, name='student_profile'),
    path('delete-classroom/<int:id>/', delete_classroom, name='delete_classroom'),
    path('delete-student/<int:id>/', delete_student, name='delete_student'),
    path('update-student/<int:id>/', update_student, name='update_student'),
    path('update-profile/<int:id>/', update_profile, name='update_profile'),
    path('detail-profile/<int:id>/', detail_profile, name='detail_profile'),
]
