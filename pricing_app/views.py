from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import PricingConfiguration
from .serializers import PricingConfigurationSerializer

class PricingConfigurationAPI(APIView):
    def get(self, request, format=None):
        configurations = PricingConfiguration.objects.all()
        serializer = PricingConfigurationSerializer(configurations, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PricingConfigurationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        configuration = PricingConfiguration.objects.get(pk=pk)
        serializer = PricingConfigurationSerializer(configuration, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        configuration = PricingConfiguration.objects.get(pk=pk)
        configuration.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CalculatePriceAPI(APIView):
    def post(self, request, format=None):
        try:
            distance = float(request.data.get('distance', 0))
            time_duration = float(request.data.get('time_duration', 0))
            waiting_time = float(request.data.get('waiting_time', 0))

            day_of_week = request.data.get('day_of_week', None)  
            pricing_config = PricingConfiguration.objects.filter(day_of_week=day_of_week, is_active=True).first()

            if pricing_config:
                distance_base_price = float(pricing_config.distance_base_price)
                distance_additional_price = float(pricing_config.distance_additional_price)
                time_multiplier_factor = float(pricing_config.time_multiplier_factor)
                waiting_charges = float(pricing_config.waiting_charges)

                price = (distance_base_price + (max(float(distance) - 3, 0) * distance_additional_price)) + (float(time_duration) * time_multiplier_factor) + (float(waiting_time) * waiting_charges)
                return Response({'price': price}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'No active pricing configuration found for the provided day.'}, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)