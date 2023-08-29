"""
URL configuration for ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from userside import views as us_views
from spadmin import views as ad_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',us_views.homepage,name = 'home'),
    path('admin/',ad_views.adminhome,name = 'spadmin'),
    path('admin/dataadd/',ad_views.dataAdd,name = 'dataadd'),
    path('product/<int:mobile_id>/', us_views.product_detail, name='product'),
    path('edit/<int:mobile_id>/', ad_views.edit_data, name='edit_data'),
    path('allproducts/', ad_views.allproducts, name='allproducts'),
    path('delete_product/<int:mobile_id>/', ad_views.delete_product, name='delete_product'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

