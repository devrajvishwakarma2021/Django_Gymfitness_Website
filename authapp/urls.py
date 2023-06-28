from django.urls import path
from authapp import views
urlpatterns = [
    path('', views.home, name='home'),
    path('services', views.services, name='services'),
    # path('about', views.About, name='about'),
    path('signup', views.signup, name='signup'),
    path('login', views.userlogin, name='login'),
    path('logout', views.userlogout, name='logout'),
    path('contact', views.contact, name='contact'),
    path('join', views.enroll, name="enroll"),
    path('profile', views.profile, name="profile"),
    path('gallery', views.gallery, name="gallery"),
    path('attendence', views.attendence, name="attendence"),


]