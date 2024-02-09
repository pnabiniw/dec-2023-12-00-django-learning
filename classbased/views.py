from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView, DetailView
from crud.models import ClassRoom
from .forms import ClassRoomModelForm


class HomeView(TemplateView):
    template_name = 'classbased/home.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["message"] = "I am learning classbased Django"
        return context


class ClassRoomView(CreateView):
    template_name = "classbased/classroom.html"
    queryset = ClassRoom.objects.all()
    context_object_name = 'classrooms'
    form_class = ClassRoomModelForm
    success_url = reverse_lazy("classbased_classroom")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["classrooms"] = ClassRoom.objects.all()
        return context


class ClassRoomUpdateView(UpdateView):
    template_name = "classbased/classroom_update.html"
    form_class = ClassRoomModelForm
    success_url = reverse_lazy("classbased_classroom")
    queryset = ClassRoom.objects.all()


class ClassRoomDeleteView(DeleteView):
    template_name = "classbased/classroom_delete.html"
    queryset = ClassRoom.objects.all()
    success_url = reverse_lazy('classbased_classroom')


class ClassRoomDetailView(DetailView):
    template_name = "classbased/classroom_detail.html"
    queryset = ClassRoom.objects.all()
    context_object_name = "classroom"
