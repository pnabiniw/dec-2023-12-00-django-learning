from django.shortcuts import render


def students(request):
    stds = [
        {"name": "Jon", "email": "j@email.com", "age": 30, "address": "KTM"},
        {"name": "Jane", "email": "jane@email.com", "age": 30, "address": "KTM"},
        {"name": "Hary", "email": "hary@email.com", "age": 30, "address": "KTM"},
        {"name": "Alex", "email": "alex@email.com", "age": 30, "address": "KTM"},
    ]
    return render(request, template_name='core/students.html',
                  context={"students": stds, "title": "Students"})
