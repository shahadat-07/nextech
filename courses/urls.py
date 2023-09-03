from django.urls import path, include

from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='all_courses_student_panel'),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    path('all/', views.CourseListView.as_view(), name='courses'),
    path('create/', views.CourseCreateView.as_view(), name='creation'),
    path('<int:pk>/update/',
         views.CourseUpdateView.as_view(), name='course-update'),
    path('<int:pk>/delete/',
         views.CourseDeleteView.as_view(), name='course-delete'),
]
