from django.urls import path
from .views import ProdutoListView
from .views import ProdutoCreateView

urlpatterns = [
    path('criar/', ProdutoCreateView.as_view(), name="criar_produto"),
    path('', ProdutoListView.as_view(), name='produtos'),
]