from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as vue # importation de la bubliothèque pour la reunitialisation de
app_name="plc_site"

urlpatterns = [
    path('',views.Blog.as_view(),name="index"),
    path('Activity/<int:id>',views.Activity.as_view(),name="activity")
]
