from rest_framework import viewsets, permissions
from .models import Trade
from .serializers import TradeSerializer

class TradeViewSet(viewsets.ModelViewSet):
    serializer_class = TradeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Each user sees only their trades
        return Trade.objects.filter(user=self.request.user).order_by('-date')

    def perform_create(self, serializer):
        # Set the user as the logged-in user
        serializer.save(user=self.request.user)
