from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as vue # importation de la bubliothèque pour la reunitialisation de
app_name="administration"

urlpatterns = [
    path("",views.Login.as_view(),name="login"),
    path('logout',views.Logout.as_view(),name="logout"),
    # path("User_change/",views.UserChangeView.as_view(),name="change_user"),
    path("password_change/",vue.PasswordChangeView.as_view(),name="password"),
    
    # nous chargeons les urls pour la reunitialisation du mot de passe
    path("reset_password", vue.PasswordResetView.as_view(),name="pass_forgeted" ),
    path("reset_password_send",vue.PasswordResetDoneView.as_view(),name="password_reset_done"),
    path("reset/<uidb64>/<token>",vue.PasswordResetConfirmView.as_view(),name="password_reset_confirm"),
    path("reset_password_complete",vue.PasswordResetCompleteView.as_view(),name="password_reset_complete"),
]