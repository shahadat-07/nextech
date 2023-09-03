from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.views.generic import FormView
from .forms import RegistrationForm
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.views import View
from django.shortcuts import redirect
from .models import UserDetails


class UserRegistrationView(FormView):
    template_name = 'accounts/register.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        user_details = UserDetails.objects.create(
            user=user,
            user_type=form.cleaned_data['user_type']
        )
        login(self.request, user)
        return super().form_valid(form)

    def get_success_url(self):
        user_type = self.request.user.account.user_type
        if user_type == 'Teacher':
            return reverse_lazy('courses')
        elif user_type == 'Student':
            return reverse_lazy('all_courses_student_panel')
        else:
            return reverse_lazy('home')


class UserLoginView(LoginView):
    template_name = 'accounts/signin.html'

    def get_success_url(self):
        user_type = self.request.user.account.user_type
        if user_type == 'Teacher':
            return reverse_lazy('courses')
        elif user_type == 'Student':
            return reverse_lazy('all_courses_student_panel')
        else:
            return reverse_lazy('home')


class UserLogoutView(LogoutView):
    def get_success_url(self):
        if self.request.user.is_authenticated:
            logout(self.request)
        return reverse_lazy('home')
