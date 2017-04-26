""" Sections Api Calls """

from ..phpipam import PhpIpamApi
from ..phpipam import build_payload


class SectionsApi(object):
    """ Sections Api Class """

    _objmap = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'master_section_id': 'masterSection',
        'permissions': 'permissions',
        'strict_mode': 'strictMode',
        'subnet_ordering': 'subnetOrdering',
        'order': 'order',
        'show_vlan': 'showVLAN',
        'show_vrf': 'showVRF',
        'show_supernet_only': 'showSupernetOnly',
        'dns_id': 'DNS'
    }

    def __init__(self, phpipam=None):
        if phpipam:
            self.phpipam = phpipam
        else:
            self.phpipam = PhpIpamApi()

    def list_sections(self):
        """ get section list """
        uri = 'sections/'
        result = self.phpipam.api_send_request(path=uri, method='get')
        return result

    def list_section_subnets(self, section_id=''):
        """ get section subnet list """
        uri = 'sections/' + section_id + '/subnets/'
        result = self.phpipam.api_send_request(path=uri, method='get')
        return result

    def list_section_custom_fields(self):
        """ get custom fields list """
        uri = 'sections/custom_fields/'
        result = self.phpipam.api_send_request(path=uri, method='get')
        return result

    def get_section(self, section=''):
        """ get section by name or id """
        uri = 'sections/' + str(section) + '/'
        result = self.phpipam.api_send_request(path=uri, method='get')
        return result

    def add_section(self, name='', **kwargs):
        """ add new section """
        payload = {
            'name': name
        }
        payload.update(build_payload(self._objmap, **kwargs))
        uri = 'sections/'
        result = self.phpipam.api_send_request(
            path=uri, method='post', payload=payload)
        return result

    def update_section(self, section_id='', **kwargs):
        """ update section """
        payload = {}
        payload.update(build_payload(self._objmap, **kwargs))
        uri = 'sections/' + str(section_id) + '/'
        result = self.phpipam.api_send_request(
            path=uri, method='patch', payload=payload)
        return result

    def del_section(self, section_id=''):
        """ delete section """
        uri = 'sections/' + str(section_id) + '/'
        result = self.phpipam.api_send_request(path=uri, method='delete')
        return result
