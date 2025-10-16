from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from trades.models import Trade

# Analytics Summary View 
class AnalyticsSummaryView(APIView):
    permission_classes = [permissions.IsAuthenticated]

# GET method to retrieve analytics summary data for the authenticated user 
    def get(self, request):
        user = request.user
        trades = Trade.objects.filter(user=user)

        total_trades = trades.count()
        total_profit_loss = sum([t.profit_loss or 0 for t in trades])

        win_trades = trades.filter(outcome='WIN').count()
        win_rate = (win_trades / total_trades * 100) if total_trades > 0 else 0

        rr_values = [t.rr_ratio for t in trades if t.rr_ratio is not None]
        avg_rr = sum(rr_values) / len(rr_values) if rr_values else 0
        
# Prepare the response data
        data = {
            'total_trades': total_trades,
            'win_rate': round(win_rate, 2),
            'average_rr': round(avg_rr, 2),
            'total_profit_loss': round(total_profit_loss, 2)
        }
        return Response(data)
