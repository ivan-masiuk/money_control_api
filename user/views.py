from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Customer
from .serializers import (
    CustomerListSerializer,
    CustomerDetailsSerializer,
)


class CustomerListView(APIView):
    """
    View all customers
    """
    def get(self, request):
        user = Customer.objects.all()
        serializer = CustomerListSerializer(user, many=True)
        return Response(serializer.data)


class CustomerDetailsView(APIView):
    """
    View all data by customer
    """
    def get(self, request, pk):
        user = Customer.objects.get(id=pk)
        serializer = CustomerDetailsSerializer(user)
        return Response(serializer.data)
