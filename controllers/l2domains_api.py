""" L2Domains Api Calls """

from ..phpipam import PhpIpamApi

class L2DomainsApi(object):
    """ L2Domains Api Class """
    def __init__(self, phpipam=None):
        if phpipam:
            self.phpipam = phpipam
        else:
            self.phpipam = PhpIpamApi()


    def list_l2domains(self):
        """ get l2domain list """
        uri = 'l2domains/'
        result = self.phpipam.api_send_request(path=uri, method='get')
        return result


    def add_l2domain(self, name='', **kwargs):
        """ add new l2domain """
        payload = {
            'name' : name
        }
        if 'description' in kwargs:
            payload['description'] = kwargs['description']
        uri = 'l2domains/'
        result = self.phpipam.api_send_request(
            path=uri, method='post', payload=payload)
        return result


    def del_l2domain(self, l2domain_id=''):
        """ delete l2domain """
        uri = 'l2domains/' + str(l2domain_id) + '/'
        result = self.phpipam.api_send_request(path=uri, method='delete')
        return result


    