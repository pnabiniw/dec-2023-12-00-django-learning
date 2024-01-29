from typing import Any
from django.views.generic import TemplateView, ListView
from crud.models import ClassRoom


class HomeView(TemplateView):
    template_name = 'classbased/home.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["message"] = "I am learning classbased Django"
        return context


class ClassRoomView(ListView):
    template_name = "classbased/classroom.html"
    queryset = ClassRoom.objects.all()
    context_object_name = 'classrooms'
