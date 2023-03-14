from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('service', views.service, name='service'),
    path('contact', views.contact, name='contact'),
    path('feature', views.feature, name='feature'),
    path('project', views.project, name='project'),
    path('quote', views.quote, name='quote'),
    path('team', views.team, name='team'),
    path('testimonial', views.testimonial, name='testimonial'),
    path('404', views.testimonial, name='404'),
]
