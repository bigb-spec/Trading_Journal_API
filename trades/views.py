from rest_framework import viewsets, permissions
from .models import Trade
from .serializers import TradeSerializer

class TradeViewSet(viewsets.ModelViewSet):
    queryset = Trade.objects.all()
    serializer_class = TradeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # only return trades for the authenticated user 
        return Trade.objects.filter(user=self.request.user)
