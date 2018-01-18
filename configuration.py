""" configuration class """


class Configuration(object):
    """ class used to store configuration """
    def __init__(self):
        """ constructor """
        self.api_uri = ''
        self.api_username = ''
        self.api_password = ''
        self.api_verify_ssl = ''
