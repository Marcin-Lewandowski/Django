"""
URL configuration for greek_apartments project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include, re_path
from django.contrib import admin
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
   openapi.Info(
      title="API Documentation",
      default_version='v1',
      description="API documentation for all available endpoints",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="example@example.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # SWAGGER
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    
    # DJANGO
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('profile/', user_profile, name='user_profile'),
    path('booking/', include('booking.urls')),
    path('clients/', include('clients.urls')),
    path('reservation_planning/', reservation_planning, name='reservation_planning'),
    path('api/reservation-planning/', ReservationPlanningAPIView.as_view(), name='reservation-planning-api'),
=======
    path('api/v1/', include([
        path('', include('hotel.urls')),
    ])),
>>>>>>> develop
]