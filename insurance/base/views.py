# Create your views here.
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import redirect, render

from .forms import PolicyForm
from .models import Policy


@login_required(login_url="account_login")
def policy_view(request):
    order_by = request.GET.get("order_by", "created_at")
    q = request.GET.get("q") if request.GET.get("q") is not None else ""
    # * icontains is kind of a regex match.
    policies = Policy.objects.filter(
        Q(id__icontains=q)
        | Q(customer__id__icontains=q)
        | Q(customer__name__icontains=q)
    ).order_by(order_by)
    context = {"policies": policies}
    return render(request, "policy/policies.html", context)


@login_required(login_url="account_login")
def create_policy(request):
    form = PolicyForm()
    if request.method == "POST":
        form = PolicyForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Policy Updated successfully")
        else:
            messages.error(request, "Invalid Value for Premium")
        return redirect("base:policies")
    context = {"form": form, "form_name": "Create Policy"}
    return render(request, "policy/policy_form.html", context)


@login_required(login_url="account_login")
def update_policy(request, pk):
    policy = Policy.objects.get(id=pk)
    # Prefilling the form with the policy instance value
    form = PolicyForm(instance=policy)
    if request.method == "POST":
        form = PolicyForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Policy Updated successfully")
        else:
            messages.error(request, "Invalid Value for Premium")
        return redirect("base:policies")
    context = {"form": form, "form_name": "Updated Policy"}
    return render(request, "policy/policy_form.html", context)


@login_required(login_url="account_login")
def deletePolicy(request, pk):
    policy = Policy.objects.get(id=pk)
    if request.method == "POST":
        policy.delete()
        messages.success(request, "Policy deleted successfully")
        return redirect("base:policies")
    return render(request, "pages/delete.html", {"obj": policy})
