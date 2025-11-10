from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('education/', views.education, name='education'),
    path('experience/', views.experience, name='experience'),
    path('skills/', views.skills, name='skills'),
    path('projects/', views.project_list, name='project_list'),
    path('projects/<slug:slug>/', views.project_detail, name='project_detail'),
    path('contact/', views.contact, name='contact'),
]
