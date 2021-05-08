from core.api.v1.views.views_v1 import index
from django.urls import path,re_path,include
from rest_framework import permissions
from core.api.v1.views.views_v1 import index
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Task API",
      default_version='v1',
      description="Project with django and angular",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="regis@task.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)



urlpatterns = [
   path("accounts/", include("core.api.v1.urls.account_urls")),
   path("tasks/", index),
   re_path('swagger', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
   re_path('redoc/', schema_view.with_ui('redoc', cache_timeout=0),
         name='schema-redoc'),
    ]