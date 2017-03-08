""" Tools Vlans Api Calls """

from ..phpipam import PhpIpamApi
from ..phpipam import build_payload

class ToolsVlansApi(object):
    """ Tools Vlans Api Class """

    _objmap = {
        'id' : 'id',
        'domain_id' : 'domainId',
        'name' : 'name',
        'number' : 'number',
        'description' : 'description'
    }

    def __init__(self, phpipam=None):
        if phpipam:
            self.phpipam = phpipam
        else:
            self.phpipam = PhpIpamApi()


    def list_tools_vlans(self):
        """ get vlan list """
        uri = 'tools/vlans/'
        result = self.phpipam.api_send_request(path=uri, method='get')
        return result


    def get_tools_vlan(self, vlan_id=''):
        """ get vlan list """
        uri = 'tools/vlans/' + str(vlan_id) +'/'
        result = self.phpipam.api_send_request(path=uri, method='get')
        return result


    def list_tools_vlan_subnets(self, vlan_id=''):
        """ get vlan subnet list """
        uri = 'tools/vlans/' + str(vlan_id) + '/subnets/'
        result = self.phpipam.api_send_request(path=uri, method='get')
        return result


    def add_tools_vlan(self, name='', number='', **kwargs):
        """ add new tools vlan """
        payload = {
            'name' : name,
            'number': str(number)
        }
        payload.update(build_payload(self._objmap, **kwargs))
        uri = 'tools/vlans/'
        result = self.phpipam.api_send_request(
            path=uri, method='post', payload=payload)
        return result


    def update_tools_vlan(self, vlan_id='', **kwargs):
        """ update tools vlan """
        payload = {}
        payload.update(build_payload(self._objmap, **kwargs))
        uri = 'tools/vlans/' + str(vlan_id) + '/'
        result = self.phpipam.api_send_request(
            path=uri, method='patch', payload=payload)
        return result


    def del_vlan(self, vlan_id=''):
        """ delete tools vlan """
        uri = 'tools/vlans/' + str(vlan_id) + '/'
        result = self.phpipam.api_send_request(path=uri, method='delete')
        return result
