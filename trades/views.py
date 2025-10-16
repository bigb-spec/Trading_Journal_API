from rest_framework import generics, permissions
from .models import Trade
from .serializers import TradeSerializer

# View to list and create trades
class TradeListCreateView(generics.ListCreateAPIView):
    queryset = Trade.objects.all()
    serializer_class = TradeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user).order_by('-date')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# View to retrieve, update, and delete a specific trade
class TradeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Trade.objects.all()
    serializer_class = TradeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
