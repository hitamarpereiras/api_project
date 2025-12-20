from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from .views import home

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('contas/', include('accounts.urls')),
    path('produtos/', include('products.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
