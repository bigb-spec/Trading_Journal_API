from django.urls import path, include
from .views import TradeListCreateView, TradeDetailView

# URL patterns for trade-related endpoints
urlpatterns = [
    path('trades/', TradeListCreateView.as_view(), name='trade-list-create'),
    path('trades/<int:pk>/', TradeDetailView.as_view(), name='trade-detail'),
]