""" Vlans Api Calls """

from ..phpipam import PhpIpamApi
from ..phpipam import build_payload

class VlansApi(object):
    """ Vlans Api Class """

    _objmap = {
        'id' : 'id',
        'domain_id' : 'domainId',
        'name' : 'name',
        'number' : 'number',
        'description' : 'description'
    }


    def __init__(self, phpipam=None):
        """ vlans constructor """
        if phpipam:
            self.phpipam = phpipam
        else:
            self.phpipam = PhpIpamApi()


    def list_vlans(self):
        """ list vlans """
        uri = 'vlans/'
        result = self.phpipam.api_send_request(path=uri, method='get')
        return result


    def get_vlan(self, vlan_id=''):
        """ list vlans """
        uri = 'vlans/' + str(vlan_id) + '/'
        result = self.phpipam.api_send_request(path=uri, method='get')
        return result


    def list_vlan_subnets(self, vlan_id=''):
        """ list vlan subnets """
        uri = 'vlans/' + str(vlan_id) + '/subnets/'
        result = self.phpipam.api_send_request(path=uri, method='get')
        return result


    def list_vlan_subnets_section(self, vlan_id='', section_id=''):
        """ list vlan subnets section """
        uri = 'vlans/' + str(vlan_id) + '/subnets/' + str(section_id) +'/'
        result = self.phpipam.api_send_request(path=uri, method='get')
        return result


    def list_vlan_custom_fields(self):
        """ list vlan custom fields """
        uri = 'vlans/custom_fields/'
        result = self.phpipam.api_send_request(path=uri, method='get')
        return result


    def search_vlans(self, vlan_id='', vlan=''):
        """ search vlans """
        uri = 'vlans/' + str(vlan_id) + '/search/' + str(vlan) + '/'
        result = self.phpipam.api_send_request(path=uri, method='get')
        return result


    def add_vlan(self, name='', number='', **kwargs):
        """ add new vlan """
        payload = {
            'name' : name,
            'number': str(number)
        }
        payload.update(build_payload(self._objmap, **kwargs))
        uri = 'vlans/'
        result = self.phpipam.api_send_request(
            path=uri, method='post', payload=payload)
        return result


    def update_vlan(self, vlan_id='', **kwargs):
        """ update vlan """
        payload = {}
        payload.update(build_payload(self._objmap, **kwargs))
        uri = 'vlans/' + str(vlan_id) + '/'
        result = self.phpipam.api_send_request(
            path=uri, method='patch', payload=payload)
        return result


    def del_vlan(self, vlan_id=''):
        """ delete vlan """
        uri = 'vlans/' + str(vlan_id) + '/'
        result = self.phpipam.api_send_request(path=uri, method='delete')
        return result
