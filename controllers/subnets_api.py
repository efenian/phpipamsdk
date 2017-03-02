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

    def del_subnet(self, subnet_id=''):
        """ delete subnet """
        uri = 'subnets/' + str(subnet_id) + '/'
        result = self.phpipam.api_send_request(path=uri, method='delete')
        return result


    def list_subnets_cidr(self, subnet_cidr=''):
        """ lists subnets based on CIDR notation """
        uri = 'subnets/cidr/' + subnet_cidr
        result = self.phpipam.api_send_request(path=uri, method='get')
        return result


    def get_subnet_first_free_address(self, subnet_id=''):
        """ get first available addresss in subnet """
        uri = 'subnets/' + str(subnet_id) + '/first_free/'
        result = self.phpipam.api_send_request(path=uri, method='get')
        return result
