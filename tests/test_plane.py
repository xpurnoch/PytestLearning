import pytest
import source.plane as plane_module

class TestPlane:
    def setup_method(self):
        self.plane = plane_module.Plane(12, 400)

    def test_plane_initialization(self):
        assert self.plane.get_id() == 12
        assert self.plane.get_speed() == 400
        assert self.plane.get_motors() == 1

    def test_add_motor(self):
        self.plane.add_motor(100)
        assert self.plane.get_speed() == 500
        assert self.plane.get_motors() == 2

    def test_plane_equality(self):
        a = plane_module.Plane(12, 400)
        b = plane_module.Plane(12, 400)
        assert a == b

    def test_plane_not_equal(self):
        other_plane = plane_module.Plane(13, 450)
        assert self.plane != other_plane
