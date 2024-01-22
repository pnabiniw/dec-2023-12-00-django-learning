from django.shortcuts import render, redirect
from .models import ClassRoom, Student, StudentProfile


def classroom(request):
    if request.method == "POST":
        name = request.POST.get("name")
        ClassRoom.objects.create(name=name)
        return redirect('classroom')
    classrooms = ClassRoom.objects.all()
    return render(request, template_name='crud/classroom.html', context={"classrooms": classrooms,
                                                                         "classroom_active": "active"})


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
                  context={"students": students, "title": "Students", "classrooms": classrooms,
                           "student_active": "active"})


def delete_student(request, id):
    student = Student.objects.get(id=id)
    if request.method == "POST":
        student.delete()
        return redirect('crud_student')
    return render(request, template_name="crud/delete_student.html", context={"student": student})


def update_student(request, id):
    student = Student.objects.get(id=id)
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        email = request.POST.get("email")
        address = request.POST.get("address")
        classroom_id = request.POST.get("classroom")
        Student.objects.filter(id=id).update(name=name, age=age, email=email, address=address,
                                             classroom_id=classroom_id)
        return redirect("crud_student")
    classrooms = ClassRoom.objects.all()
    return render(request, template_name='crud/update_student.html',
                  context={"student": student, "classrooms": classrooms})


def student_profile(request):
    if request.method == "POST":
        student_id = request.POST.get("student")
        roll = request.POST.get("roll")
        phone = request.POST.get("phone")
        StudentProfile.objects.create(student_id=student_id, roll_no=roll, phone=phone)
        return redirect("student_profile")
    profiles = StudentProfile.objects.all()
    students = Student.objects.all()
    return render(request, template_name="crud/student_profile.html",
                  context={"profiles": profiles, "students": students, "profile_active": "active"})
