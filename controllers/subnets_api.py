""" Subnets Api Calls """

from ..phpipam import PhpIpamApi

class SubnetsApi(object):
    """ Subnets Api Class """
    def __init__(self, phpipam=None):
        if phpipam:
            self.phpipam = phpipam
        else:
            self.phpipam = PhpIpamApi()