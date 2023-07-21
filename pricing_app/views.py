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
