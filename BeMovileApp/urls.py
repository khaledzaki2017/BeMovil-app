"""BeMovileApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework_swagger.views import get_swagger_view
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static


schema_view = get_swagger_view(title='App APIs')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('multi_step_form.urls')),
    path('adminpanel/', include('adminpanel.urls')),
    # path('pdf/', include('pdf_results.urls')),
    path('auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(),
         name='token_obtain_pair'),  # new
    path('api/refresh/', TokenRefreshView.as_view(),
         name='token_refresh'),      # new
    path('', schema_view)
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
