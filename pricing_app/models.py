from django.db import models

class PricingConfiguration(models.Model):
    distance_base_price = models.DecimalField(max_digits=8, decimal_places=2)
    distance_additional_price = models.DecimalField(max_digits=8, decimal_places=2)
    time_multiplier_factor = models.DecimalField(max_digits=8, decimal_places=2)
    waiting_charges = models.DecimalField(max_digits=8, decimal_places=2)
    day_of_week = models.CharField(max_length=3)  # Assuming 'Mon', 'Tue', etc.
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Pricing Configuration - {self.id} ({self.day_of_week})"
