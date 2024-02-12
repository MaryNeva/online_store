from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse

from products.models import Product, ProductCategory


class IndexViewTestCase(TestCase):

    def test_view(self):
        path = reverse('index')
        response = self.client.get(path)

        products = Product.objects.all()

        self.assertEquals(response.status_code, HTTPStatus.OK)
        self.assertEquals(response.context_data['title'], 'Store')
        self.assertTemplateUsed(response, 'products/index.html')
        self.assertEquals(response.context_data['object_list'], products)


class ProductListViewTestCase(TestCase):
    fixtures = ['categories.json', 'goods.json']

    def setUp(self) -> None:
        self.products = Product.objects.all()

    def test_list(self):
        path = reverse('products:index')
        response = self.client.get(path)

        self._common_tests(response)
        self.assertQuerysetEqual(response.context_data.get('object_list'), self._get_products_list(response), ordered=False)


    def test_list_with_category(self):
        category = ProductCategory.objects.first()
        path = reverse('products:category', kwargs={'category_id': category.id})
        response = self.client.get(path)

        self._common_tests(response)
        self.assertEquals(
            list(response.context_data['object_list']),
            self._get_products_list(response)
        )

    def _common_tests(self, response):
        self.assertEquals(response.status_code, HTTPStatus.OK)
        self.assertEquals(response.context_data['title'], 'Store - Каталог')
        self.assertTemplateUsed(response, 'products/products.html')

    @staticmethod
    def _get_items_count(response):
        paginator =response.context_data.get('paginator')
        return paginator.per_page if paginator else None

    def _get_products_list(self, response, filter_args: dict = None):
        if filter_args:
            products_list = Product.objects.filter(**filter_args)
        else:
            products_list = Product.objects.all()

        items_count = self._get_items_count(response)
        if items_count:
            products_list = products_list[:items_count]

        return list(products_list)