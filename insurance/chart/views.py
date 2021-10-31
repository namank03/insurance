# shop/views.py

from django.db.models import Count, F
from django.db.models.functions import ExtractMonth, ExtractYear
from django.http import JsonResponse
from django.shortcuts import render

from insurance.base.models import Policy
from insurance.utils.charts import colorPrimary, get_year_dict, months


def get_filter_options(request):
    # q = request.GET.get("q") if request.GET.get("q") is not None else ""

    grouped_policies = (
        Policy.objects.annotate(year=ExtractYear("date_of_purchase"))
        .values("year")
        .order_by("-year")
        .distinct()
    )

    year_options = [policy["year"] for policy in grouped_policies]
    region_options = ["east", "west", "south", "north"]

    return JsonResponse(
        {"year_options": year_options, "region_options": region_options}
    )


def get_policy_chart(request, year, region):
    policies = Policy.objects.filter(
        date_of_purchase__year=year, customer__region=region
    )
    grouped_policies = (
        policies.annotate(price=F("premium"))
        .annotate(month=ExtractMonth("date_of_purchase"))
        .values("month")
        .annotate(average=Count("premium"))
        .values("month", "average")
        .order_by("month")
    )

    policy_dict = get_year_dict()

    for group in grouped_policies:
        policy_dict[months[group["month"] - 1]] = round(group["average"], 2)

    return JsonResponse(
        {
            "title": f"Policies {year} -  Region {region.upper()}",
            "data": {
                "labels": list(policy_dict.keys()),
                "datasets": [
                    {
                        "label": "Count",
                        "backgroundColor": colorPrimary,
                        "borderColor": colorPrimary,
                        "data": list(policy_dict.values()),
                    }
                ],
            },
        }
    )


def statistics_view(request):
    return render(request, "charts/statistics.html", {})
