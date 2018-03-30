from django.shortcuts import render

from .models import Course

def courses(request):
    courses = Course.objects.all()
    
    context = {
        'courses': courses
    }

    template_name = "courses.html"
    return render(request, template_name, context)

'''def details(request, id):
    course = Course.objects.get(id=id)
    
    context = {
        'course': course
    }

    template_name = "details.html"
    return render(request, template_name, context)'''

def details(request, slug):
    course = Course.objects.get(slug=slug)
    
    context = {
        'course': course
    }

    template_name = "details.html"
    return render(request, template_name, context)