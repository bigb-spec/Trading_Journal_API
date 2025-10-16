from django.db import models
from django.contrib.auth.models import User

class Trade(models.Model):

    # Choices for direction and session
    DIRECTION_CHOICES = [
        ('BUY', 'Buy'),
        ('SELL', 'Sell'),
    ]

    # New session choices
    SESSION_CHOICES = [
        ('ASIAN', 'Asian'),
        ('LONDON', 'London'),
        ('NEW YORK', 'New York'),
    ]

    # Outcome choices
    OUTCOME_CHOICES = [
        ('WIN', 'Win'),
        ('LOSS', 'Loss'),
        ('BREAKEVEN', 'Breakeven'),
    ]
    
    Session = models.CharField(max_length=10, choices=SESSION_CHOICES, null=True, blank=True) # e.g., 'ASIAN', 'LONDON', 'NEW YORK' 
    user = models.ForeignKey(User, on_delete=models.CASCADE) # Link to User model
    date = models.DateTimeField()  # Date and time of the trade 
    symbol = models.CharField(max_length=10) # e.g., 'EURUSD' 
    direction = models.CharField(max_length=4, choices=DIRECTION_CHOICES) # 'BUY' or 'SELL'
    entry_price = models.DecimalField(max_digits=10, decimal_places=2) 
    exit_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    stop_loss = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    take_profit = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    lot_size = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True)
    outcome = models.CharField(max_length=10, choices=OUTCOME_CHOICES, null=True, blank=True) # 'WIN', 'LOSS', or 'BREAKEVEN'
    profit_loss = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    rr_ratio = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    notes = models.TextField(null=True, blank=True) # Additional notes about the trade 
    screenshot = models.ImageField(upload_to='trade_screenshots/', null=True, blank=True) # Optional screenshot of the trade 
    day_of_week = models.CharField(max_length=10, null=True, blank=True) # e.g., 'Monday', 'Tuesday', etc. 

    def save(self, *args, **kwargs):
        # Calculate profit/loss and risk/reward ratio if exit_price is provided

        if self.exit_price and self.entry_price:
            if self.direction == 'BUY':
                self.profit_loss = (self.exit_price - self.entry_price) * (self.lot_size if self.lot_size else 1)
            elif self.direction == 'SELL':
                self.profit_loss = (self.entry_price - self.exit_price) * (self.lot_size if self.lot_size else 1)
            
            # Calculate risk/reward ratio only if stop_loss and take_profit are provided 
            if self.stop_loss and self.take_profit:
                risk = abs(self.entry_price - self.stop_loss)
                reward = abs(self.take_profit - self.entry_price)
                if risk > 0:
                    self.rr_ratio = reward / risk
            
            # Determine day of the week from date
        if self.date:
            self.day_of_week = self.date.strftime('%A')

        super().save(*args, **kwargs) 


    def __str__(self):
        return f"{self.user.username} - {self.symbol} - {self.direction} - {self.date.strftime('%Y-%m-%d')}" 
