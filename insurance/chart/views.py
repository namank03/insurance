# shop/views.py

from django.db.models import Count, F
from django.db.models.functions import ExtractMonth, ExtractYear
from django.http import JsonResponse
from django.shortcuts import render

from insurance.base.models import Customer, Policy
from insurance.utils.charts import (
    colorPrimary,
    generate_color_palette,
    get_year_dict,
    months,
)


def get_filter_options(request):
    # q = request.GET.get("q") if request.GET.get("q") is not None else ""
    grouped_policies = (
        Policy.objects.annotate(year=ExtractYear("date_of_purchase"))
        .values("year")
        .order_by("-year")
        .distinct()
    )

    year_options = [policy["year"] for policy in grouped_policies]
    region_options = ["EAST", "WEST", "SOUTH", "NORTH"]

    return JsonResponse(
        {"year_options": year_options, "region_options": region_options}
    )


def get_policy_chart(request, year, region):
    policies = Policy.objects.filter(
        date_of_purchase__year=year, customer__region=region
    )
    grouped_policies = (
        policies.annotate(month=ExtractMonth("date_of_purchase"))
        .values("month")
        .annotate(count=Count("premium"))
        .values("month", "count")
        .order_by("month")
    )

    policy_dict = get_year_dict()

    for group in grouped_policies:
        policy_dict[months[group["month"] - 1]] = round(group["count"], 2)

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


def get_policy_pie_chart(request, year, region):
    policies = Policy.objects.filter(date_of_purchase__year=year)

    grouped_policies = (
        policies.values('customer__region')
        .annotate(count=Count('id'))
        .values('customer__region', 'count')
        .order_by('customer__region')
    )

    region_dict = {region[1]: 0 for region in Customer.REGION_CHOICES}

    for group in grouped_policies:
        region_dict[dict(Customer.REGION_CHOICES)[group['customer__region']]] = group[
            'count'
        ]

    return JsonResponse(
        {
            'title': f'Policies Purchased/Region in {year}',
            'data': {
                'labels': list(region_dict.keys()),
                'datasets': [
                    {
                        'label': 'Amount ($)',
                        'backgroundColor': generate_color_palette(len(region_dict)),
                        'borderColor': generate_color_palette(len(region_dict)),
                        'data': list(region_dict.values()),
                    }
                ],
            },
        }
    )


def statistics_view(request):
    return render(request, 'charts/statistics.html', {})
