from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('imovel.urls')),
    path('api/', include('imovel.urls')),
]
