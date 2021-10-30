from django.urls import path

from . import views

app_name = "chart"

urlpatterns = [
    path('', views.statistics_view, name='shop-statistics'),
    path(
        'filter-options/',
        views.get_filter_options,
        name='chart-filter-options',
    ),
    path('sales/<int:year>/', views.get_policy_chart, name='chart-sales'),
]
