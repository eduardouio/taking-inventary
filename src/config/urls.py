"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf import settings
from django.contrib.staticfiles.urls import static
from django.urls import path, include
from accounts.views import HomeTV

admin.autodiscover()
admin.site.enable_nav_sidebar = False
admin.site.site_title = 'Sistema Toma de Inventario'
admin.site.site_description = 'Sistema Toma de Inventario'
admin.site.site_header = 'Admin Sistema Toma de Inventario'

urlpatterns = [
    path('', HomeTV.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('sap/', include('sap_migrations.urls')),
    path('mobile/', include('mobile.urls')),
    path('takings/', include('takings.urls')),
    path('products/', include('products.urls')),
    path('accounts/', include('accounts.urls')),
    path('recounts/', include('recounts.urls')),
    path('api/', include('api.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
