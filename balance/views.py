from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Transaction
from .serializers import (
    TransactionListSerializer,
    TransactionDetailsSerializer,
    TransactionCreateSerializer,
    TransactionUpdateSerializer,
)


class TransactionListView(generics.ListAPIView):
    """
    View all transactions
    """
    queryset = Transaction.objects.all()
    serializer_class = TransactionListSerializer


class TransactionDetailsView(generics.RetrieveAPIView):
    """
    View all data by transaction
    """
    queryset = Transaction.objects.filter()
    serializer_class = TransactionDetailsSerializer


class TransactionCreateView(generics.CreateAPIView):
    """
    Create transaction
    """
    serializer_class = TransactionCreateSerializer

    # def perform_create(self, serializer):
    #     serializer.save(id=self.request.data["id"])


class TransactionUpdateView(generics.UpdateAPIView):
    queryset = Transaction.objects.filter()
    serializer_class = TransactionUpdateSerializer
