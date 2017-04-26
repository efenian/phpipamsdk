""" L2Domains Api Calls """

from ..phpipam import PhpIpamApi
from ..phpipam import build_payload


class L2DomainsApi(object):
    """ L2Domains Api Class """

    _objmap = {
        'id': 'id',
        'name': 'name',
        'description': 'description'
    }

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

    def get_l2domain(self, domain_id=''):
        """ get l2domain """
        uri = 'l2domains/' + str(domain_id) + '/'
        result = self.phpipam.api_send_request(path=uri, method='get')
        return result

    def get_l2domain_vlans(self, domain_id=''):
        """ get l2domain vlans """
        uri = 'l2domains/' + str(domain_id) + '/vlans/'
        result = self.phpipam.api_send_request(path=uri, method='get')
        return result

    def list_l2domain_custom_fields(self):
        """ get l2domain custom fields """
        uri = 'l2domains/custom_fields/'
        result = self.phpipam.api_send_request(path=uri, method='get')
        return result

    def add_l2domain(self, name='', **kwargs):
        """ add new l2domain """
        payload = {
            'name': name
        }
        payload.update(build_payload(self._objmap, **kwargs))
        uri = 'l2domains/'
        result = self.phpipam.api_send_request(
            path=uri, method='post', payload=payload)
        return result

    def update_l2domain(self, domain_id='', **kwargs):
        """ update l2domain """
        payload = {}
        payload.update(build_payload(self._objmap, **kwargs))
        uri = 'l2domains/' + str(domain_id) + '/'
        result = self.phpipam.api_send_request(
            path=uri, method='patch', payload=payload)
        return result

    def del_l2domain(self, l2domain_id=''):
        """ delete l2domain """
        uri = 'l2domains/' + str(l2domain_id) + '/'
        result = self.phpipam.api_send_request(path=uri, method='delete')
        return result
