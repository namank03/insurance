from rest_flex_fields import FlexFieldsModelSerializer

from ..models import Customer, Policy


class CustomerSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"
        expandable_fields = {
            'policies': ('insurance.base.api.PolicySerializer', {'many': True})
        }


class PolicySerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Policy
        fields = "__all__"
        expandable_fields = {'customer': ('insurance.base.api.CustomerSerializer')}
