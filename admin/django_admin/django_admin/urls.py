from django.contrib import admin
from django.urls import path,include
from django.views.generic.base import TemplateView

urlpatterns = [
    
    path('admin/', admin.site.urls),

    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    
    # User management
    path('accounts/', include('django.contrib.auth.urls')), # new

    path('users/', include('users.urls')),
]
