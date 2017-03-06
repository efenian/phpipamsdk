""" Tools Tags Api Calls """

from ..phpipam import PhpIpamApi

class ToolsTagsApi(object):
    """ Tools Tags Api Class """
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
            'type' : name
        }
        if 'showtags' in kwargs:
            payload['showtags'] = kwargs['showtags']
        if 'bgcolor' in kwargs:
            payload['bgcolor'] = kwargs['bgcolor']
        if 'fgcolor' in kwargs:
            payload['fgcolor'] = kwargs['fgcolor']
        if 'compress' in kwargs:
            payload['compress'] = kwargs['compress']
        uri = 'tools/tags/'
        result = self.phpipam.api_send_request(
            path=uri, method='post', payload=payload)
        return result


    def update_tools_tag(self, tag_id='', **kwargs):
        """ update tag """
        payload = {}
        if 'name' in kwargs:
            payload['type'] = kwargs['name']
        if 'showtags' in kwargs:
            payload['showtags'] = kwargs['showtags']
        if 'bgcolor' in kwargs:
            payload['bgcolor'] = kwargs['bgcolor']
        if 'fgcolor' in kwargs:
            payload['fgcolor'] = kwargs['fgcolor']
        if 'compress' in kwargs:
            payload['compress'] = kwargs['compress']
        uri = 'tools/tags/' + str(tag_id) + '/'
        result = self.phpipam.api_send_request(
            path=uri, method='patch', payload=payload)
        return result


    def del_tools_tag(self, tag_id=''):
        """ delete tag """
        uri = 'tools/tags/' + str(tag_id) + '/'
        result = self.phpipam.api_send_request(path=uri, method='delete')
        return result
