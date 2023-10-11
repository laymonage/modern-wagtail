from django.db import models


class Product(models.Model):
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
        return self.price * (1 - self.discount / 100)

    def __str__(self) -> str:
        return self.name
