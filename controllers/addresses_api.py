""" Addresses Api Calls """

from ..phpipam import PhpIpamApi

class AddressesApi(object):
    """ Addresses Api Class """
    def __init__(self, phpipam=None):
        if phpipam:
            self.phpipam = phpipam
        else:
            self.phpipam = PhpIpamApi()


    def add_address(self, subnet_id='', ip_addr='', tag_id='', **kwargs):
        """ add IP address """
        payload = {
            'subnetId' : str(subnet_id),
            'ip' : ip_addr,
            'tag' : tag_id
        }
        if 'hostname' in kwargs:
            payload['hostname'] = kwargs['hostname']
        if 'owner' in kwargs:
            payload['owner'] = kwargs['owner']
        if 'description' in kwargs:
            payload['description'] = kwargs['description']
        if 'note' in kwargs:
            payload['note'] = kwargs['note']
        if 'device_id' in kwargs:
            payload['deviceId'] = kwargs['device_id']
        if 'is_gateway' in kwargs:
            payload['is_gateway'] = kwargs['is_gateway']
        if 'mac' in kwargs:
            payload['mac'] = kwargs['mac']
        uri = 'addresses/'
        result = self.phpipam.api_send_request(
            path=uri, method='post', payload=payload)
        return result


    def del_address(self, address_id=''):
        """ delete IP address """
        uri = 'addresses/' + str(address_id) + '/'
        result = self.phpipam.api_send_request(path=uri, method='delete')
        return result
