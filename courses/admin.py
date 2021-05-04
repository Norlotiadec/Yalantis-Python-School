from django.contrib import admin
from .models import Course


class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_start', 'date_end', 'amount_lecture')
    list_display_links = ('title', 'amount_lecture')
    search_fields = ('title', 'date_start')


admin.site.register(Course, CourseAdmin)
