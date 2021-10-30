from django.urls import path

from insurance.base.views import create_policy, deletePolicy, policy_view

app_name = "base"

urlpatterns = [
    path("", view=policy_view, name="policies"),
    path('create-policy/', create_policy, name="createPolicy"),
    path('delete-policy/<str:pk>', deletePolicy, name="deletePolicy"),
]
