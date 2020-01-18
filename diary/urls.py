from django.urls import path
from diary import views


urlpatterns = [
    path("", views.list, name="articles-list"),
    path("<int:pk>/", views.read, name="articles-read"),
    path("create/", views.create, name="articles-create"),
    path("update/<int:pk>/", views.update, name="articles-update"),
    path("delete/<int:pk>/", views.delete, name="articles-delete")
]