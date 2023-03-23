import pytest
pytestmark = pytest.mark.django_db

class TestCategoryModel:
    def test_string_method(self, category_factory):
        # Arrange
        # Action
        x = category_factory(name='test_category')
        # Assert
        assert x.__str__() == 'test_category'
        
class TestBrandModel:
    def test_string_method(self, brand_factory):
        # Arrange
        # Action
        x = brand_factory(name='test_brand')
        # Assert
        assert x.__str__() == 'test_brand'    
    
class TestProductModel:
    def test_string_method(self, product_factory):
        # Arrange
        # Action
        x = product_factory(name='test_product')
        # Assert
        assert x.__str__() == 'test_product'
    