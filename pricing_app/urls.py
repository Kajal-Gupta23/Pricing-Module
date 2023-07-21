from django.urls import path
from .views import PricingConfigurationAPI

urlpatterns = [
    path('api/pricing_configurations/', PricingConfigurationAPI.as_view(), name='pricing_configurations'),

]
