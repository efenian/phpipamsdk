""" Eric Donohue's PhpIPAM SDK """

import json
import requests


def build_payload(objmap=None, **kwargs):
    """ build the REST payload """
    payload = {}
    for key, val in kwargs.items():
        if key in objmap:
            payload[objmap[key]] = val
    return payload


class PhpIpamException(Exception):
    """ phpipam generic exception class """
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)


class PhpIpamApi(object):
    """ phpipam REST API class """

    _api_uri = ''
    _api_token = ''
    _api_verify_ssl = False
    _api_headers = {
        'accept': 'application/json',
        'content-type' : 'application/json'
    }

    def __init__(self, api_uri='', api_verify_ssl=True):
        self._api_uri = api_uri
        self._api_verify_ssl = api_verify_ssl


    def api_send_request(self, path='', method='', auth='', payload=''):
        """ send HTTP REST request """
        verify = self._api_verify_ssl
        if method == 'post' or method == 'patch':
            temp = json.dumps(payload)
            payload = temp
        try:
            response = requests.request(
                method=method,
                url=self._api_uri + path,
                auth=auth,
                headers=self._api_headers,
                data=payload,
                verify=verify)
        except requests.exceptions.RequestException as exception:
            raise PhpIpamException(exception)
        else:
            status_code = response.status_code
            if status_code == 200:
                return json.loads(response.text)
            elif status_code == 201:
                result = json.loads(response.text)
                result['location'] = response.headers['Location']
                if 'id' not in result:
                    result['id'] = response.headers['Location'].split('/')[-2]
                return result
            else:
                raise PhpIpamException(response.text)


    def login(self, auth=''):
        """ authenticate to API """
        result = self.api_send_request(path='user/', auth=auth, method='post')
        self._api_token = result['data']['token']
        self._api_headers['phpipam-token'] = self._api_token


    def get_token(self):
        """ reset auth token """
        uri = 'user/'
        self.api_send_request(path=uri, method='get')


    def refresh_token(self):
        """ reset auth token """
        uri = 'user/'
        self.api_send_request(path=uri, method='patch')


    def logout(self):
        """ delete session """
        uri = 'user/'
        self.api_send_request(path=uri, method='delete')
