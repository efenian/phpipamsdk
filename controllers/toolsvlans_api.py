""" Tools Vlans Api Calls """

from ..phpipam import PhpIpamApi

class ToolsVlansApi(object):
    """ Tools Vlans Api Class """
    def __init__(self, phpipam=None):
        if phpipam:
            self.phpipam = phpipam
        else:
            self.phpipam = PhpIpamApi()

    def list_vlans(self):
        """ get vlan list """
        uri = 'tools/vlans/'
        result = self.phpipam.api_send_request(path=uri, method='get')
        return result
