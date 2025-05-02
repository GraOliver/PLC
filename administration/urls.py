from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as vue # importation de la bubliothèque pour la reunitialisation de
app_name="administration"

urlpatterns = [
    path("",views.Login.as_view(),name="login"),
    path('logout',views.Logout.as_view(),name="logout"),
]