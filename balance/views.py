from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Transaction
from .serializers import (
    TransactionListSerializer,
    TransactionDetailsSerializer,
)


class TransactionListView(APIView):
    """
    View all transactions
    """
    def get(self, request):
        transactions = Transaction.objects.all()
        serializer = TransactionListSerializer(transactions, many=True)
        return Response(serializer.data)


class TransactionDetailsView(APIView):
    """
    View all data by transaction
    """
    def get(self, request, pk):
        transaction = Transaction.objects.get(id=pk)
        serializer = TransactionDetailsSerializer(transaction)
        return Response(serializer.data)