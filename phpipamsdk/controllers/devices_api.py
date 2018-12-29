""" Devices Api Calls """

from phpipamsdk.phpipam import PhpIpamApi
from phpipamsdk.phpipam import build_payload


class DevicesApi(object):
    """ Devices Api Class """

    _objmap = {
        'id': 'id',
        'hostname': 'hostname',
        'ip_addr': 'ip_addr',
        'ip': 'ip',
        'type_id': 'type',
        'vendor': 'vendor',
        'model': 'model',
        'sections': 'sections',
        'location_id': 'location',
        'rack_id': 'rack',
        'rack_size': 'rack_size',
        'rack_start': 'rack_start',
        'snmp_community': 'snmp_community',
        'snmp_port': 'snmp_port',
        'snmp_queries': 'snmp_queries',
        'snmp_timeout': 'snmp_timeout',
        'snmp_version': 'snmp_version',
        'snmp_v3_auth_protocol': 'snmp_v3_auth_protocol',
        'snmp_v3_auth_pass': 'snmp_v3_auth_pass',
        'snmp_v3_priv_protocol': 'snmp_v3_priv_protocol',
        'snmp_v3_priv_pass': 'snmp_v3_priv_pass',
        'snmp_v3_ctx_name': 'snmp_v3_ctx_name',
        'snmp_v3_ctx_engine_id': 'snmp_v3_ctx_engine_id',
        'description': 'description'
    }

    def __init__(self, phpipam=None):
        if phpipam:
            self.phpipam = phpipam
        else:
            self.phpipam = PhpIpamApi()

    def list_devices(self):
        """ get device list """
        uri = 'devices/'
        result = self.phpipam.api_send_request(path=uri, method='get')
        return result

    def get_device(self, device_id=''):
        """ get device  """
        uri = 'devices/' + str(device_id) + '/'
        result = self.phpipam.api_send_request(path=uri, method='get')
        return result

    def get_device_subnets(self, device_id=''):
        """ get device subnets """
        uri = 'devices/' + str(device_id) + '/subnets/'
        result = self.phpipam.api_send_request(path=uri, method='get')
        return result

    def get_device_addresses(self, device_id=''):
        """ get device addresses """
        uri = 'devices/' + str(device_id) + '/addresses/'
        result = self.phpipam.api_send_request(path=uri, method='get')
        return result

    def search_device(self, device=''):
        """ search IP address """
        uri = 'devices/search/' + str(device) + '/'
        result = self.phpipam.api_send_request(path=uri, method='get')
        return result

    def add_device(self, hostname='', **kwargs):
        """ add new device """
        payload = {
            'hostname': hostname,
        }
        payload.update(build_payload(self._objmap, **kwargs))
        uri = 'devices/'
        result = self.phpipam.api_send_request(
            path=uri, method='post', payload=payload)
        return result

    def update_device(self, device_id='', **kwargs):
        """ update device """
        payload = {}
        payload.update(build_payload(self._objmap, **kwargs))
        uri = 'devices/' + str(device_id) + '/'
        result = self.phpipam.api_send_request(
            path=uri, method='patch', payload=payload)
        return result

    def del_device(self, device_id=''):
        """ delete device """
        uri = 'devices/' + str(device_id) + '/'
        result = self.phpipam.api_send_request(path=uri, method='delete')
        return result
