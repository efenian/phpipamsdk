""" Tools Device Types Api Calls """

from ..phpipam import PhpIpamApi

class ToolsDeviceTypesApi(object):
    """ Tools Devices Api Class """
    def __init__(self, phpipam=None):
        if phpipam:
            self.phpipam = phpipam
        else:
            self.phpipam = PhpIpamApi()


    def list_tools_devicetypes(self):
        """ get device type list """
        uri = 'tools/devicetypes/'
        result = self.phpipam.api_send_request(path=uri, method='get')
        return result


    def list_tools_devicetype_devices(self, devicetype_id=''):
        """ get device type devices """
        uri = 'tools/devicetypes/' + str(devicetype_id) + '/devices/'
        result = self.phpipam.api_send_request(path=uri, method='get')
        return result


    def get_tools_devicetype(self, devicetype_id=''):
        """ get device type """
        uri = 'tools/devicetypes/' + str(devicetype_id) + '/'
        result = self.phpipam.api_send_request(path=uri, method='get')
        return result


    def add_tools_devicetype(self, hostname='', **kwargs):
        """ add new devicetype """
        payload = {
            'hostname' : hostname,
        }
        if 'ip_addr' in kwargs:
            payload['ip_addr'] = kwargs['ip_addr']
        if 'type' in kwargs:
            payload['type'] = kwargs['type']
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


    def update_tools_devicetype(self, device_id='', **kwargs):
        """ add new device """
        payload = {}
        if 'hostname' in kwargs:
            payload['hostname'] = kwargs['hostname']
        if 'ip_addr' in kwargs:
            payload['ip_addr'] = kwargs['ip_addr']
        if 'type' in kwargs:
            payload['type'] = kwargs['type']
        if 'vendor' in kwargs:
            payload['vendor'] = kwargs['vendor']
        if 'model' in kwargs:
            payload['model'] = kwargs['model']
        if 'sections' in kwargs:
            payload['sections'] = kwargs['sections']
        if 'description' in kwargs:
            payload['description'] = kwargs['description']
        uri = 'tools/devices/' + str(device_id) + '/'
        result = self.phpipam.api_send_request(
            path=uri, method='post', payload=payload)
        return result


    def del_tools_devicetype(self, device_id=''):
        """ delete device """
        uri = 'tools/devices/' + str(device_id) + '/'
        result = self.phpipam.api_send_request(path=uri, method='delete')
        return result
        