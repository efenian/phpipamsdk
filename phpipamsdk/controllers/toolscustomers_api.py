""" Tools Customers Api Calls """

from phpipamsdk.phpipam import PhpIpamApi, build_payload


class ToolsCustomersApi(object):
    """ Tools Customers Api Class """

    _objmap = {
        'id': 'id',
        'title': 'title',
        'address': 'address',
        'postcode': 'postcode',
        'city': 'city',
        'tag': 'tag',
        'lat': 'lat',
        'long': 'long',
        'contact_person': 'contact_person',
        'contact_phone': 'contact_phone',
        'contact_mail': 'contact_mail',
        'note': 'note',
        'status': 'status'
    }

    def __init__(self, phpipam=None):
        if phpipam:
            self.phpipam = phpipam
        else:
            self.phpipam = PhpIpamApi()

    def list_tools_customers(self):
        """ get customers list """
        uri = 'tools/customers/'
        result = self.phpipam.api_send_request(path=uri, method='get')
        return result

    def get_tools_customer(self, customer_id=''):
        """ get customer """
        uri = 'tools/customers/' + str(customer_id) + '/'
        result = self.phpipam.api_send_request(path=uri, method='get')
        return result

    def add_tools_customer(self, title='', **kwargs):
        """ add new customer """
        payload = {
            'title': title,
        }
        payload.update(build_payload(self._objmap, **kwargs))
        uri = 'tools/customers/'
        result = self.phpipam.api_send_request(
            path=uri, method='post', payload=payload)
        return result

    def update_tools_customer(self, customer_id='', **kwargs):
        """ update customer """
        payload = {}
        payload.update(build_payload(self._objmap, **kwargs))
        uri = 'tools/customers/' + str(customer_id) + '/'
        result = self.phpipam.api_send_request(
            path=uri, method='patch', payload=payload)
        return result

    def del_tools_customer(self, customer_id=''):
        """ delete customer """
        uri = 'tools/customers/' + str(customer_id) + '/'
        result = self.phpipam.api_send_request(path=uri, method='delete')
        return result
