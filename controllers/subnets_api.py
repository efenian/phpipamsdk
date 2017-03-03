""" Subnets Api Calls """

from ..phpipam import PhpIpamApi

class SubnetsApi(object):
    """ Subnets Api Class """
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
        uri = 'subnets/' + str(subnet_id) + '/first_subnet/' + str(mask) +'/'
        result = self.phpipam.api_send_request(path=uri, method='get')
        return result


    def list_subnet_free_subnets(self, subnet_id='', mask=''):
        """ list available subnet in parent subnet """
        uri = 'subnets/' + str(subnet_id) + '/all_subnets/' + str(mask) +'/'
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


    def add_subnet(self, subnet='', mask='', section='',
                   permissions='', **kwargs):
        """ add new subnet """
        payload = {
            'subnet' : subnet,
            'mask': mask,
            'sectionId': section,
            'permissions': permissions
        }
        if 'description' in kwargs:
            payload['description'] = kwargs['description']
        if 'master_subnet' in kwargs:
            if 'master_subnet' != '0':
                payload['masterSubnetId'] = kwargs['master_subnet']
        if 'vlan' in kwargs:
            payload['vlanId'] = kwargs['vlan']
        if 'device' in kwargs:
            payload['device'] = kwargs['device']
        if 'show_name' in kwargs:
            payload['showName'] = kwargs['show_name']
        if 'ping_subnet' in kwargs:
            payload['pingSubnet'] = kwargs['ping_subnet']
        if 'discover_subnet' in kwargs:
            payload['discoverSubnet'] = kwargs['discover_subnet']
        if 'scan_agent' in kwargs:
            payload['scanAgent'] = kwargs['scan_agent']
        if 'full' in kwargs:
            payload['isFull'] = kwargs['full']
        uri = 'subnets/'
        result = self.phpipam.api_send_request(
            path=uri, method='post', payload=payload)
        return result


    def add_subnet_first_free_subnet(self, subnet_id='', mask='', **kwargs):
        """ add first free subnet under parent subnet """
        payload = {}
        if 'description' in kwargs:
            payload['description'] = kwargs['description']
        if 'master_subnet' in kwargs:
            if 'master_subnet' != '0':
                payload['masterSubnetId'] = kwargs['master_subnet']
        if 'vlan' in kwargs:
            payload['vlanId'] = kwargs['vlan']
        if 'device' in kwargs:
            payload['device'] = kwargs['device']
        if 'show_name' in kwargs:
            payload['showName'] = kwargs['show_name']
        if 'ping_subnet' in kwargs:
            payload['pingSubnet'] = kwargs['ping_subnet']
        if 'discover_subnet' in kwargs:
            payload['discoverSubnet'] = kwargs['discover_subnet']
        if 'scan_agent' in kwargs:
            payload['scanAgent'] = kwargs['scan_agent']
        if 'full' in kwargs:
            payload['isFull'] = kwargs['full']
        uri = 'subnets/' + str(subnet_id) + '/first_subnet/' + str(mask) +'/'
        result = self.phpipam.api_send_request(
            path=uri, method='post', payload=payload)
        return result


    def update_subnet(self, subnet_id='', **kwargs):
        """ update subnet """
        payload = {
            'subnetId' : subnet_id,
        }
        if 'permissions' in kwargs:
            payload['permissions'] = kwargs['permissions']
        if 'description' in kwargs:
            payload['description'] = kwargs['description']
        if 'master_subnet' in kwargs:
            if 'master_subnet' != '0':
                payload['masterSubnetId'] = kwargs['master_subnet']
        if 'vlan' in kwargs:
            payload['vlanId'] = kwargs['vlan']
        if 'device' in kwargs:
            payload['device'] = kwargs['device']
        if 'show_name' in kwargs:
            payload['showName'] = kwargs['show_name']
        if 'ping_subnet' in kwargs:
            payload['pingSubnet'] = kwargs['ping_subnet']
        if 'discover_subnet' in kwargs:
            payload['discoverSubnet'] = kwargs['discover_subnet']
        if 'scan_agent' in kwargs:
            payload['scanAgent'] = kwargs['scan_agent']
        if 'full' in kwargs:
            payload['isFull'] = kwargs['full']
        uri = 'subnets/'
        result = self.phpipam.api_send_request(
            path=uri, method='patch', payload=payload)
        return result


    def resize_subnet(self, subnet_id='', mask=''):
        """ update subnet """
        payload = {
            'mask' : mask
        }
        uri = 'subnets/' + str(subnet_id) + '/resize/'
        result = self.phpipam.api_send_request(
            path=uri, method='patch', payload=payload)
        return result


    def split_subnet(self, subnet_id='', mask=''):
        """ update subnet """
        payload = {
            'mask' : mask
        }
        uri = 'subnets/' + str(subnet_id) + '/split/'
        result = self.phpipam.api_send_request(
            path=uri, method='patch', payload=payload)
        return result

    def update_subnet_permissions(self, subnet_id='', permissions=''):
        """ update subnet """
        payload = {
            'permissions' : permissions
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
