""" Tools Racks Api Calls """

from ..phpipam import PhpIpamApi
from ..phpipam import build_payload

class ToolsRacksApi(object):
    """ Tools Racks Api Class """

    _objmap = {
        'id' : 'id',
        'name' : 'name',
        'location_id' : 'location',
        'size' : 'size',
        'description' : 'description'
    }


    def __init__(self, phpipam=None):
        if phpipam:
            self.phpipam = phpipam
        else:
            self.phpipam = PhpIpamApi()


    def list_tools_racks(self):
        """ get racks list """
        uri = 'tools/racks/'
        result = self.phpipam.api_send_request(path=uri, method='get')
        return result


    def get_tools_rack(self, rack_id=''):
        """ get racks list """
        uri = 'tools/racks/' + str(rack_id) + '/'
        result = self.phpipam.api_send_request(path=uri, method='get')
        return result


    def list_tools_rack_devices(self, rack_id=''):
        """ get racks device list """
        uri = 'tools/racks/' + str(rack_id) + '/devices/'
        result = self.phpipam.api_send_request(path=uri, method='get')
        return result


    def add_tools_rack(self, name='', **kwargs):
        """ add new rack """
        payload = {
            'name' : name,
        }
        payload.update(build_payload(self._objmap, **kwargs))
        uri = 'tools/racks/'
        result = self.phpipam.api_send_request(
            path=uri, method='post', payload=payload)
        return result


    def update_tools_rack(self, rack_id='', **kwargs):
        """ update rack """
        payload = {}
        payload.update(build_payload(self._objmap, **kwargs))
        uri = 'tools/racks/' + str(rack_id) + '/'
        result = self.phpipam.api_send_request(
            path=uri, method='patch', payload=payload)
        return result


    def del_tools_rack(self, rack_id=''):
        """ get rack """
        uri = 'tools/racks/' + str(rack_id) + '/'
        result = self.phpipam.api_send_request(path=uri, method='delete')
        return result
