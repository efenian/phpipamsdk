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
        uri = 'vrf/'
        result = self.phpipam.api_send_request(path=uri, method='get')
        return result


    def get_vrf(self, vrf_id=''):
        """ get vrf """
        uri = 'vrf/' + str(vrf_id) + '/'
        result = self.phpipam.api_send_request(path=uri, method='get')
        return result


    def list_vrf_subnets(self, vrf_id=''):
        """ list vrfs subnets """
        uri = 'vrf/' + str(vrf_id) + '/subnets/'
        result = self.phpipam.api_send_request(path=uri, method='get')
        return result


    def list_vrf_custom_fields(self):
        """ list vrfs custom fields """
        uri = 'vrf/custom_fields/'
        result = self.phpipam.api_send_request(path=uri, method='get')
        return result
    