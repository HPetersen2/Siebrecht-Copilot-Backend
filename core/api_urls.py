from django.urls import path, include

urlpatterns = [
    path('', include('basicdata.api.urls')),
    path('', include('checklist.api.urls')),
]