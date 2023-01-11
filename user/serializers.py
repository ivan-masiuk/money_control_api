from rest_framework import serializers

from .models import Customer

from balance.serializers import TransactionDetailsSerializer


class CustomerListSerializer(serializers.ModelSerializer):
    """
    Prepare data of customers by fields
    """

    class Meta:
        model = Customer
        fields = ("name", "age", )


class CustomerDetailsSerializer(serializers.ModelSerializer):
    """
    Prepare data of customer by all fields
    """
    transactions = TransactionDetailsSerializer(many=True)

    class Meta:
        model = Customer
        exclude = ("updated", )
