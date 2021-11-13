from bootstrap_datepicker_plus import DatePickerInput
from django import forms

from .models import Customer, Policy


class PolicyForm(forms.ModelForm):
    """Form definition for Policy."""

    class Meta:
        """Meta definition for Policyform."""

        model = Policy
        fields = "__all__"
        widgets = {'date_of_purchase': DatePickerInput()}


class CustomerForm(forms.ModelForm):
    """Form definition for Customer."""

    class Meta:
        """Meta definition for Customerform."""

        model = Customer
        fields = "__all__"
