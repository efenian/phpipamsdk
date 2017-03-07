""" Tools Nameservers Api Calls """

from ..phpipam import PhpIpamApi

class ToolsNameserversApi(object):
    """ Tools Tags Api Class """
    def __init__(self, phpipam=None):
        if phpipam:
            self.phpipam = phpipam
        else:
            self.phpipam = PhpIpamApi()
