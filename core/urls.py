from django.urls import path,include

urlpatterns = [
    path('v1/', include('core.api.urls.urls_v1') ),
]