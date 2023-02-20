import certifi
import ssl
import geopy.geocoders
import geopy.distance
from geopy.geocoders import Nominatim
import time
from db.db import Db
from config import Config
import math
from logger.logger import logger

ctx = ssl.create_default_context(cafile=certifi.where())
geopy.geocoders.options.default_ssl_context = ctx
geolocator = Nominatim(scheme='http', user_agent="myGeocoder")

data = Db("data.csv")


def get_geo_location_by_address(address):
    try:
        location = geolocator.geocode(address, timeout=5)
        return location.latitude, location.longitude
    except Exception as e:
        logger.error("Error: geocode failed on input %s with message %s" % e)


def calculate_branches_in_radius(address):
    relevant_data = data.get_data(Config.brand_name)
    start = time.time()
    address_geo_location = get_geo_location_by_address(address)
    res = list()
    for row in relevant_data:
        geo_location = row['Latitude'], row['Longitude']
        if not math.isnan(geo_location[0]) and not math.isnan(geo_location[1]):
            dist = geopy.distance.geodesic(geo_location, address_geo_location).km
            if dist <= Config.radius:
                res.append(row['Name'])
    end = time.time()
    print(end - start)
    return res
