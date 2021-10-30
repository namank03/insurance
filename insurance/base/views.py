# Create your views here.
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect, render


def ViewName(request):
    return HttpResponse("Enter response")


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


@login_required(login_url='login')
def deletePolicy(request, pk):
    policy = Policy.objects.get(id=pk)
    if request.method == 'POST':
        policy.delete()
        return redirect('base:policies')
    return render(request, 'pages/delete.html', {'obj': policy})


@login_required(login_url='login')
def update_policy(request, pk):
    policy = Policy.objects.get(id=pk)
    # Prefilling the form with the policy instance value
    form = PolicyForm(instance=policy)
    if request.method == 'POST':
        policy.fuel = request.POST.get('fuel')
        policy.vehicle_segment = request.POST.get('vehicle_segment')
        policy.premium = request.POST.get('premium')
        policy.customer = Customer.objects.get(id=request.POST.get('customer'))
        policy.save()
        return redirect('base:policies')
    context = {'form': form, 'policy': policy}
    return render(request, 'policy/policy_form.html', context)
