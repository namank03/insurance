# shop/views.py

from django.db.models import Count, F
from django.db.models.functions import ExtractMonth, ExtractYear
from django.http import JsonResponse
from django.shortcuts import render

from insurance.base.models import Customer, Policy
from insurance.utils.charts import colorPrimary, get_year_dict, months


def get_filter_options(request):
    grouped_policies = (
        Policy.objects.annotate(year=ExtractYear('created_at'))
        .values('year')
        .order_by('-year')
        .distinct()
    )
    grouped_regions = Customer.objects.values('region').distinct()

    year_options = [policy['year'] for policy in grouped_policies]
    region_options = [region['region'] for region in grouped_regions]

    return JsonResponse(
        {'year_options': year_options, 'region_options': region_options}
    )


def get_policy_chart(request, year):
    policies = Policy.objects.filter(created_at__year=year)
    grouped_policies = (
        policies.annotate(price=F('premium'))
        .annotate(month=ExtractMonth('created_at'))
        .values('month')
        .annotate(average=Count('premium'))
        .values('month', 'average')
        .order_by('month')
    )

    sales_dict = get_year_dict()

    for group in grouped_policies:
        sales_dict[months[group['month'] - 1]] = round(group['average'], 2)

    return JsonResponse(
        {
            'title': f'Policies {year}',
            'data': {
                'labels': list(sales_dict.keys()),
                'datasets': [
                    {
                        'label': 'Count',
                        'backgroundColor': colorPrimary,
                        'borderColor': colorPrimary,
                        'data': list(sales_dict.values()),
                    }
                ],
            },
        }
    )


def statistics_view(request):
    return render(request, 'charts/statistics.html', {})
