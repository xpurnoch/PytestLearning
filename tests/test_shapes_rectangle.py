import source.shapes as shapes
import pytest

@pytest.fixture
def my_rectangle():
    return shapes.Rectangle(10, 20)

@pytest.fixture
def other_rectangle():
    return shapes.Rectangle(5, 6)

@pytest.fixture
def same_rectangle():
    return shapes.Rectangle(10, 20)

@pytest.fixture
def circle():
    return shapes.Circle(5)

def test_area(my_rectangle):
    assert my_rectangle.area() == 200

def test_perimeter(my_rectangle):
    assert my_rectangle.perimeter() == 60

def test_not_equal(my_rectangle, other_rectangle):
    assert my_rectangle != other_rectangle

def test_equal(my_rectangle, same_rectangle):
    assert my_rectangle == same_rectangle

def test_circle_not_rectangle(circle, same_rectangle):
    assert circle != same_rectangle
