# phpipamsdk
PhpIpam Python REST API Client

No crypt API support, only HTTP/HTTPS with HTTPS recommended.

Example Configuration Class File:
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

from phpipamsdk.utils import get_subnet_id
from phpipamsdk.utils import get_section_id

def list_subnets(ipam=None, section_name=None):
    """ get and print out section subnets """
    sections_api = phpipamsdk.SectionsApi(phpipam=ipam)

    section_id = get_section_id(ipam=ipam, name=section_name)

    subnetlist = sections_api.list_section_subnets(section_id=section_id)

    if 'data' in subnetlist:
        for item in subnetlist['data']:
            print item['description'] + ": " + item['subnet'] + "/" + item['mask']

def add_first_free_subnet(
        ipam=None, section_name=None, master_subnet_cidr=None, mask=None):
    """ add first available subnet to parent subnet """
    subnets_api = phpipamsdk.SubnetsApi(phpipam=ipam)

    section_id = get_section_id(ipam=ipam, name=section_name)

    master_subnet_id = get_subnet_id(
        ipam=ipam, cidr=master_subnet_cidr, section_id=section_id)

    subnets_api.add_subnet_first_free(
        subnet_id=master_subnet_id,
        mask=mask)

if __name__ == "__main__":
    warnings.filterwarnings('ignore')
    IPAM = phpipamsdk.PhpIpamApi()
    IPAM.login()

    list_subnets(ipam=IPAM, section_name='Customers')
    add_first_free_subnet(
        ipam=IPAM, section_name='Customers',
        master_subnet_cidr="10.10.0.0/16", mask="24")
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
    list_subnets(ipam=IPAM, section_name='Customers')

    IPAM.logout()
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
**API autocreated: 10.10.0.0/24**
Customer 1: 10.10.1.0/24
Customer 2: 10.10.2.0/24
DHCP range: 10.65.22.0/24
```

---

Class PhpIpamApi

methods:  
login()  
login()  
get_token()  
refresh_token()  
logout()  

---

Class AddressesApi

methods:  
get_address()  
ping_address()  
get_address_from_subnet()  
search_address()  
search_hostname()  
get_address_first_free()  
list_address_custom_fields()  
list_address_tags()  
get_address_tag()  
list_addresses_tag()  
add_address()  
add_address_first_free()  
update_address()  
del_address()  
del_address_subnet()  


available parameters:  
id  
subnet_id  
ip  
is_gateway  
description  
hostname  
mac  
owner  
tag_id  
ptr_ignore  
ptr_id  
device_id  
port  
note  
exclude_ping  

---

Class L2DomainsApi()


methods:  
list_l2domains()  
get_l2domain()  
get_l2domain_vlans()  
list_l2domain_custom_fields()  
add_l2domain()  
update_l2domain()  
del_l2domain()  

available parameters:  
id  
name  
description  

---

Class PrefixesApi()

methods:  
list_prefixes_subnets()  
list_prefixes_subnets_version()  
list_prefixes_address()  
list_prefixes_address_version()  
get_prefixes_first_free_subnet()  
get_prefixes_first_free_address()  
add_prefixes_first_free_subnet()  
add_prefixes_first_free_address()  

available parameters:  
id  
subnet  
mask  
description  
section_id  
linked_subnet_id  
vlan_id  
vrf_id  
master_subnet_id  
nameserver_id  
show_name  
permissions  
dns_recursive  
dns_records  
allow_requests  
scan_agent_id  
ping_subnet  
discover_subnet  
is_folder  
is_full  
state_id  
threshold  
location_id  
subnet_id  
ip  
is_gateway  
mac  
owner  
tag_id  
ptr_ignore  
ptr_id  
device_id  
port  
note  
exclude_ping  

---

Class SectionsApi()

methods:  
list_sections()  
list_section_subnets()  
list_section_custom_fields()  
get_section()  
add_section()  
update_section()  
del_section()  

available parameters:  
id  
name  
description  
master_section_id  
permissions  
strict_mode  
subnet_ordering  
order  
show_vlan  
show_vrf  
show_supernet_only  
dns_id  

---

Class SubnetsApi()

methods:  
get_subnet()  
get_subnet_usage()  
list_subnet_slaves()  
list_subnet_slaves_recursive()  
list_subnet_addresses()  
get_subnet_address()  
get_subnet_first_free_address()  
get_subnet_first_free_subnet()  
list_subnet_free_subnets()  
list_subnet_custom_fields()  
list_subnets_cidr()  
search_subnets_cidr()  
add_subnet()  
add_subnet_first_free()  
update_subnet()  
resize_subnet()  
split_subnet()  
update_subnet_permissions()  
del_subnet()  
del_subnet_addresses()  
del_subnet_permissions()  


available parameters:
id  
subnet  
mask  
description  
section_id  
linked_subnet_id  
device_id  
vlan_id  
vrf_id  
master_subnet_id  
nameserver_id  
show_name  
permissions  
dns_recursive  
dns_records  
allow_requests  
scan_agent_id  
ping_subnet  
discover_subnet  
is_folder  
is_full  
state_id  
threshold  
location_id

---

Class ToolsDevicesApi()

methods:  
list_tools_devices()  
get_tools_device()  
add_tools_device()  
update_tools_device()  
del_tools_device()  

available parameters:  
id  
hostname  
ip_addr  
ip  
type_id  
vendor  
model  
sections  
location_id  
rack_id  
rack_size  
rack_start  
snmp_community  
snmp_port  
snmp_queries  
snmp_timeout  
snmp_version  
description  

---

Class ToolsDeviceTypesApi()

methods:  
list_tools_devicetypes()  
list_tools_devicetype_devices()  
get_tools_devicetype()  
add_tools_devicetype()  
update_tools_devicetype()  
del_tools_devicetype()  

available parameters:  
id  
name  
description  

---

Class ToolsLocationsApi()

methods:  
list_tools_locations()  
get_tools_location()  
list_tools_location_subnets()  
list_tools_location_devices()  
list_tools_location_racks()  
add_tools_location()  
update_tools_location()  
del_tools_location()  

available parameters:  
id  
name  
address  
lat  
long  
description  

---

Class ToolsNameserversApi()

methods:  
list_tools_nameservers()  
get_tools_nameserver()  
add_tools_nameserver()  
update_tools_nameserver()  
del_tools_nameserver()  

available parameters:  
id  
name  
namesrv1  
description  
permissions  

---

Class ToolsNATApi()

methods:  
list_tools_nats()  
get_tools_nat()  
list_tools_nat_objects()  
list_tools_nat_objects_full()  
add_tools_nat()  
update_tools_nat()  
del_tools_nat()  

available parameters:  
id  
name  
type  
device_id  
src  
src_port  
dst  
dst_port  
description

---

Class ToolsRacksApi()

methods:  
list_tools_racks()  
get_tools_rack()  
list_tools_rack_devices()  
add_tools_rack()  
update_tools_rack()  
del_tools_rack()  

available parameters:  
id  
name  
location_id  
size  
description

---

Class ToolsScanagentsApi()

methods:
list_tools_scanagents()  
get_tools_scanagent()  
add_tools_scanagent()  
update_tools_scanagent()  
del_tools_scanagent()  

available parameters:  
id  
name  
type  
description  
code  

---

Class ToolsTagsApi()

methods:  
list_tools_tags()  
get_tools_tag()  
add_tools_tag()  
update_tools_tag()  
del_tools_tag()  

available parameters:  
id  
type  
showtags  
bgcolor  
fgcolor  
compress

---

Class ToolsVlansApi()

methods:  
list_tools_vlans()  
get_tools_vlan()  
list_tools_vlan_subnets()  
add_tools_vlan()  
update_tools_vlan()  
del_vlan()  

available parameters:  
id  
domain_id  
name  
number  
description

---

Class ToolsVRFsApi()

methods:  
list_tools_vrfs()  
get_tools_vrf()  
list_tools_vrf_subnets()  
add_tools_vrf()  
update_tools_vrf()  
del_vrf()  

available parameters:  
id  
name  
rd  
description  
sections

---

Class VlansApi()

methods:  
list_vlans()  
get_vlan()  
list_vlan_subnets()  
list_vlan_subnets_section()  
list_vlan_custom_fields()  
search_vlans()  
add_vlan()  
update_vlan()  
del_vlan()  

available parameters:  
id  
domain_id  
name  
number  
description  

---

Class VRFsApi()

methods:  
list_vrfs()  
get_vrf()  
list_vrf_subnets()  
list_vrf_custom_fields()  
add_vrf()  
update_vrf()  
del_vrf()  

available parameters:  
id  
name  
rd  
description  
sections  

---

Utility Functions:

get_tools_location_id()  
get_tools_rack_id()  
get_tools_devicetype_id()  
get_tools_device_id()  
get_section_id()  
get_l2domain_id()  
get_vlan_id()  
get_subnet_id()  
get_vrf_id()  
get_tag_id()  
get_address_id()  
