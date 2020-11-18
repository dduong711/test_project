from django.urls import path

from . import views

app_name="organization"

urlpatterns = [
    path('create/', views.OrganizationCreateView.as_view(), name="create"),
    path('detail/', views.OrganizationDetailView.as_view(), name="detail"),
]