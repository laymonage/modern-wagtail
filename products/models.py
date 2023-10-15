from decimal import Decimal
from django.db import models

from wagtail.admin.panels import FieldPanel, PublishingPanel
from wagtail.models import (
    DraftStateMixin,
    LockableMixin,
    PreviewableMixin,
    RevisionMixin,
    WorkflowMixin,
)
from wagtail.snippets.models import register_snippet


@register_snippet
class Product(
    WorkflowMixin,
    DraftStateMixin,
    LockableMixin,
    RevisionMixin,
    PreviewableMixin,
    models.Model,
):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    discount = models.PositiveSmallIntegerField()
    stock = models.PositiveIntegerField()
    image_url = models.URLField(
        max_length=2047,
        blank=True,
        default="https://picsum.photos/256",
    )

    @property
    def final_price(self):
        return Decimal(
            self.price * (Decimal("1.0") - Decimal(str(self.discount)) / Decimal("100"))
        ).quantize(Decimal("1.00"))

    def __str__(self) -> str:
        return self.name

    panels = [
        FieldPanel("name"),
        FieldPanel("description"),
        FieldPanel("price"),
        FieldPanel("discount"),
        FieldPanel("stock"),
        FieldPanel("image_url"),
        PublishingPanel(),
    ]

    preview_modes = [
        ("index", "Index"),
        ("detail", "Detail"),
    ]
    default_preview_mode = "detail"

    def get_preview_template(self, request, preview_mode):
        return f"products/{preview_mode}.html"

    def get_preview_context(self, request, preview_mode):
        if preview_mode == "index":
            return {
                "products": [
                    self,
                    *Product.objects.filter(live=True).exclude(pk=self.pk),
                ]
            }
        return {"product": self}
