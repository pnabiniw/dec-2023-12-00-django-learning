from django.shortcuts import render, redirect
from .models import ClassRoom, Student


def classroom(request):
    if request.method == "POST":
        name = request.POST.get("name")
        ClassRoom.objects.create(name=name)
        return redirect('classroom')
    classrooms = ClassRoom.objects.all()
    return render(request, template_name='crud/classroom.html', context={"classrooms": classrooms})


def delete_classroom(request, id):
    clroom = ClassRoom.objects.get(id=id)
    if request.method == "POST":
        clroom.delete()
        return redirect('classroom')
    return render(request, template_name='crud/delete_classroom.html', context={"classroom": clroom})


def student(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        age = request.POST.get("age")
        address = request.POST.get("address")
        classroom_id = request.POST.get("classroom")
        Student.objects.create(name=name, email=email, age=age, address=address, classroom_id=classroom_id)
        return redirect('crud_student')
    students = Student.objects.all()
    classrooms = ClassRoom.objects.all()
    return render(request, template_name='crud/student.html',
                  context={"students": students, "title": "Students", "classrooms": classrooms})


def delete_student(request, id):
    student = Student.objects.get(id=id)
    if request.method == "POST":
        student.delete()
        return redirect('crud_student')
    return render(request, template_name="crud/delete_student.html", context={"student": student})
