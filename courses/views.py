from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Course
from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import CourseForm  # Import the CourseForm
from django.views.generic import ListView
from .forms import CourseForm
from django.views import View


@method_decorator(login_required, name='dispatch')
class CourseCreateView(CreateView):
    model = Course
    form_class = CourseForm  # Use the CourseForm
    template_name = 'course_creation.html'  # Replace with your template name
    success_url = reverse_lazy('courses')  # Define your success URL name

    def form_valid(self, form):
        # Check if the user is a teacher (user_type is 'Teacher')
        if self.request.user.account.user_type == 'Teacher':
            # Set the teacher (user) for the course and save it
            form.instance.teacher = self.request.user
            return super().form_valid(form)
        else:
            # Redirect or display an error message for students
            # For example, you can redirect them to a permission denied page
            # or show an error message
            return HttpResponse("You don't have permission to create a course")


class CourseListView(ListView):
    model = Course
    template_name = 'all_courses.html'
    context_object_name = 'courses'

    def get_queryset(self):
        # Filter courses based on the currently logged-in teacher
        return Course.objects.filter(teacher=self.request.user)

    # Optionally, you can add a login URL and a redirect URL
    # Replace 'login' with your actual login URL
    login_url = reverse_lazy('login')
    # redirect_field_name = 'next'  # If needed, specify the redirect field name


class CourseDeleteView(DeleteView):
    model = Course
    template_name = 'confirm_delete.html'  # Create this template
    # Redirect to the courses list page after deletion
    success_url = reverse_lazy('courses')
    context_object_name = 'course'  # Context variable name for the course object


class CourseUpdateView(UpdateView):
    model = Course
    form_class = CourseForm  # Replace with your actual form class
    template_name = 'course_update_form.html'  # Create this template
    # Redirect to courses list page after update
    success_url = reverse_lazy('courses')
    context_object_name = 'course'  # Context variable name for the course object


class HomePageView(View):
    template_name = 'homepage.html'

    def get(self, request):
        courses = Course.objects.all()

        # Handle search by title
        query = request.GET.get('q')
        if query:
            courses = courses.filter(title__icontains=query)

        # Get distinct departments from the Course model
        departments = Course.objects.values_list(
            'department', flat=True).distinct()

        # Handle filtering by department
        department_filter = request.GET.get('department')
        if department_filter:
            courses = courses.filter(department=department_filter)

        context = {
            'courses': courses,
            'departments': departments,
        }
        return render(request, self.template_name, context)


class DashboardView(View):
    template_name = 'dashboard.html'

    def get(self, request):
        return render(request, self.template_name)
