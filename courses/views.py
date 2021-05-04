from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.views.generic import ListView, DetailView
from .models import Course
from .forms import CourseForm
from .serializers import CourseSerializer
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from rest_framework.response import Response
from rest_framework.decorators import api_view


class CourseView(ListView):
    model = Course
    queryset = Course.objects.all()
    context_object_name = 'courses'


class Search(ListView):
    model = Course
    context_object_name = 'courses'
    template_name = 'courses/search_list.html'

    def get_queryset(self):
        if self.request.GET.get('q'):
            return Course.objects.filter(title__icontains=self.request.GET.get('q'))
        elif self.request.GET.get('date'):
            return Course.objects.filter(date_start__in=self.request.GET.getlist('date'))


# def course_detail(request, course_id):
#     course = Course.objects.get(pk=course_id)
#     return render(request, 'courses/detail_course.html', {'course': course})


class CourseDetail(DetailView):
    model = Course
    template_name = 'courses/detail_course.html'


class AddCourse(CreateView):
    template_name = 'courses/create_course.html'
    form_class = CourseForm
    success_url = reverse_lazy('home')


class DeleteCourse(DeleteView):
    model = Course
    template_name = 'courses/delete_course.html'
    success_url = reverse_lazy('home')


class UpdateCourse(UpdateView):
    template_name = 'courses/update_course.html'
    model = Course
    form_class = CourseForm
    success_url = reverse_lazy('home')


def api_courses(request):
    if request.method == 'GET':
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return JsonResponse(serializer.data, safe=False)


def api_courses_detail(request, pk):
    if request.method == 'GET':
        courses = Course.objects.get(pk=pk)
        serializer = CourseSerializer(courses)
        return JsonResponse(serializer.data)
