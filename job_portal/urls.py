from django.contrib import admin
from django.urls import path, include
from jobs.views import home, job_detail, apply_job, job_create, register
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('job/<int:job_id>/', job_detail, name='job_detail'),
    path('job/<int:job_id>/apply/', apply_job, name='apply_job'),
    path('job/create/', job_create, name='job_create'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('register/', register, name='register'),
]