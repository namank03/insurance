from django.urls import path

from . import views

app_name = "chart"

urlpatterns = [
    path('', views.statistics_view, name='policy-statistics'),
    path(
        'filter-options/',
        views.get_filter_options,
        name='chart-filter-options',
    ),
    path('policy/<int:year>/<str:region>', views.get_policy_chart, name='chart-policy'),
    path(
        'policy-pie/<int:year>/<str:region>',
        views.get_policy_pie_chart,
        name='chart-policy-pie',
    ),
]
