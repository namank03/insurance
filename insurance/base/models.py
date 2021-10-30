from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Customer(BaseModel):
    """Model definition for Customer."""

    GENDER_CHOICES = (
        ("Male", "Male"),
        ("Female", "Female"),
        ("Other", "Other"),
    )

    INCOME_CHOICES = (
        ("0-25k", "0-$25k"),
        (">$70", ">$70K"),
        ("$25-$70", "$25-$70K"),
    )

    REGION_CHOICES = (
        ("east", "east"),
        ("west", "west"),
        ("south", "south"),
        ("north", "north"),
    )

    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=50, choices=GENDER_CHOICES)
    income_group = models.CharField(max_length=50, choices=INCOME_CHOICES)
    region = models.CharField(max_length=50, choices=REGION_CHOICES)
    marital_status = models.BooleanField(default=False)

    class Meta:
        """Meta definition for Customer."""

        verbose_name = "Customer"
        verbose_name_plural = "Customers"

    def __str__(self):
        """Unicode representation of Customer."""
        return f"{self.name}_{self.id}"


class Policy(BaseModel):
    """Model definition for Policy."""

    FUEL_CHOICES = (
        ("CNG", "cng"),
        ("DIESEL", "diesel"),
        ("PETROL", "petrol"),
    )

    VEHICLE_SEGMENT = (
        ("A", "A"),
        ("B", "B"),
        ("C", "C"),
    )

    fuel = models.CharField(max_length=50, choices=FUEL_CHOICES)
    customer = models.ForeignKey(
        Customer, related_name="policies", on_delete=models.CASCADE
    )
    vehicle_segment = models.CharField(max_length=50, choices=VEHICLE_SEGMENT)
    premium = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100000)]
    )

    class Meta:
        """Meta definition for ClassRoom."""

        verbose_name = "Policy"
        verbose_name_plural = "Policies"
        ordering = ("created_at",)

    def __str__(self):
        """Unicode representation of ClassRoom."""
        return f"{self.vehicle_segment}_{self.id}"
