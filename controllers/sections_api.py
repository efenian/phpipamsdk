""" Sections Api Calls """

from ..phpipam import PhpIpamApi

class SectionsApi(object):
    """ Sections Api Class """
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


    def add_section(self, name='', permissions='', **kwargs):
        """ add new section """
        payload = {
            'name' : name,
            'permissions': permissions
        }
        if 'description' in kwargs:
            payload['description'] = kwargs['description']
        if 'master_section' in kwargs:
            if 'master_section' != '0':
                payload['masterSection'] = kwargs['master_section']
        if 'vlan' in kwargs:
            payload['showVLAN'] = kwargs['vlan']
        if 'vrf' in kwargs:
            payload['showVRF'] = kwargs['vrf']
        if 'strict_mode' in kwargs:
            payload['strictMode'] = kwargs['strict_mode']
        if 'ordering' in kwargs:
            payload['subnetOrdering'] = kwargs['ordering']
        uri = 'sections/'
        result = self.phpipam.api_send_request(
            path=uri, method='post', payload=payload)
        return result


    def del_section(self, section_id=''):
        """ delete section """
        uri = 'sections/' + str(section_id) + '/'
        result = self.phpipam.api_send_request(path=uri, method='delete')
        return result
