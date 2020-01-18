from django.urls import path
from diary import views


urlpatterns = [
    path("", views.list),
    path("<int:pk>/", views.read),
]