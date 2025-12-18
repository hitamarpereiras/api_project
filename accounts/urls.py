from django.urls import path
from .views import EmpresaView

urlpatterns = [
    path('usuario/', EmpresaView.as_view(), name='empresa'),
]