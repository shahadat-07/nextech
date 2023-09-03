from django.shortcuts import render


def home(request):
    return render(request, 'index.html')


def teacher(request):
    return render(request, 'teacher.html')


def courses(request):
    return render(request, 'courses.html')


def about(request):
    return render(request, 'about.html')


def pricing(request):
    return render(request, 'pricing.html')


def blog(request):
    return render(request, 'blog.html')


def contact(request):
    return render(request, 'contact.html')
