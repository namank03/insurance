from django.urls import path

from insurance.base import views

app_name = "base"

urlpatterns = [
    path("policies/", view=views.policy_view, name="policies"),
    path("create-policy/", view=views.create_policy, name="create-policy"),
    path("create-policy/<str:pk>", view=views.update_policy, name="update-policy"),
    path("delete-policy/<str:pk>", view=views.delete_policy, name="delete-policy"),
    path("customers/", view=views.customer_view, name="customers"),
    path("customers/<str:pk>", view=views.customer_detail, name="customer-detail"),
    path("create-customers/", view=views.create_customer, name="create-customer"),
    path(
        "update-customers/<str:pk>", view=views.update_customer, name="update-customer"
    ),
    path(
        "delete-customers/<str:pk>", view=views.delete_customer, name="delete-customer"
    ),
]
