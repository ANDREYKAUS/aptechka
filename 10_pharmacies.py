from geocoder import *
from business import *
from distance import *
from map_show_addi import *
import sys


def main():
    mark = {
        'green': 'pm2gnm',
        'blue': 'pm2blm',
        'gray': 'pm2grm',
    }

    address = ' '.join(sys.argv[1:])
    # address = 'Красноярск Дубровинского, 1и'
    ad_lat, ad_lon = get_coordinates(address)

    address_ll = f'{ad_lat},{ad_lon}'
    delta = 0.001
    spn = '0.001,0.001'
    while True:
        orgs = find_businesses('аптека', address_ll, spn)
        print(len(orgs))
        if len(orgs) < 10:
            delta += 0.001
            spn = f'{delta},{delta}'
        else:
            break
    points = []
    for org in orgs:
        time = org['properties']['CompanyMetaData'].get('Hours', '')
        if not time:
            color = mark['gray']
        else:
            if 'круглосуточно' in time['text']:
                color = mark['green']
            else:
                color = mark['blue']
        org_point = org['geometry']['coordinates']
        point = f'{org_point[0]},{org_point[1]},{color}'
        points.append(point)

    open_image(address_ll, spn, points)


if __name__ == '__main__':
    main()
