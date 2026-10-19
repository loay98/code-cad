
from src.models.mounting_plate import make_part


def test_mounting_plate_is_valid():
    part = make_part()

    assert part.is_valid
    assert len(part.solids()) == 1
    assert part.volume > 0


def test_mounting_plate_dimensions():
    part = make_part()
    bounds = part.bounding_box()

    assert abs(bounds.size.X - 100.0) < 1e-5
    assert abs(bounds.size.Y - 60.0) < 1e-5
    assert abs(bounds.size.Z - 8.0) < 1e-5
