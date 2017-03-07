""" Tools VRFs Api Calls """

from ..phpipam import PhpIpamApi

class ToolsVRFsApi(object):
    """ Tools VRFs Api Class """
    def __init__(self, phpipam=None):
        if phpipam:
            self.phpipam = phpipam
        else:
            self.phpipam = PhpIpamApi()


    def list_tools_vrfs(self):
        """ get vrf list """
        uri = 'tools/vrfs/'
        result = self.phpipam.api_send_request(path=uri, method='get')
        return result


    def get_tools_vrf(self, vrf_id=''):
        """ get vrf list """
        uri = 'tools/vrfs/' + str(vrf_id) +'/'
        result = self.phpipam.api_send_request(path=uri, method='get')
        return result


    def list_tools_vrf_subnets(self, vrf_id=''):
        """ get vrf subnet list """
        uri = 'tools/vrfs/' + str(vrf_id) + '/subnets/'
        result = self.phpipam.api_send_request(path=uri, method='get')
        return result


    def add_tools_vrf(self, name='', number='', **kwargs):
        """ add new tools vrf """
        payload = {
            'name' : name
        }
        if 'rd' in kwargs:
            payload['rd'] = kwargs['rd']
        if 'sections' in kwargs:
            payload['sections'] = kwargs['sections']
        if 'description' in kwargs:
            payload['description'] = kwargs['description']
        uri = 'tools/vrfs/'
        result = self.phpipam.api_send_request(
            path=uri, method='post', payload=payload)
        return result


    def update_tools_vrf(self, vrf_id='', **kwargs):
        """ update tools vrf """
        payload = {}
        if 'name' in kwargs:
            payload['name'] = kwargs['name']
        if 'rd' in kwargs:
            payload['rd'] = kwargs['rd']
        if 'sections' in kwargs:
            payload['sections'] = kwargs['sections']
        if 'description' in kwargs:
            payload['description'] = kwargs['description']
        uri = 'tools/vrfs/' + str(vrf_id) + '/'
        result = self.phpipam.api_send_request(
            path=uri, method='patch', payload=payload)
        return result


    def del_vrf(self, vrf_id=''):
        """ delete tools vrf """
        uri = 'tools/vrfs/' + str(vrf_id) + '/'
        result = self.phpipam.api_send_request(path=uri, method='delete')
        return result
