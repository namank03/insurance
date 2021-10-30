from django import forms

from .models import Policy


class PolicyForm(forms.ModelForm):
    """Form definition for Policy."""

    class Meta:
        """Meta definition for Policyform."""

        model = Policy
        fields = '__all__'
