""" Tools Tags Api Calls """

from ..phpipam import PhpIpamApi

class ToolsTagsApi(object):
    """ Tools Tags Api Class """
    def __init__(self, phpipam=None):
        if phpipam:
            self.phpipam = phpipam
        else:
            self.phpipam = PhpIpamApi()


    def list_tags(self):
        """ get tag list """
        uri = 'tools/tags/'
        result = self.phpipam.api_send_request(path=uri, method='get')
        return result


    def get_tag(self, tag_id=''):
        """ get tag """
        uri = 'tools/tags/' + str(tag_id) + '/'
        result = self.phpipam.api_send_request(path=uri, method='get')
        return result
