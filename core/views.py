from django.shortcuts import render
from .models import Student


def students(request):
    stds = Student.objects.all()
    return render(request, template_name='core/students.html',
                  context={"students": stds, "title": "Students"})
