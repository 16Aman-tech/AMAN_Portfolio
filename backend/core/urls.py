from django.urls import path

from .views import home

from analytics.views import download_resume


urlpatterns = [

    path("", home, name="home"),

    path(
        "download-resume/",
        download_resume,
        name="download_resume",
    ),

]