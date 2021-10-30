from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class BaseConfig(AppConfig):
    name = "insurance.base"
    verbose_name = _("Base")

    def ready(self):
        try:
            import insurance.base.signals  # noqa F401
        except ImportError:
            pass
