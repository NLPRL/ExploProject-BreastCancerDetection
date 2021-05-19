"""Breast_Cancer_Detection URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from os import name
from re import template
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from firstApp import views
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve
from django.contrib.auth import views as auth_views

urlpatterns = [
    #admin path
    url('base',views.base2,name = 'base'), 
    path('verification/', include('verify_email.urls')),
    path('admin/', admin.site.urls),
    path('register/', views.registerPage , name = 'register'),               #url for registration page        
    path('login/', views.loginPage , name = 'login'),                        #url for login
    path('logout/', views.logoutUser, name="logout"),                        #url for logout
    url('home',views.index,name = 'homepage'),                               #url for homepage                              #url for homepage
    url('predictImage',views.predictImage,name = 'predictImage'),            #url for predict image to run model in backend
    path('download/<int:pk>/',views.some_view,name = 'download'),     
    path('send_email',views.send_email,name='email_report'),     
    path("password-reset", auth_views.PasswordResetView.as_view( template_name='password_reset.html'), name="password_reset"),
    path("password-reset/done/", auth_views.PasswordResetDoneView.as_view( template_name='password_reset_done.html'), name="password_reset_done"),
    path("password-reset-confirm/<uidb64>/<token>", auth_views.PasswordResetConfirmView.as_view( template_name='password_reset_confirm.html'), name="password_reset_confirm"),
    path("password-reset-complete/", auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name="password_reset_complete"),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),      
    url(r'^media/(?P<path>.*)$', serve,{'document_root':settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), # images path 

    
]



urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)