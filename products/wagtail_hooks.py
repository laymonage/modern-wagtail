from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet

from products.models import Product


class ProductViewSet(SnippetViewSet):
    model = Product
    search_fields = ["name"]
    list_display = ["name", "final_price", "stock"]
    list_export = ["name", "price", "discount", "final_price", "stock"]
    list_filter = {"discount": ["gte"], "stock": ["lte"]}


register_snippet(ProductViewSet)
