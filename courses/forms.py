from django.forms import ModelForm
from .models import Course


class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = ('title', 'content', 'date_start', 'date_end', 'amount_lecture')
