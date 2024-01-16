from django.shortcuts import render


def students(request):
    return render(request, template_name='core/students.html')
