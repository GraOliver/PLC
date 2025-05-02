from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as vue # importation de la bubliothèque pour la reunitialisation de
app_name="plc_site"

urlpatterns = [
    
    path('',views.Blog.as_view(),name="index"),
    path('Activity/',views.Activity.as_view(),name="activity"),
    path('services/',views.Services.as_view(),name="services"),
    
    #PLC Carousel Admine setting
    path('carousel_aministration',views.CarouselView.as_view(),name ='carousel_view'),
    
    path('personnel_aministration',views.PersonneView.as_view(),name ='personnel_view'),
    path('produit_aministration',views.ProduitView.as_view(),name ='produit_view'),
    path('service_aministration',views.ServiceView.as_view(),name ='services_view'),
    
    path('administration',views.AdminBlog.as_view(),name="admin"),
    path('administration_supp/<int:id>/<int:id_photo>',views.SupAdminBlog.as_view(),name='sup_admin_blog'),

]
