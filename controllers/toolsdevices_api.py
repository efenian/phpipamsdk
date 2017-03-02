""" Tools Devices Api Calls """

from ..phpipam import PhpIpamApi

class ToolsDevicesApi(object):
    """ Tools Devices Api Class """
    def __init__(self, phpipam=None):
        if phpipam:
            self.phpipam = phpipam
        else:
            self.phpipam = PhpIpamApi()


    def list_devices(self):
        """ get device list """
        uri = 'tools/devices/'
        result = self.phpipam.api_send_request(path=uri, method='get')
        return result


    def add_device(self, hostname='', ip_addr='', devicetype='', **kwargs):
        """ add new device """
        payload = {
            'hostname' : hostname,
            'ip_addr' : ip_addr,
            'type' : devicetype
        }
        if 'vendor' in kwargs:
            payload['vendor'] = kwargs['vendor']
        if 'model' in kwargs:
            payload['model'] = kwargs['model']
        if 'sections' in kwargs:
            payload['sections'] = kwargs['sections']
        if 'description' in kwargs:
            payload['description'] = kwargs['description']
        uri = 'tools/devices/'
        result = self.phpipam.api_send_request(
            path=uri, method='post', payload=payload)
        return result


    def del_device(self, device_id=''):
        """ delete device """
        uri = 'tools/devices/' + str(device_id) + '/'
        result = self.phpipam.api_send_request(path=uri, method='delete')
        return result
