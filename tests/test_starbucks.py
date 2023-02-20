from app.distance_methods import get_geo_location_by_address
from config import Config


def test_configure_radius():
    new_val = 7.0
    Config.radius = new_val
    assert Config.radius == new_val


def test_configure_brand_name():
    new_val = 'KFC'
    Config.brand_name = new_val
    assert Config.brand_name == new_val


def test_get_geo_location():
    address = '1 Pace Plaza, New York'
    geo_correct_res = (40.7110664, -74.00462571728673)
    assert get_geo_location_by_address(address) == geo_correct_res