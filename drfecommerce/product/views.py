# from django.db import connection
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import action
# from pygments import highlight
# from pygments.formatters import TerminalFormatter
# from pygments.lexers.sql import SqlLexer
# from sqlparse import format
from drf_spectacular.utils import extend_schema
from .models import Category, Brand, Product
from .serializers import CategorySerializer, BrandSerializer, ProductSerializer

class CategoryView(viewsets.ViewSet):
    """A Simple viewset for viewing categories"""
    queryset = Category.objects.all()
    
    @extend_schema(responses=CategorySerializer)
    def list(self, request):
        serializer = CategorySerializer(self.queryset, many=True)
        return Response(serializer.data)
    
class BrandView(viewsets.ViewSet):
    """A Simple viewset for viewing brands"""
    queryset = Brand.objects.all()
    
    @extend_schema(responses=BrandSerializer)
    def list(self, request):
        serializer = BrandSerializer(self.queryset, many=True)
        return Response(serializer.data)

class ProductView(viewsets.ViewSet):
    """A Simple viewset for viewing brands"""
    queryset = Product.objects.all().isactive()
    lookup_field = "slug"
    
    def retrieve(self, request, slug=None):
        serializer = ProductSerializer(
            Product.queryset.filter(slug=slug)
            .select_related("category", "brand")
            .prefetch_related("product_line__product_image"), many=True)
        # x = self.queryset.filter(slug=slug)
        # sqlformatted = format(str(x.query), reindent=True)
        # print(highlight(sqlformatted, SqlLexer(), TerminalFormatter()))
        return Response(serializer.data)
    
    @extend_schema(responses=ProductSerializer)
    def list(self, request):
        serializer = ProductSerializer(self.queryset, many=True)
        return Response(serializer.data)
    
    @action(methods=["get"], detail=False, url_path=r"category/(?P<category>\w+)/all", url_name="all")
    def list_product_by_category(self, request, category=None):
        """This is endpoint to return products by category"""
        serializer = ProductSerializer(self.queryset.filter(category__name=category), many=True)
        return Response(serializer.data)
