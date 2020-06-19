from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),

    # User management
    path('accounts/', include('allauth.urls')),

    #when you go to -> 127.0.0.1:8000/accounts/ then you can see the list of urls 

    # Local apps
    path('', include('users.urls')), # new
]
