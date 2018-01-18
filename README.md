# phpipamsdk
PhpIpam Python SDK

Example Configuration File:
```python
""" configuration class """


class Configuration(object):
    """ class used to store configuration """
    def __init__(self):
        """ constructor """
        self.api_uri = 'https://192.168.16.30/api/app/'
        self.api_username = 'admin'
        self.api_password = 'password'
        self.api_verify_ssl = False
```

Example Script:

```python
#!/usr/bin/env python
""" Example """

import warnings
import phpipamsdk

def check_list(t_list='', t_item='', t_string=''):
    """ function to check list length and raise appropriate exception """
    not_found = t_string.capitalize() + ' not found: ' + t_item
    ambiguous = 'Abiguous ' + t_string + ' match: ' + t_item
    if not t_list:
        raise ValueError(not_found)
    if t_list:
        raise ValueError(ambiguous)

def list_subnets(ipam=None, section_name=None):
    """ get and print out section subnets """
    sections_api = phpipamsdk.SectionsApi(phpipam=ipam)

    apiresult = sections_api.list_sections()
    sectionlist = apiresult['data'] if 'data' in apiresult else []
    sect = [x for x in sectionlist if x['name'] == section_name]

    check_list(t_list=sect, t_item=section_name, t_string='section name')

    section_id = sect[0]['id']

    subnetlist = sections_api.list_section_subnets(section_id=section_id)

    if 'data' in subnetlist:
        for item in subnetlist['data']:
            print item['description'] + ": " + item['subnet'] + "/" + item['mask']

def add_first_free_subnet(
        ipam=None, section_name=None, master_subnet_cidr=None, mask=None):
    """ add first available subnet to parent subnet """
    subnets_api = phpipamsdk.SubnetsApi(phpipam=ipam)

    sections_api = phpipamsdk.SectionsApi(phpipam=ipam)

    apiresult = sections_api.list_sections()
    sectionlist = apiresult['data'] if 'data' in apiresult else []
    sect = [x for x in sectionlist if x['name'] == section_name]

    check_list(t_list=sect, t_item=section_name, t_string='section name')

    section_id = sect[0]['id']

    apiresult = subnets_api.list_subnets_cidr(subnet_cidr=master_subnet_cidr)
    subnetlist = apiresult['data'] if 'data' in apiresult else []
```

Example Output:

```sh
 ./example.py
My folder: 0.0.0.0/
Business customers: 10.10.0.0/16
Customer 1: 10.10.1.0/24
Customer 2: 10.10.2.0/24
DHCP range: 10.65.22.0/24
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
My folder: 0.0.0.0/
Business customers: 10.10.0.0/16
API autocreated: 10.10.0.0/24
Customer 1: 10.10.1.0/24
Customer 2: 10.10.2.0/24
DHCP range: 10.65.22.0/24
```
