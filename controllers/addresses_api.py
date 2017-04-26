""" Addresses Api Calls """

from ..phpipam import PhpIpamApi
from ..phpipam import build_payload


class AddressesApi(object):
    """ Addresses Api Class """

    _objmap = {
        'id': 'id',
        'subnet_id': 'subnetId',
        'ip': 'ip',
        'is_gateway': 'is_gateway',
        'description': 'description',
        'hostname': 'hostname',
        'mac': 'mac',
        'owner': 'owner',
        'tag_id': 'tag',
        'ptr_ignore': 'PTRignore',
        'ptr_id': 'PTR',
        'device_id': 'deviceId',
        'port': 'port',
        'note': 'note',
        'exclude_ping': 'excludePing'
    }

    def __init__(self, phpipam=None):
        if phpipam:
            self.phpipam = phpipam
        else:
            self.phpipam = PhpIpamApi()

    def get_address(self, address_id=''):
        """ get IP address """
        uri = 'addresses/' + str(address_id) + '/'
        result = self.phpipam.api_send_request(path=uri, method='get')
        return result

    def ping_address(self, address_id=''):
        """ ping IP address """
        uri = 'addresses/' + str(address_id) + '/ping/'
        result = self.phpipam.api_send_request(path=uri, method='get')
        return result

    def get_address_from_subnet(self, address='', subnet_id=''):
        """ get IP address from subnet """
        uri = 'addresses/' + str(address) + '/' + str(subnet_id) + '/'
        result = self.phpipam.api_send_request(path=uri, method='get')
        return result

    def search_address(self, address=''):
        """ search IP address """
        uri = 'addresses/search/' + str(address) + '/'
        result = self.phpipam.api_send_request(path=uri, method='get')
        return result

    def search_hostname(self, hostname=''):
        """ search for hostname """
        uri = 'addresses/search/' + str(hostname) + '/'
        result = self.phpipam.api_send_request(path=uri, method='get')
        return result

    def get_address_first_free_subnet(self, subnet_id=''):
        """ get first available address from subnet """
        uri = 'addresses/first_free/' + str(subnet_id) + '/'
        result = self.phpipam.api_send_request(path=uri, method='get')
        return result

    def list_address_custom_fields(self):
        """ list address custom fields """
        uri = 'addresses/custom_fields/'
        result = self.phpipam.api_send_request(path=uri, method='get')
        return result

    def list_address_tags(self):
        """ list address tags """
        uri = 'addresses/tags/'
        result = self.phpipam.api_send_request(path=uri, method='get')
        return result

    def get_address_tag(self, tag_id=''):
        """ get specific tag """
        uri = 'addresses/tags/' + str(tag_id) + '/'
        result = self.phpipam.api_send_request(path=uri, method='get')
        return result

    def list_addresses_tag(self, tag_id=''):
        """ list addresses for tag """
        uri = 'addresses/tags/' + str(tag_id) + '/addresses/'
        result = self.phpipam.api_send_request(path=uri, method='get')
        return result

    def add_address(self, subnet_id='', ip_addr='', **kwargs):
        """ add IP address """
        payload = {
            'subnetId': str(subnet_id),
            'ip': ip_addr
        }
        payload.update(build_payload(self._objmap, **kwargs))
        uri = 'addresses/'
        result = self.phpipam.api_send_request(
            path=uri, method='post', payload=payload)
        return result

    def add_address_first_free(self, subnet_id='', **kwargs):
        """ add first free IP address """
        payload = {}
        payload.update(build_payload(self._objmap, **kwargs))
        uri = 'addresses/' + str(subnet_id) + '/'
        result = self.phpipam.api_send_request(
            path=uri, method='post', payload=payload)
        return result

    def update_address(self, address_id='', **kwargs):
        """ update IP address """
        payload = {}
        payload.update(build_payload(self._objmap, **kwargs))
        uri = 'addresses/' + str(address_id) + '/'
        result = self.phpipam.api_send_request(
            path=uri, method='patch', payload=payload)
        return result

    def del_address(self, address_id='', **kwargs):
        """ delete IP address """
        payload = {}
        if 'remove_dns' in kwargs:
            payload['remove_dns'] = kwargs['remove_dns']
        uri = 'addresses/' + str(address_id) + '/'
        result = self.phpipam.api_send_request(
            path=uri, method='delete', payload=payload)
        return result

    def del_address_subnet(self, address='', subnet_id=''):
        """ delete IP address from subnet """
        uri = 'addresses/' + str(address) + '/' + str(subnet_id) + '/'
        result = self.phpipam.api_send_request(path=uri, method='delete')
        return result
