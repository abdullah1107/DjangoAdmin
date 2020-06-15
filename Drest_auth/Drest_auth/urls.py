
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import include, url
from django.views.generic import TemplateView, RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    

    # User management
    path('accounts/', include('django.contrib.auth.urls')),

    # Local apps
    path('', include('users.urls')), # new
    path('accounts/', include('users.urls')), # new


]


