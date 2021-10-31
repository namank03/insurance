from django.urls import path

from insurance.base.views import (
    create_customer,
    create_policy,
    customer_detail,
    customer_view,
    delete_customer,
    delete_policy,
    policy_view,
    update_customer,
    update_policy,
)

app_name = "base"

urlpatterns = [
    path("policies/", view=policy_view, name="policies"),
    path("create-policy/", create_policy, name="createPolicy"),
    path("create-policy/<str:pk>", update_policy, name="updatePolicy"),
    path("delete-policy/<str:pk>", delete_policy, name="deletePolicy"),
    path("customers/", view=customer_view, name="customers"),
    path("customers/<str:pk>", view=customer_detail, name="customerDetail"),
    path("create-customers/", create_customer, name="createCustomer"),
    path("update-customers/<str:pk>", update_customer, name="updateCustomer"),
    path("delete-customers/<str:pk>", delete_customer, name="deleteCustomer"),
]
