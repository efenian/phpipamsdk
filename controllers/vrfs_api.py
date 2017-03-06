""" VRFs Api Calls """

from ..phpipam import PhpIpamApi

class VRFsApi(object):
    """ VRFs Api Class """
    def __init__(self, phpipam=None):
        if phpipam:
            self.phpipam = phpipam
        else:
            self.phpipam = PhpIpamApi()


    def list_vrfs(self):
        """ list vrfs """
        uri = 'vrfs/'
        result = self.phpipam.api_send_request(path=uri, method='get')
        return result
        