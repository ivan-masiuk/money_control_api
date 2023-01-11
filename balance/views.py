from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Transaction
from .serializers import (
    TransactionListSerializer,
    TransactionDetailsSerializer,
    TransactionCreateSerializer,
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


class TransactionCreateView(APIView):
    """
    Create transaction
    """

    def post(self, request):
        transaction = TransactionCreateSerializer(data=request.data)
        if transaction.is_valid():
            transaction.save(id=request.data["id"])
            return Response(status=201)
        else:
            return Response(status=400)
