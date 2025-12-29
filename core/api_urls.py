from django.urls import path, include

urlpatterns = [    
    path('', include('auth_app.api.urls')),
    path('', include('basicdata.api.urls')),
    path('', include('checklist.api.urls')),
    path('', include('discounts.api.urls')),
]