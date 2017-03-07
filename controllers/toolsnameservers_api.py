""" Tools Nameservers Api Calls """

from ..phpipam import PhpIpamApi

class ToolsNameserversApi(object):
    """ Tools Tags Api Class """
    def __init__(self, phpipam=None):
        if phpipam:
            self.phpipam = phpipam
        else:
            self.phpipam = PhpIpamApi()


    def list_tools_nameservers(self):
         """ get nameserver list """
        uri = 'tools/nameservers/'
        result = self.phpipam.api_send_request(path=uri, method='get')
        return result
