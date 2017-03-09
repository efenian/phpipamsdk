""" Tools Prefixes Api Calls """

from ..phpipam import PhpIpamApi
from ..phpipam import build_payload

class PrefixesApi(object):
    """ Tools Prefixes Api Class """

    _objmap = {
        'id' : 'id',
        'subnet' : 'subnet',
        'mask' : 'mask',
        'description' : 'description',
        'section_id' : 'sectionId',
        'linked_subnet_id' : 'linked_subnet',
        'vlan_id' : 'vlanId',
        'vrf_id' : 'vrfId',
        'master_subnet_id' : 'masterSubnetId',
        'nameserver_id' : 'nameserverId',
        'show_name' : 'showName',
        'permissions' : 'permissions',
        'dns_recursive' : 'DNSrecursive',
        'dns_records' : 'DNSrecords',
        'allow_requests' : 'allowRequests',
        'scan_agent_id' : 'scanAgent',
        'ping_subnet' : 'pingSubnet',
        'discover_subnet' : 'discoverSubnet',
        'is_folder' : 'isFolder',
        'is_full' : 'isFull',
        'state_id' : 'state',
        'threshold' : 'threshold',
        'location_id' : 'location',
        'subnet_id' : 'subnetId',
        'ip' : 'ip',
        'is_gateway' : 'is_gateway',
        'mac' : 'mac',
        'owner' : 'owner',
        'tag_id' : 'tag',
        'ptr_ignore' : 'PTRignore',
        'ptr_id' : 'PTR',
        'device_id' : 'deviceId',
        'port' : 'port',
        'note' : 'note',
        'exclude_ping' : 'excludePing'
    }


    def __init__(self, phpipam=None):
        if phpipam:
            self.phpipam = phpipam
        else:
            self.phpipam = PhpIpamApi()


    def list_prefixes_subnets(self, customer_type=''):
        """ get subnets list used to deliver new subnets """
        uri = 'prefix/' + str(customer_type) + '/'
        result = self.phpipam.api_send_request(path=uri, method='get')
        return result


    def list_prefixes_subnets_version(self, customer_type='', ip_version=''):
        """ get subnets list used to deliver new subnets by version """
        uri = (
            'prefix/' + str(customer_type)
            + '/' + str(ip_version) +'/')
        result = self.phpipam.api_send_request(path=uri, method='get')
        return result


    def list_prefixes_address(self, customer_type=''):
        """ get subnets list used to deliver new address """
        uri = 'prefix/' + str(customer_type) + '/address/'
        result = self.phpipam.api_send_request(path=uri, method='get')
        return result


    def list_prefixes_address_version(self, customer_type='', ip_version=''):
        """ get subnets list used to deliver new address by version """
        uri = (
            'prefix/' + str(customer_type)
            + '/address/' + str(ip_version) +'/')
        result = self.phpipam.api_send_request(path=uri, method='get')
        return result


    def get_prefixes_first_free_subnet(
            self, customer_type='', ip_version='', mask=''):
        """ get first available subnet """
        uri = (
            'prefix/' + str(customer_type)
            + '/' + str(ip_version) +'/' + str(mask) + '/')
        result = self.phpipam.api_send_request(path=uri, method='get')
        return result


    def get_prefixes_first_free_address(self, customer_type='', ip_version=''):
        """ get first available address """
        uri = (
            'prefix/' + str(customer_type)
            + '/' + str(ip_version) +'/address/')
        result = self.phpipam.api_send_request(path=uri, method='get')
        return result


    def add_prefixes_first_free_subnet(
            self, customer_type='', ip_version='', mask='', **kwargs):
        """ add first available subnet """
        payload = {}
        payload.update(build_payload(self._objmap, **kwargs))
        uri = (
            'prefix/' + str(customer_type)
            + '/' + str(ip_version) +'/' + str(mask) + '/')
        result = self.phpipam.api_send_request(
            path=uri, method='post', payload=payload)
        return result


    def add_prefixes_first_free_address(
            self, customer_type='', ip_version='', **kwargs):
        """ add first available subnet """
        payload = {}
        payload.update(build_payload(self._objmap, **kwargs))
        uri = (
            'prefix/' + str(customer_type)
            + '/' + str(ip_version) +'/address/')
        result = self.phpipam.api_send_request(
            path=uri, method='post', payload=payload)
        return result
