from rest_framework import serializers

from ..models import Customer, Policy


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class PolicySerializer(serializers.ModelSerializer):
    customers = serializers.SerializerMethodField()

    class Meta:
        model = Policy
        fields = '__all__'

    def get_customers(self, obj):
        return CustomerSerializer(obj.Customer_id).data
