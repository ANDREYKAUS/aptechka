import math


def lonlat_distance(a, b):
	degree_to_meters_factor = 111 * 1000
	a_long, a_lat = a
	b_long, b_lat = b

	radiance_lattitude = math.radians((a_lat + b_lat) / 2)
	lat_lon_factor = math.cos(radiance_lattitude)

	dx = abs(a_long - b_long) * degree_to_meters_factor * lat_lon_factor
	dy = abs(a_lat - b_lat) * degree_to_meters_factor

	distance = math.sqrt(dx ** 2 + dy ** 2)

	return distance