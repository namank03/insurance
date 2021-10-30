from django.urls import path

from insurance.base.views import create_policy, policy_view

app_name = "base"

urlpatterns = [
    path("", view=policy_view, name="policies"),
    path('create-policy/', create_policy, name="createPolicy"),
]
