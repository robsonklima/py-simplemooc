from django.shortcuts import render

from .models import Course

def courses(request):
    courses = Course.objects.all()
    
    context = {
        'courses': courses
    }

    template_name = "courses.html"
    return render(request, template_name, context)