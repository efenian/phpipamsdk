""" Tools Tags Api Calls """

from ..phpipam import PhpIpamApi

class ToolsTagsApi(object):
    """ Tools Tags Api Class """
    def __init__(self, phpipam=None):
        if phpipam:
            self.phpipam = phpipam
        else:
            self.phpipam = PhpIpamApi()


    def list_tags(self):
        """ get device list """
        uri = 'tools/tags/'
        result = self.phpipam.api_send_request(path=uri, method='get')
        return result
