""" Tools Devices Api Calls """

from ..phpipam import PhpIpamApi
from ..phpipam import build_payload

class ToolsDevicesApi(object):
    """ Tools Devices Api Class """

    _objmap = {
        'id' : 'id',
        'hostname' : 'hostname',
        'ip_addr' : 'ip_addr',
        'ip' : 'ip',
        'type_id' : 'type',
        'vendor' : 'vendor',
        'model' : 'model',
        'sections' : 'sections',
        'location_id' : 'location',
        'rack_id' : 'rack',
        'rack_size' : 'rack_size',
        'rack_start' : 'rack_start',
        'snmp_community' : 'snmp_community',
        'snmp_port' : 'snmp_port',
        'snmp_queries' : 'snmp_queries',
        'snmp_timeout' : 'snmp_timeout',
        'snmp_version' : 'snmp_version',
        'description' : 'description'
    }


    def __init__(self, phpipam=None):
        if phpipam:
            self.phpipam = phpipam
        else:
            self.phpipam = PhpIpamApi()


    def list_tools_devices(self):
        """ get device list """
        uri = 'tools/devices/'
        result = self.phpipam.api_send_request(path=uri, method='get')
        return result


    def get_tools_device(self, device_id=''):
        """ get device  """
        uri = 'tools/devices/' + str(device_id) + '/'
        result = self.phpipam.api_send_request(path=uri, method='get')
        return result


    def add_tools_device(self, hostname='', **kwargs):
        """ add new device """
        payload = {
            'hostname' : hostname,
        }
        payload.update(build_payload(self._objmap, **kwargs))
        uri = 'tools/devices/'
        result = self.phpipam.api_send_request(
            path=uri, method='post', payload=payload)
        return result


    def update_tools_device(self, device_id='', **kwargs):
        """ update device """
        payload = {}
        payload.update(build_payload(self._objmap, **kwargs))
        uri = 'tools/devices/' + str(device_id) + '/'
        result = self.phpipam.api_send_request(
            path=uri, method='patch', payload=payload)
        return result


    def del_tools_device(self, device_id=''):
        """ delete device """
        uri = 'tools/devices/' + str(device_id) + '/'
        result = self.phpipam.api_send_request(path=uri, method='delete')
        return result
