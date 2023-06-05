from django.urls import path

app_name = 'products'

from .views import ProductListView
from .views import ProductDetailSlugView


urlpatterns = [
        path('', ProductListView.as_view()),
        path('<slug:slug>/', ProductDetailSlugView.as_view(), name='detail')
    ]
