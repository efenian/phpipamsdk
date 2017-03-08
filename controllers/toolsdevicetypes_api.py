""" Tools Device Types Api Calls """

from ..phpipam import PhpIpamApi
from ..phpipam import build_payload

class ToolsDeviceTypesApi(object):
    """ Tools Devices Api Class """

    _objmap = {
        'id' : 'id',
        'name' : 'name',
        'description' : 'description'
    }


    def __init__(self, phpipam=None):
        if phpipam:
            self.phpipam = phpipam
        else:
            self.phpipam = PhpIpamApi()


    def list_tools_devicetypes(self):
        """ get device type list """
        uri = 'tools/devicetypes/'
        result = self.phpipam.api_send_request(path=uri, method='get')
        return result


    def list_tools_devicetype_devices(self, devicetype_id=''):
        """ get device type devices """
        uri = 'tools/devicetypes/' + str(devicetype_id) + '/devices/'
        result = self.phpipam.api_send_request(path=uri, method='get')
        return result


    def get_tools_devicetype(self, devicetype_id=''):
        """ get device type """
        uri = 'tools/devicetypes/' + str(devicetype_id) + '/'
        result = self.phpipam.api_send_request(path=uri, method='get')
        return result


    def add_tools_devicetype(self, name='', **kwargs):
        """ add new devicetype """
        payload = {
            'name' : name,
        }
        payload.update(build_payload(self._objmap, **kwargs))
        uri = 'tools/devicetypes/'
        result = self.phpipam.api_send_request(
            path=uri, method='post', payload=payload)
        return result


    def update_tools_devicetype(self, devicetype_id='', **kwargs):
        """ update devicetype """
        payload = {}
        payload.update(build_payload(self._objmap, **kwargs))
        uri = 'tools/devicetypes/' + str(devicetype_id) + '/'
        result = self.phpipam.api_send_request(
            path=uri, method='patch', payload=payload)
        return result


    def del_tools_devicetype(self, devicetype_id=''):
        """ delete devicetype """
        uri = 'tools/devicetypes/' + str(devicetype_id) + '/'
        result = self.phpipam.api_send_request(path=uri, method='delete')
        return result
        