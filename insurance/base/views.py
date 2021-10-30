# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import PolicyForm
from .models import Customer, Policy


def policy_view(request):
    policies = Policy.objects.all()
    context = {'policies': policies}
    return render(request, 'policy/policies.html', context)


@login_required(login_url='login')
def create_policy(request):
    form = PolicyForm()
    if request.method == 'POST':
        Policy.objects.create(
            fuel=request.POST.get('fuel'),
            vehicle_segment=request.POST.get('vehicle_segment'),
            premium=request.POST.get('premium'),
            customer=Customer.objects.get(id=request.POST.get('customer')),
        )
        return redirect('base:policies')
    context = {'form': form}
    return render(request, 'policy/policy_form.html', context)
