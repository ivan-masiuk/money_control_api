from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics


from .models import Customer
from .serializers import (
    CustomerListSerializer,
    CustomerDetailsSerializer,
)


class CustomerListView(generics.ListAPIView):
    """
    View all customers
    """
    queryset = Customer.objects.all()
    serializer_class = CustomerListSerializer


class CustomerDetailsView(generics.ListAPIView):
    """
    View all data by customer
    """
    queryset = Customer.objects.all()
    serializer_class = CustomerDetailsSerializer
