from django.urls import path
from . import views
from .views import ProductListView, ProductDetaiView

urlpatterns = [
    path('', ProductListView.as_view(),name='product-home')

]