""" Circuits Api Calls """

from phpipamsdk.phpipam import PhpIpamApi, build_payload


class CircuitsApi(object):
    """ Circuits Api Class """

    _objmap = {
        'id': 'id',
        'circuit_id': 'circuit_id',
        'provider': 'provider',
        'type': 'type',
        'capacity': 'capacity',
        'status': 'status',
        'device1': 'device1',
        'location1': 'location1',
        'device2': 'device2',
        'location2': 'location2',
        'comment': 'comment',
        'name': 'name',
        'description': 'description',
        'contact': 'contact'
    }

    def __init__(self, phpipam=None):
        """ circuits constructor """
        if phpipam:
            self.phpipam = phpipam
        else:
            self.phpipam = PhpIpamApi()

    def list_circuits(self):
        """ list circuits """
        uri = 'circuits/'
        result = self.phpipam.api_send_request(path=uri, method='get')
        return result

    def get_circuit(self, cir_id=''):
        """ get circuit """
        uri = 'circuits/' + str(cir_id) + '/'
        result = self.phpipam.api_send_request(path=uri, method='get')
        return result

    def add_circuit(self, circuit_id=None, provider_id=None, **kwargs):
        """ add new circuit """
        payload = {
            'circuit_id': circuit_id,
            'provider': provider_id,
        }
        payload.update(build_payload(self._objmap, **kwargs))
        uri = 'circuits/'
        result = self.phpipam.api_send_request(
            path=uri, method='post', payload=payload)
        return result

    def update_circuit(self, cir_id=None, **kwargs):
        """ update circuit """
        payload = {}
        payload.update(build_payload(self._objmap, **kwargs))
        uri = 'circuits/' + str(cir_id) + '/'
        result = self.phpipam.api_send_request(
            path=uri, method='patch', payload=payload)
        return result

    def del_circuit(self, cir_id=None):
        """ delete circuit """
        uri = 'circuits/' + str(cir_id) + '/'
        result = self.phpipam.api_send_request(path=uri, method='delete')
        return result

    def list_providers(self):
        """ list providers """
        uri = 'circuits/providers/'
        result = self.phpipam.api_send_request(path=uri, method='get')
        return result

    def get_provider(self, provider_id=None):
        """ get provider """
        uri = 'circuits/providers/' + str(provider_id) + '/'
        result = self.phpipam.api_send_request(path=uri, method='get')
        return result

    def add_provider(self, name='', **kwargs):
        """ add new provider """
        payload = {
            'name': name,
        }
        payload.update(build_payload(self._objmap, **kwargs))
        uri = 'circuits/providers/'
        result = self.phpipam.api_send_request(
            path=uri, method='post', payload=payload)
        return result

    def update_provider(self, provider_id=None, **kwargs):
        """ update provider """
        payload = {}
        payload.update(build_payload(self._objmap, **kwargs))
        uri = 'circuits/providers/' + str(provider_id) + '/'
        result = self.phpipam.api_send_request(
            path=uri, method='patch', payload=payload)
        return result

    def del_provider(self, provider_id=None):
        """ delete provider """
        uri = 'circuits/providers/' + str(provider_id) + '/'
        result = self.phpipam.api_send_request(path=uri, method='delete')
        return result
