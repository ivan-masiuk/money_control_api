from rest_framework import serializers

from .models import Transaction


class TransactionListSerializer(serializers.ModelSerializer):
    """
    Prepare data of transactions by fields
    """

    class Meta:
        model = Transaction
        fields = ("amount", "type", )


class TransactionDetailsSerializer(serializers.ModelSerializer):
    """
    Prepare data of transaction by all fields
    """

    # customer_fk = serializers.SlugRelatedField(
    #     slug_field="name", read_only=True,  # many=True
    # )

    class Meta:
        model = Transaction
        exclude = ("updated", "customer_fk", )


class TransactionCreateSerializer(serializers.ModelSerializer):
    """
    Creation transaction serializer
    """

    class Meta:
        model = Transaction
        fields = "__all__"

    def create(self, validated_data):
        updated_values = {
            "amount": validated_data.get("amount"),
            "type": validated_data.get("type"),
        }
        created, transaction = Transaction.objects.update_or_create(
            id=validated_data.get("id"),
            defaults=updated_values,
        )
        return transaction
