
from django.urls import path
from . import views

urlpatterns = [
  
    path('welcome/', views.greeting, name = 'hello'),
    path('contact-us/', views.contactus, name = 'contact123'),
    path('', views.index, name ='home'),
    path('test-run/' , views.test123, name = 'test'),
    path('index/' , views.index, name = 'index'),
    path('contact/' , views.contact, name = 'contact'),
    path('news/' , views.news, name = 'news'),
    path('about/' , views.about, name = 'about'),
    path('registration/', views.register, name= 'regurl'),
    path('DataUpload/', views.formsubmit, name= 'formsubmit')
]