from rest_framework.viewsets import ModelViewSet

from product.serializers.product_serializer import ProductSerializer
from product.models import Product

class ProductViewSet(ModelViewSet):

    serializer_class = ProductSerializer
    
    def get_queryset(self):
        return Product.objects.all()