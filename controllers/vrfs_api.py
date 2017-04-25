""" VRFs Api Calls """

from ..phpipam import PhpIpamApi
from ..phpipam import build_payload

class VRFsApi(object):
    """ VRFs Api Class """

    _objmap = {
        'id' : 'id',
        'name' : 'name',
        'rd' : 'rd',
        'description' : 'description',
        'sections' : 'sections'
    }

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


    def get_vrf(self, vrf_id=''):
        """ get vrf """
        uri = 'vrfs/' + str(vrf_id) + '/'
        result = self.phpipam.api_send_request(path=uri, method='get')
        return result


    def list_vrf_subnets(self, vrf_id=''):
        """ list vrfs subnets """
        uri = 'vrfs/' + str(vrf_id) + '/subnets/'
        result = self.phpipam.api_send_request(path=uri, method='get')
        return result


    def list_vrf_custom_fields(self):
        """ list vrfs custom fields """
        uri = 'vrfs/custom_fields/'
        result = self.phpipam.api_send_request(path=uri, method='get')
        return result


    def add_vrf(self, name='', **kwargs):
        """ add new vrf """
        payload = {
            'name' : name
        }
        payload.update(build_payload(self._objmap, **kwargs))
        uri = 'vrfs/'
        result = self.phpipam.api_send_request(
            path=uri, method='post', payload=payload)
        return result


    def update_vrf(self, vrf_id='', **kwargs):
        """ update vrf """
        payload = {}
        payload.update(build_payload(self._objmap, **kwargs))
        uri = 'vrfs/' + str(vrf_id) + '/'
        result = self.phpipam.api_send_request(
            path=uri, method='patch', payload=payload)
        return result


    def del_vrf(self, vrf_id=''):
        """ delete l2domain """
        uri = 'vrfs/' + str(vrf_id) + '/'
        result = self.phpipam.api_send_request(path=uri, method='delete')
        return result
