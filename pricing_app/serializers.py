from rest_framework import serializers
from .models import PricingConfiguration

class PricingConfigurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PricingConfiguration
        fields = '__all__'
