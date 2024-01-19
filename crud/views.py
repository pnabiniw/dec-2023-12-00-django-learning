from django.shortcuts import render, redirect
from .models import ClassRoom


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
