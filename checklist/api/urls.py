from django.urls import path
from .views import ChecklistItemTemplateListView

urlpatterns = [
    path('checklist-items/', ChecklistItemTemplateListView.as_view(), name='checklist-items'),
]