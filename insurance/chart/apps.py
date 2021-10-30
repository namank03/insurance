from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ChartConfig(AppConfig):
    name = "insurance.chart"
    verbose_name = _("Chart")

    def ready(self):
        try:
            import insurance.chart.signals  # noqa F401
        except ImportError:
            pass
