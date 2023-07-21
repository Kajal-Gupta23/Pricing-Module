from django.urls import path
from .views import PricingConfigurationAPI, CalculatePriceAPI

urlpatterns = [
    path('api/pricing_configurations/', PricingConfigurationAPI.as_view(), name='pricing_configurations'),
    path('api/calculate_price/', CalculatePriceAPI.as_view(), name='calculate_price'),
]
