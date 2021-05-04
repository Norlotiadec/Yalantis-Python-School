from django.urls import path
from .views import AddCourse, DeleteCourse, UpdateCourse, api_courses, CourseView, Search, CourseDetail, \
    api_courses_detail

urlpatterns = [
    # path('', index, name='home'),
    path('', CourseView.as_view(), name='home'),
    path('search/', Search.as_view(), name='search'),
    path('<int:pk>/delete/', DeleteCourse.as_view(), name='delete_course'),
    path('<int:pk>/update/', UpdateCourse.as_view(), name='update_course'),
    path('<int:pk>', CourseDetail.as_view(), name='course_detail'),
    path('add/', AddCourse.as_view(), name='add_course'),
    path('api/courses', api_courses, name='api_courses'),
    path('api/courses/<int:pk>', api_courses_detail, name='api_detail'),
]
