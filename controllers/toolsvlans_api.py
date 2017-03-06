""" Tools Vlans Api Calls """

from ..phpipam import PhpIpamApi

class ToolsVlansApi(object):
    """ Tools Vlans Api Class """
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
