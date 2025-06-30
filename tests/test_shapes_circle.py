import source.shapes as shapes
from pytest import approx

class TestCircle:
    def setup_method(self):
        self.circle = shapes.Circle(5)

    def test_area(self):
        assert self.circle.area() == 78.5

    def test_perimeter(self):
        assert self.circle.perimeter() == approx(31.4)

    def test_radius_change(self):
        self.circle.radius = 10
        assert self.circle.area() == 314.0
        assert self.circle.perimeter() == approx(62.8)
