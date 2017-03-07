""" Tools Nameservers Api Calls """

from ..phpipam import PhpIpamApi

class ToolsNameserversApi(object):
    """ Tools Tags Api Class """

    _objmap = {
        'id' : 'id',
        'name' : 'name',
        'namesrv1' : 'namesrv1',
        'description' : 'description',
        'permissions' : 'permissions'
    }

    def __init__(self, phpipam=None):
        if phpipam:
            self.phpipam = phpipam
        else:
            self.phpipam = PhpIpamApi()


    def _build_payload(self, **kwargs):
        payload = {}
        for key, val in kwargs.items():
            if key in self._objmap:
                payload[self._objmap[key]] = val
        return payload

    def list_tools_nameservers(self):
        """ get nameserver list """
        uri = 'tools/nameservers/'
        result = self.phpipam.api_send_request(path=uri, method='get')
        return result

    def get_tools_nameserver(self, nameserver_id=''):
        """ get nameserver """
        uri = 'tools/nameservers/' + str(nameserver_id) + '/'
        result = self.phpipam.api_send_request(path=uri, method='get')
        return result

    def add_tools_nameserver(self, name='', **kwargs):
        """ add new devicetype """
        payload = {
            'name' : name,
        }
        payload.update(self._build_payload(**kwargs))
        uri = 'tools/nameservers/'
        result = self.phpipam.api_send_request(
            path=uri, method='post', payload=payload)
        return result
