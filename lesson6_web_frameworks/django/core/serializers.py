from django.core.serializers.json import DjangoJSONEncoder
from .models import Product

class ProductSerializer(DjangoJSONEncoder):
    def default(self, o):
        if isinstance(o, Product):
            result = {}
            result['id'] = o.id
            result['slug'] = o.slug
            result['name'] = o.name
            result['description'] = o.description
            return result 
        return super().default(o)