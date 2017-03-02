""" Vlans Api Calls """

from ..phpipam import PhpIpamApi

class VlansApi(object):
    """ Vlans Api Class """
    def __init__(self, phpipam=None):
        if phpipam:
            self.phpipam = phpipam
        else:
            self.phpipam = PhpIpamApi()


    def add_vlan(self, name='', number='', **kwargs):
        """ add new vlan """
        payload = {
            'name' : name,
            'number': str(number)
        }
        if 'description' in kwargs:
            payload['description'] = kwargs['description']
        if 'domain_id' in kwargs:
            payload['domainId'] = str(kwargs['domain_id'])
        uri = 'vlans/'
        result = self.phpipam.api_send_request(
            path=uri, method='post', payload=payload)
        return result


    def del_vlan(self, vlan_id=''):
        """ delete vlan """
        uri = 'vlans/' + str(vlan_id) + '/'
        result = self.phpipam.api_send_request(path=uri, method='delete')
        return result
