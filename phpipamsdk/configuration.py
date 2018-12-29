""" configuration class """


class Configuration(object):
    """ class used to store configuration """
    def __init__(self):
        """ constructor """
        self.api_uri = ''
        self.api_username = ''
        self.api_password = ''
        # if using app code authentication instead of user/pass set app code
        self.api_appcode = ''
        self.api_verify_ssl = True
