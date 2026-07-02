"""
URL Configuration for school management system.

The `urlpatterns` list routes URLs to views.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('dj_rest_auth.urls')),
    path('api/auth/registration/', include('dj_rest_auth.registration.urls')),
    
    # App URLs
    path('api/users/', include('apps.users.urls', namespace='users')),
    path('api/students/', include('apps.students.urls', namespace='students')),
    path('api/teachers/', include('apps.teachers.urls', namespace='teachers')),
    path('api/exams/', include('apps.exams.urls', namespace='exams')),
    path('api/reports/', include('apps.reports.urls', namespace='reports')),
    path('api/fees/', include('apps.fees.urls', namespace='fees')),
    path('api/notifications/', include('apps.notifications.urls', namespace='notifications')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)