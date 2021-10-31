# Create your views here.
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import redirect, render

from .forms import CustomerForm, PolicyForm
from .models import Customer, Policy

# Policy Views


@login_required(login_url="account_login")
def policy_view(request):
    # order_by = request.GET.get("order_by", "created_at")
    # q = request.GET.get("q") if request.GET.get("q") is not None else ""
    # * icontains is kind of a regex match.
    policies = Policy.objects.all()
    # filter(
    #     Q(id__icontains=q)
    #     | Q(customer__id__icontains=q)
    #     | Q(customer__name__icontains=q)
    # ).order_by(order_by)
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
    # Making date of purchase field read-only.
    form.fields['date_of_purchase'].widget.attrs['readonly'] = True
    if request.method == "POST":
        form = PolicyForm(request.POST, instance=policy)
        if form.is_valid():
            policy = form.save(commit=False)
            policy.save()
            messages.success(request, "Policy Updated successfully")
        else:
            messages.error(request, "Invalid Value for Premium")
        return redirect("base:policies")
    context = {"form": form, "form_name": "Update Policy"}
    return render(request, "policy/policy_form.html", context)


@login_required(login_url="account_login")
def delete_policy(request, pk):
    policy = Policy.objects.get(id=pk)
    if request.method == "POST":
        policy.delete()
        messages.success(request, "Policy deleted successfully")
        return redirect("base:policies")
    return render(request, "pages/delete.html", {"obj": policy})


# Customer Views


@login_required(login_url="account_login")
def customer_view(request):
    order_by = request.GET.get("order_by", "created_at")
    q = request.GET.get("q") if request.GET.get("q") is not None else ""
    # * icontains is kind of a regex match.
    customers = Customer.objects.filter(
        Q(id__icontains=q) | Q(name__icontains=q)
    ).order_by(order_by)
    context = {"customers": customers}
    return render(request, "customer/customers.html", context)


@login_required(login_url="account_login")
def create_customer(request):
    form = CustomerForm()
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Customer Created successfully")
        else:
            messages.error(request, "Something went wrong!!")
        return redirect("base:customers")
    context = {"form": form, "form_name": "Create Customer"}
    return render(request, "customer/customer_form.html", context)


@login_required(login_url="account_login")
def update_customer(request, pk):
    customer = Customer.objects.get(id=pk)
    # Prefilling the form with the customer instance value
    form = CustomerForm(instance=customer)
    if request.method == "POST":
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            messages.success(request, "Customer Updated successfully")
        else:
            messages.error(request, "Something went wrong!!")
        return redirect("base:customers")
    context = {"form": form, "form_name": "Update Customer"}
    return render(request, "customer/customer_form.html", context)


@login_required(login_url="account_login")
def delete_customer(request, pk):
    customer = Customer.objects.get(id=pk)
    if request.method == "POST":
        customer.delete()
        messages.success(request, "Customer deleted successfully")
        return redirect("base:customers")
    return render(request, "pages/delete.html", {"obj": customer})


@login_required(login_url="account_login")
def customer_detail(request, pk):
    customer = Customer.objects.get(id=pk)
    policies = customer.policies.all()
    context = {
        "customer": customer,
        "policies": policies,
    }
    return render(request, "customer/detail.html", context)
