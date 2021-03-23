from geocoder import *
from business import *
from distance import *
from map_show import *
import sys


toponym = ' '.join(sys.argv[1:])
ad_lat, ad_lon = get_coordinates(toponym)
address_ll = f'{ad_lat},{ad_lon}'
spn = '0.005,0.005'

org = find_business('аптека', address_ll, spn)
org_point = org['geometry']['coordinates']
org_lat, org_long = map(float, org_point)
org_ll = f'{org_lat},{org_long}'

open_image(address_ll, spn, org_ll)

# сниппет
name = org['properties']['CompanyMetaData']['name']
address = org['properties']['CompanyMetaData']['address']
time = org['properties']['CompanyMetaData']['Hours']['text']
distance = round(lonlat_distance((ad_lat, ad_lon), (org_lat, org_long)))

print(f'''
name={name}
address={address}
time={time}
distance={distance}м.
''')