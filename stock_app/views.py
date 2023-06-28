from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from .permissions import myDjangoModelPermissions
# Create your views here.

import django_filters


class CategoryFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Category
        fields = ['name']

class CategoryView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ["name"]
    # filterset_fields = ["name"]
    filterset_class = CategoryFilter

    # change the serializer
    def get_serializer_class(self):
        if self.request.query_params.get("name"):
            return CategoryProductSerializer
        return super().get_serializer_class()

class BrandView(ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

class FirmView(ModelViewSet):
    queryset = Firm.objects.all()
    serializer_class = FirmSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ["name"]
    filterset_fields = ["name", "address", "phone"]
    # permission_classes = [IsAuthenticated]
    # permission_classes = [DjangoModelPermissions]
    permission_classes = [myDjangoModelPermissions]

class ProductView(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class PurchasesView(ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchasesSerializer

class SalesView(ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SalesSerializer
