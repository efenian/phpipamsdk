""" Tools NAT Api Calls """

from ..phpipam import PhpIpamApi
from ..phpipam import build_payload


class ToolsNATApi(object):
    """ Tools NAT Api Class """

    _objmap = {
        'id': 'id',
        'name': 'name',
        'type': 'type',
        'device_id': 'device',
        'src': 'src',
        'src_port': 'src_port',
        'dst': 'dst',
        'dst_port': 'dst_port',
        'description': 'description'
    }

    def __init__(self, phpipam=None):
        if phpipam:
            self.phpipam = phpipam
        else:
            self.phpipam = PhpIpamApi()

    def list_tools_nats(self):
        """ get nat list """
        uri = 'tools/nat/'
        result = self.phpipam.api_send_request(path=uri, method='get')
        return result

    def get_tools_nat(self, nat_id=''):
        """ get nat list """
        uri = 'tools/nat/' + str(nat_id) + '/'
        result = self.phpipam.api_send_request(path=uri, method='get')
        return result

    def list_tools_nat_objects(self, nat_id=''):
        """ get nats device list """
        uri = 'tools/nat/' + str(nat_id) + '/objects/'
        result = self.phpipam.api_send_request(path=uri, method='get')
        return result

    def list_tools_nat_objects_full(self, nat_id=''):
        """ get nats device list """
        uri = 'tools/nat/' + str(nat_id) + '/objects_full/'
        result = self.phpipam.api_send_request(path=uri, method='get')
        return result

    def add_tools_nat(self, name='', **kwargs):
        """ add new nat """
        payload = {
            'name': name,
        }
        payload.update(build_payload(self._objmap, **kwargs))
        uri = 'tools/nat/'
        result = self.phpipam.api_send_request(
            path=uri, method='post', payload=payload)
        return result

    def update_tools_nat(self, nat_id='', **kwargs):
        """ update nat """
        payload = {}
        payload.update(build_payload(self._objmap, **kwargs))
        uri = 'tools/nat/' + str(nat_id) + '/'
        result = self.phpipam.api_send_request(
            path=uri, method='patch', payload=payload)
        return result

    def del_tools_nat(self, nat_id=''):
        """ get nat """
        uri = 'tools/nat/' + str(nat_id) + '/'
        result = self.phpipam.api_send_request(path=uri, method='delete')
        return result
