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


    def add_vrf(self, name='', **kwargs):
        """ add new vrf """
        payload = {
            'name' : name
        }
        if 'rd' in kwargs:
            payload['rd'] = kwargs['rd']
        if 'sections' in kwargs:
            payload['sections'] = kwargs['sections']
        if 'description' in kwargs:
            payload['description'] = kwargs['description']
        uri = 'vrf/'
        result = self.phpipam.api_send_request(
            path=uri, method='post', payload=payload)
        return result


    def update_vrf(self, vrf_id='', **kwargs):
        """ update vrf """
        payload = {}
        if 'name' in kwargs:
            payload['name'] = kwargs['name']
        if 'rd' in kwargs:
            payload['rd'] = kwargs['rd']
        if 'sections' in kwargs:
            payload['sections'] = kwargs['sections']
        if 'description' in kwargs:
            payload['description'] = kwargs['description']
        uri = 'vrf/' + str(vrf_id) + '/'
        result = self.phpipam.api_send_request(
            path=uri, method='patch', payload=payload)
        return result


    def del_vrf(self, vrf_id=''):
        """ delete l2domain """
        uri = 'vrf/' + str(vrf_id) + '/'
        result = self.phpipam.api_send_request(path=uri, method='delete')
        return result
