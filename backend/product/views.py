from django.shortcuts import render
from rest_framework.decorators import action

from .serializers import ProductSerializer
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin
from .models import Product
from rest_framework.response import Response


class ProductViewSet(ListModelMixin,
                     RetrieveModelMixin,
                     GenericViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    @action(methods=['GET'], detail=False)
    def latest(self, request):
        products = Product.objects.all()[:4]
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        product = self.get_object()
        serializer = ProductSerializer(product)
        return Response(serializer.data)