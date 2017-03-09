""" Tools Scanagents Api Calls """

from ..phpipam import PhpIpamApi
from ..phpipam import build_payload

class ToolsScanagentsApi(object):
    """ Tools Scanagents Api Class """

    _objmap = {
        'id' : 'id',
        'name' : 'name',
        'type' : 'type',
        'description' : 'description',
        'code' : 'code'
    }


    def __init__(self, phpipam=None):
        if phpipam:
            self.phpipam = phpipam
        else:
            self.phpipam = PhpIpamApi()


    def list_tools_scanagents(self):
        """ get scanagents list """
        uri = 'tools/scanagents/'
        result = self.phpipam.api_send_request(path=uri, method='get')
        return result


    def get_tools_scanagent(self, scanagent_id=''):
        """ get scanagent """
        uri = 'tools/scanagents/' + str(scanagent_id) + '/'
        result = self.phpipam.api_send_request(path=uri, method='get')
        return result


    def add_tools_scanagent(self, name='', **kwargs):
        """ add new scanagent """
        payload = {
            'name' : name,
        }
        payload.update(build_payload(self._objmap, **kwargs))
        uri = 'tools/scanagents/'
        result = self.phpipam.api_send_request(
            path=uri, method='post', payload=payload)
        return result


    def update_tools_scanagent(self, scanagent_id='', **kwargs):
        """ update scanagent """
        payload = {}
        payload.update(build_payload(self._objmap, **kwargs))
        uri = 'tools/scanagents/' + str(scanagent_id) + '/'
        result = self.phpipam.api_send_request(
            path=uri, method='patch', payload=payload)
        return result


    def del_tools_scanagent(self, scanagent_id=''):
        """ get scanagent """
        uri = 'tools/scanagents/' + str(scanagent_id) + '/'
        result = self.phpipam.api_send_request(path=uri, method='delete')
        return result
