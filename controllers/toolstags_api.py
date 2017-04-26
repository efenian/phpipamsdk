""" Tools Tags Api Calls """

from ..phpipam import PhpIpamApi
from ..phpipam import build_payload


class ToolsTagsApi(object):
    """ Tools Tags Api Class """

    _objmap = {
        'id': 'id',
        'type': 'type',
        'showtags': 'showtags',
        'bgcolor': 'bgcolor',
        'fgcolor': 'fgcolor',
        'compress': 'compress'
    }

    def __init__(self, phpipam=None):
        if phpipam:
            self.phpipam = phpipam
        else:
            self.phpipam = PhpIpamApi()

    def list_tools_tags(self):
        """ get tag list """
        uri = 'tools/tags/'
        result = self.phpipam.api_send_request(path=uri, method='get')
        return result

    def get_tools_tag(self, tag_id=''):
        """ get tag """
        uri = 'tools/tags/' + str(tag_id) + '/'
        result = self.phpipam.api_send_request(path=uri, method='get')
        return result

    def add_tools_tag(self, name='', **kwargs):
        """ add tag """
        payload = {
            'type': name
        }
        payload.update(build_payload(self._objmap, **kwargs))
        uri = 'tools/tags/'
        result = self.phpipam.api_send_request(
            path=uri, method='post', payload=payload)
        return result

    def update_tools_tag(self, tag_id='', **kwargs):
        """ update tag """
        payload = {}
        payload.update(build_payload(self._objmap, **kwargs))
        uri = 'tools/tags/' + str(tag_id) + '/'
        result = self.phpipam.api_send_request(
            path=uri, method='patch', payload=payload)
        return result

    def del_tools_tag(self, tag_id=''):
        """ delete tag """
        uri = 'tools/tags/' + str(tag_id) + '/'
        result = self.phpipam.api_send_request(path=uri, method='delete')
        return result
