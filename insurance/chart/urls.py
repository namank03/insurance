from django.urls import path

from . import views

app_name = "chart"

urlpatterns = [
    path('statistics/', views.statistics_view, name='shop-statistics'),
    path(
        'statistics/chart/filter-options/',
        views.get_filter_options,
        name='chart-filter-options',
    ),
    path(
        'statistics/chart/sales/<int:year>/', views.get_sales_chart, name='chart-sales'
    ),
]
