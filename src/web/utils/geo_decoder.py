import time
from flask import current_app

from googlemaps import Client as GoogleMaps
from googleplaces import GooglePlaces, types, lang


class GeoEncoder:

    def __init__(self):
        if current_app.config['GOOGLE_API_KEY'] == "":
            raise Exception("No google api key in enviroment variable")
        self.api_key = current_app.config['GOOGLE_API_KEY']
        self.gmap = GoogleMaps(self.api_key)
        self.places = GooglePlaces(self.api_key)

    def get_geo_coordinates(self, input_string, type_of_input, *args, **kwargs):
        radius = kwargs.get('radius', 1000)
        city = kwargs.get('city', 'WARSZAWA')
        if str(type_of_input).lower() == 'bus_stop':
            geocode = self.gmap.geocode(input_string + ', ' + city)
            geo_dict = geocode[0]['geometry']['location']
            lat, lon = self.obtain_lat_lon_from_address(lat_lon_dict=geo_dict,
                                                   bus_stop_name=input_string,
                                                   radius=radius)
            if lat == 0 and lon == 0: return print('Location for %s, %s not found' % (input_string, city))
            print('Location for %s is found at lat %f, lon %f' % (input_string, lat, lon))
            return lat, lon
        elif str(type_of_input).lower() == 'street':
            geocode = self.gmap.geocode(input_string + ', ' + city)
            lat_lon_dict = geocode[0]['geometry']['location']
            lat, lon = lat_lon_dict['lat'], lat_lon_dict['lng']
            print('Location for %s is found at lat %f, lon %f' % (input_string, lat, lon))
            return lat, lon
        else:
            print('Choose type bus_stop for bus stop name input or street for street name input')

    def obtain_lat_lon_from_address(self, lat_lon_dict, bus_stop_name, radius):

        fetched = 0

        query_result = self.places.nearby_search(
                                            language='POLISH',
                                            lat_lng=lat_lon_dict,
                                            radius=radius,
                                            types=[types.TYPE_BUS_STATION,
                                                   types.TYPE_SUBWAY_STATION,
                                                   types.TYPE_TRAIN_STATION])
        fetched += 1
        for entry in query_result.places:
            print('[%i] %s' % (fetched, entry.name))
            if str(entry.name).lower().__contains__(str(bus_stop_name).lower()):
                print('[%i] %s stop was SELECTED' % (fetched, entry.name))
                return entry.geo_location['lat'], entry.geo_location['lng']

        while query_result.has_next_page_token is True:
            time.sleep(5)
            query_result_next_page = self.places.nearby_search(pagetoken=query_result.next_page_token)
            fetched += 1
            for entry in query_result_next_page.places:
                print('[%i] %s' % (fetched, entry.name))
                if str(entry.name).lower() == str(bus_stop_name).lower():
                    print('[%i] %s stop was SELECTED' % (fetched, entry.name))
                    return entry.geo_location
            query_result = query_result_next_page
        return 0, 0
