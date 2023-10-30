from django.urls import path

from . import views

urlpatterns = [
    path("",views.pathList),
    path("newPath", views.newPath, name="index"),
    path("urls/<str:short_url>",views.redirectTo),
    path("display/<str:short_url>",view=views.display_url)
]