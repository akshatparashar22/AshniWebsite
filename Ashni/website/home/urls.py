from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index , name='/index'),
    path("index", views.index , name='/index'),
    path("stats", views.stats , name='/stats'),
    path("about_us", views.about_us , name='/about_us'),
    path("contact_us", views.contact_us, name='/contact_us'),
    path("our_team", views.our_team, name='/our_team'),
    path("Awareness_session", views.Awareness_session, name='/Awareness_session'),
    path("Gender_sensitization", views.Gender_sensitization, name='/Gender_sensitization'),
    path("PoSH_awareness", views.PoSH_awareness, name='/PoSH_awareness'),
]