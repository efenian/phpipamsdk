""" Tools Locations Api Calls """

from ..phpipam import PhpIpamApi
from ..phpipam import build_payload


class ToolsLocationsApi(object):
    """ Tools Locations Api Class """

    _objmap = {
        'id': 'id',
        'name': 'name',
        'address': 'address',
        'lat': 'lat',
        'long': 'long',
        'description': 'description'
    }

    def __init__(self, phpipam=None):
        if phpipam:
            self.phpipam = phpipam
        else:
            self.phpipam = PhpIpamApi()

    def list_tools_locations(self):
        """ get locations list """
        uri = 'tools/locations/'
        result = self.phpipam.api_send_request(path=uri, method='get')
        return result

    def get_tools_location(self, location_id=''):
        """ get locations list """
        uri = 'tools/locations/' + str(location_id) + '/'
        result = self.phpipam.api_send_request(path=uri, method='get')
        return result

    def list_tools_location_subnets(self, location_id=''):
        """ get locations subnets list """
        uri = 'tools/locations/' + str(location_id) + '/subnets/'
        result = self.phpipam.api_send_request(path=uri, method='get')
        return result

    def list_tools_location_devices(self, location_id=''):
        """ get locations device list """
        uri = 'tools/locations/' + str(location_id) + '/devices/'
        result = self.phpipam.api_send_request(path=uri, method='get')
        return result

    def list_tools_location_racks(self, location_id=''):
        """ get locations rack list """
        uri = 'tools/locations/' + str(location_id) + '/racks/'
        result = self.phpipam.api_send_request(path=uri, method='get')
        return result

    def add_tools_location(self, name='', **kwargs):
        """ add new location """
        payload = {
            'name': name,
        }
        payload.update(build_payload(self._objmap, **kwargs))
        uri = 'tools/locations/'
        result = self.phpipam.api_send_request(
            path=uri, method='post', payload=payload)
        return result

    def update_tools_location(self, location_id='', **kwargs):
        """ update location """
        payload = {}
        payload.update(build_payload(self._objmap, **kwargs))
        uri = 'tools/locations/' + str(location_id) + '/'
        result = self.phpipam.api_send_request(
            path=uri, method='patch', payload=payload)
        return result

    def del_tools_location(self, location_id=''):
        """ get location """
        uri = 'tools/locations/' + str(location_id) + '/'
        result = self.phpipam.api_send_request(path=uri, method='delete')
        return result
