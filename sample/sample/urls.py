"""
URL configuration for sample project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from sample import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage,name='home'),
    path('aboutus/', views.aboutus,name='about'),
    path('menu/', views.menu,name='menu'),
    path('reservation/', views.reservation,name='reservation'),
    path('eventbooking/', views.eventbooking,name='eventbooking'),
    path('location/', views.location,name='location'),
    path('reservationoutput/', views.resop,name='rop'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)