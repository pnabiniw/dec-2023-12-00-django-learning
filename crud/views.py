from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import ClassRoom, Student, StudentProfile


@login_required
def classroom(request):
    if request.method == "POST":
        name = request.POST.get("name")
        ClassRoom.objects.create(name=name)
        return redirect('classroom')
    classrooms = ClassRoom.objects.all()
    return render(request, template_name='crud/classroom.html', context={"classrooms": classrooms,
                                                                         "classroom_active": "active"})


@login_required
def delete_classroom(request, id):
    clroom = ClassRoom.objects.get(id=id)
    if request.method == "POST":
        clroom.delete()
        return redirect('classroom')
    return render(request, template_name='crud/delete_classroom.html', context={"classroom": clroom})


@login_required
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

@login_required
def delete_student(request, id):
    student = Student.objects.get(id=id)
    if request.method == "POST":
        student.delete()
        return redirect('crud_student')
    return render(request, template_name="crud/delete_student.html", context={"student": student})

@login_required
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

@login_required
def student_profile(request):
    if request.method == "POST":
        student_id = request.POST.get("student")
        roll = request.POST.get("roll")
        phone = request.POST.get("phone")
        pp = request.FILES.get('pp')
        sp = StudentProfile.objects.create(student_id=student_id, roll_no=roll, phone=phone)
        print(pp)
        if pp:
            sp.profile_picture = pp
            sp.save()
        return redirect("student_profile")
    profiles = StudentProfile.objects.all()
    students = Student.objects.all()
    return render(request, template_name="crud/student_profile.html",
                  context={"profiles": profiles, "students": students, "profile_active": "active"})

@login_required
def update_profile(request, id):
    profile = StudentProfile.objects.get(id=id)
    if request.method == "POST":
        phone = request.POST.get("phone")
        roll = request.POST.get("roll")
        StudentProfile.objects.filter(id=id).update(phone=phone, roll_no=roll)
        return redirect('student_profile')
    return render(request, template_name="crud/update_profile.html", context={"profile": profile})

@login_required
def detail_profile(request, id):
    profile = StudentProfile.objects.get(id=id)
    return render(request, template_name='crud/detail_profile.html', context={'profile': profile})


def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        try:
            user = User.objects.get(username=username)
        except:
            return redirect("user_login")
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('root_page')
        else:
            return redirect("user_login")
    return render(request, template_name="crud/user_login.html")


@login_required
def user_logout(request):
    logout(request)
    return redirect("user_login")


def user_register(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        username = request.POST.get("username")
        password1 = request.POST.get("password")
        password2 = request.POST.get("password_confirmation")
        if password1 != password2:
            return redirect("user_register")
        user = User.objects.create(first_name=first_name, last_name=last_name,
                                   email=email, username=username, is_active=True)
        user.set_password(password1)
        user.save()
        return redirect("user_login")
    return render(request, template_name="crud/user_register.html")
