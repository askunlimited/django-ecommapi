import pytest

pytestmark = pytest.mark.django_db

class TestCategoryModel:
  def test_str_method(self, category_factory):
    # Arrange
    # Act
    category = category_factory()
    # x = category_factory()
    # Assert
    assert str(category) == category.name
    # assert x.__str__() == "test_category"


class TestBrandModel:
  def test_str_method(self, brand_factory):
    # Arrange
    # Act
    brand = brand_factory()
    # x = brand_factory()
    # Assert
    assert str(brand) == brand.name
    # assert x.__str__() == "test_brand"



class TestProductModel:
  def test_str_method(self, product_factory):
    # Arrange
    # Act
    # product = product_factory()
    x = product_factory()
    # Assert
    # assert str(product) == "test_product"
    assert x.__str__() == "test_product"