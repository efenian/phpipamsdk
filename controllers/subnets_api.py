""" Subnets Api Calls """

from ..phpipam import PhpIpamApi
from ..phpipam import build_payload


class SubnetsApi(object):
    """ Subnets Api Class """

    _objmap = {
        'id': 'id',
        'subnet': 'subnet',
        'mask': 'mask',
        'description': 'description',
        'section_id': 'sectionId',
        'linked_subnet_id': 'linked_subnet',
        'device_id': 'deviceId',
        'vlan_id': 'vlanId',
        'vrf_id': 'vrfId',
        'master_subnet_id': 'masterSubnetId',
        'nameserver_id': 'nameserverId',
        'show_name': 'showName',
        'permissions': 'permissions',
        'dns_recursive': 'DNSrecursive',
        'dns_records': 'DNSrecords',
        'allow_requests': 'allowRequests',
        'scan_agent_id': 'scanAgent',
        'ping_subnet': 'pingSubnet',
        'discover_subnet': 'discoverSubnet',
        'is_folder': 'isFolder',
        'is_full': 'isFull',
        'state_id': 'state',
        'threshold': 'threshold',
        'location_id': 'location'
    }

    def __init__(self, phpipam=None):
        if phpipam:
            self.phpipam = phpipam
        else:
            self.phpipam = PhpIpamApi()

    def get_subnet(self, subnet_id=''):
        """ get subnet details based on ID """
        uri = 'subnets/' + str(subnet_id) + '/'
        result = self.phpipam.api_send_request(path=uri, method='get')
        return result

    def get_subnet_usage(self, subnet_id=''):
        """ get subnet usage details based on ID """
        uri = 'subnets/' + str(subnet_id) + '/usage/'
        result = self.phpipam.api_send_request(path=uri, method='get')
        return result

    def list_subnet_slaves(self, subnet_id=''):
        """ get subnet slave details based on ID """
        uri = 'subnets/' + str(subnet_id) + '/slaves/'
        result = self.phpipam.api_send_request(path=uri, method='get')
        return result

    def list_subnet_slaves_recursive(self, subnet_id=''):
        """ get subnet recursive salves details based on ID """
        uri = 'subnets/' + str(subnet_id) + '/slaves_recursive/'
        result = self.phpipam.api_send_request(path=uri, method='get')
        return result

    def list_subnet_addresses(self, subnet_id=''):
        """ get list of addresses in subnet """
        uri = 'subnets/' + str(subnet_id) + '/addresses/'
        result = self.phpipam.api_send_request(path=uri, method='get')
        return result

    def get_subnet_address(self, subnet_id='', address=''):
        """ get list of addresses in subnet """
        uri = 'subnets/' + str(subnet_id) + '/addresses/' + str(address) + '/'
        result = self.phpipam.api_send_request(path=uri, method='get')
        return result

    def get_subnet_first_free_address(self, subnet_id=''):
        """ get first available addresss in subnet """
        uri = 'subnets/' + str(subnet_id) + '/first_free/'
        result = self.phpipam.api_send_request(path=uri, method='get')
        return result

    def get_subnet_first_free_subnet(self, subnet_id='', mask=''):
        """ get first available subnet in parent subnet """
        uri = 'subnets/' + str(subnet_id) + '/first_subnet/' + str(mask) + '/'
        result = self.phpipam.api_send_request(path=uri, method='get')
        return result

    def list_subnet_free_subnets(self, subnet_id='', mask=''):
        """ list available subnet in parent subnet """
        uri = 'subnets/' + str(subnet_id) + '/all_subnets/' + str(mask) + '/'
        result = self.phpipam.api_send_request(path=uri, method='get')
        return result

    def list_subnet_custom_fields(self):
        """ list subnet custom fields """
        uri = 'subnets/custom_fields/'
        result = self.phpipam.api_send_request(path=uri, method='get')
        return result

    def list_subnets_cidr(self, subnet_cidr=''):
        """ lists subnets based on CIDR notation """
        uri = 'subnets/cidr/' + subnet_cidr + '/'
        result = self.phpipam.api_send_request(path=uri, method='get')
        return result

    def search_subnets_cidr(self, subnet_cidr=''):
        """ searches for subnets based on CIDR notation """
        uri = 'subnets/search/' + subnet_cidr + '/'
        result = self.phpipam.api_send_request(path=uri, method='get')
        return result

    def add_subnet(self, subnet='', mask='', **kwargs):
        """ add new subnet """
        payload = {
            'subnet': subnet,
            'mask': mask
        }
        payload.update(build_payload(self._objmap, **kwargs))
        uri = 'subnets/'
        result = self.phpipam.api_send_request(
            path=uri, method='post', payload=payload)
        return result

    def add_subnet_first_free(self, subnet_id='', mask='', **kwargs):
        """ add first free subnet under parent subnet """
        payload = {}
        payload.update(build_payload(self._objmap, **kwargs))
        uri = 'subnets/' + str(subnet_id) + '/first_subnet/' + str(mask) + '/'
        result = self.phpipam.api_send_request(
            path=uri, method='post', payload=payload)
        return result

    def update_subnet(self, subnet_id='', **kwargs):
        """ update subnet """
        payload = {}
        payload.update(build_payload(self._objmap, **kwargs))
        uri = 'subnets/' + str(subnet_id) + '/'
        result = self.phpipam.api_send_request(
            path=uri, method='patch', payload=payload)
        return result

    def resize_subnet(self, subnet_id='', mask=''):
        """ update subnet """
        payload = {
            'mask': mask
        }
        uri = 'subnets/' + str(subnet_id) + '/resize/'
        result = self.phpipam.api_send_request(
            path=uri, method='patch', payload=payload)
        return result

    def split_subnet(self, subnet_id='', mask=''):
        """ update subnet """
        payload = {
            'mask': mask
        }
        uri = 'subnets/' + str(subnet_id) + '/split/'
        result = self.phpipam.api_send_request(
            path=uri, method='patch', payload=payload)
        return result

    def update_subnet_permissions(self, subnet_id='', permissions=''):
        """ update subnet """
        payload = {
            'permissions': permissions
        }
        uri = 'subnets/' + str(subnet_id) + '/permissions/'
        result = self.phpipam.api_send_request(
            path=uri, method='patch', payload=payload)
        return result

    def del_subnet(self, subnet_id=''):
        """ delete subnet """
        uri = 'subnets/' + str(subnet_id) + '/'
        result = self.phpipam.api_send_request(path=uri, method='delete')
        return result

    def del_subnet_addresses(self, subnet_id=''):
        """ delete subnet addresses """
        uri = 'subnets/' + str(subnet_id) + '/truncate/'
        result = self.phpipam.api_send_request(path=uri, method='delete')
        return result

    def del_subnet_permissions(self, subnet_id=''):
        """ delete subnet permissions """
        uri = 'subnets/' + str(subnet_id) + '/permissions/'
        result = self.phpipam.api_send_request(path=uri, method='delete')
        return result
