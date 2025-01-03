"""
URL configuration for api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'event-handler', views.EventHandlerViewSet)

'''
This shows the request paths allowed by this API:
I allow a...
- general GET request (for debugging)
- ranged GET request (based on timestamp)
- POST request
'''
urlpatterns = [
    #path('admin/', admin.site.urls), # Admin path was here in the default setup, doesn't seem like we need it
    path('security/event/', views.EventHandlerViewSet.as_view({
        'post': 'create',   # POST requests
        'get': 'list'       # For GET requests, map to a list
    })),
    path('security/event/<str:start>/<str:end>/', views.EventHandlerViewSet.as_view({
        'get': 'filter_events'  # Uses filter_events to return all JSON objects within the time range
    })),
]
