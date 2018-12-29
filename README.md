# phpipamsdk
PhpIpam Python REST API Client

No crypt API support, only HTTP/HTTPS with HTTPS recommended.

You can try my [vagrant](https://github.com/efenian/vagrant-phpipam) to get
an instance of phpipam up and running for testing with Virtualbox.

__Install:__  
git clone https://github.com/efenian/phpipamsdk.git  
cd phpipamsdk  
pip install .  
or  
python setup.py install --record files.txt  

__Uninstall:__  
pip uninstall phpipamsdk  

__Either use the configuration class or pass parameters to PhpIpamApi class constructor and login methods as shown in the scripts in the examples directory__

__Example Configuration Class File using app id of 'app':__
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

__Example Script (also some scripts in examples directory):__

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

__Example Output:__

<pre><code>./example.py
My folder: 0.0.0.0/
Business customers: 10.10.0.0/16
Customer 1: 10.10.1.0/24
Customer 2: 10.10.2.0/24
DHCP range: 10.65.22.0/24
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
My folder: 0.0.0.0/
Business customers: 10.10.0.0/16
<b>API autocreated: 10.10.0.0/24</b>
Customer 1: 10.10.1.0/24
Customer 2: 10.10.2.0/24
DHCP range: 10.65.22.0/24
</code></pre>

---

__Class PhpIpamApi__

__methods:__  
get_token()  
login()  
logout()  
refresh_token()  

---

__Class AddressesApi__

__methods:__  
add_address()  
add_address_first_free()  
del_address()  
del_address_subnet()  
get_address()  
get_address_first_free()  
get_address_from_subnet()  
get_address_tag()  
list_address_custom_fields()  
list_address_tags()  
list_addresses_tag()  
ping_address()  
search_address()  
search_address_linked()  
search_address_mac()  
search_hostname()  
update_address()  


__available parameters:__  
description  
device_id  
exclude_ping  
firewall_address_object  
hostname  
id  
ip  
is_gateway  
location_id  
mac  
note  
owner  
port  
ptr_id  
ptr_ignore  
subnet_id  
tag_id  

---

__Class CircuitsApi__

__methods:__  
add_circuit()  
add_provider()  
del_circuit()  
del_provider()  
get_circuit()  
get_provider()  
list_circuits()  
list_providers()  
update_circuit()  
update_provider()  


__available parameters:__  
capacity  
circuit_id  
comment  
contact  
description  
device1  
device2  
id  
location1  
location2  
name  
provider  
status  
type  

---

__Class DevicesApi__

__methods:__  
add_device()  
del_device()  
get_device()  
get_device_addresses()  
get_device_subnets()  
list_devices()  
search_device()  
update_device()  


__available parameters:__  
description  
hostname  
id  
ip  
ip_addr  
location_id  
model  
rack_id  
rack_size  
rack_start  
sections  
snmp_community  
snmp_port  
snmp_queries  
snmp_timeout  
snmp_v3_auth_pass  
snmp_v3_auth_protocol  
snmp_v3_ctx_engine_id  
snmp_v3_ctx_name  
snmp_v3_priv_pass  
snmp_v3_priv_protocol  
snmp_version  
type_id  
vendor  

---

__Class L2DomainsApi__

__methods:__  
add_l2domain()  
del_l2domain()  
get_l2domain()  
get_l2domain_vlans()  
list_l2domain_custom_fields()  
list_l2domains()  
update_l2domain()  


__available parameters:__  
description  
id  
name  
sections  

---

__Class PrefixesApi__

__methods:__  
add_prefixes_first_free_address()  
add_prefixes_first_free_subnet()  
get_prefixes_first_free_address()  
get_prefixes_first_free_subnet()  
list_prefixes_address()  
list_prefixes_address_version()  
list_prefixes_subnets()  
list_prefixes_subnets_version()  


__available parameters:__  
allow_requests  
description  
device_id  
discover_subnet  
dns_records  
dns_recursive  
exclude_ping  
id  
ip  
is_folder  
is_full  
is_gateway  
linked_subnet_id  
location_id  
mac  
mask  
master_subnet_id  
nameserver_id  
note  
owner  
permissions  
ping_subnet  
port  
ptr_id  
ptr_ignore  
scan_agent_id  
section_id  
show_name  
state_id  
subnet  
subnet_id  
tag_id  
threshold  
vlan_id  
vrf_id  

---

__Class SectionsApi__

__methods:__  
add_section()  
del_section()  
get_section()  
list_section_custom_fields()  
list_section_subnets()  
list_sections()  
update_section()  


__available parameters:__  
description  
dns_id  
id  
master_section_id  
name  
order  
permissions  
show_supernet_only  
show_vlan  
show_vrf  
strict_mode  
subnet_ordering  

---

__Class SubnetsApi__

__methods:__  
add_subnet()  
add_subnet_first_free()  
add_subnet_last_free()  
del_subnet()  
del_subnet_addresses()  
del_subnet_permissions()  
get_subnet()  
get_subnet_address()  
get_subnet_first_free_address()  
get_subnet_first_free_subnet()  
get_subnet_last_free_subnet()  
get_subnet_usage()  
list_subnet_addresses()  
list_subnet_custom_fields()  
list_subnet_free_subnets()  
list_subnet_slaves()  
list_subnet_slaves_recursive()  
list_subnets_cidr()  
resize_subnet()  
search_subnets_cidr()  
split_subnet()  
update_subnet()  
update_subnet_permissions()  


__available parameters:__  
allow_requests  
description  
device_id  
discover_subnet  
dns_records  
dns_recursive  
firewall_address_object  
id  
is_folder  
is_full  
linked_subnet_id  
location_id  
mask  
master_subnet_id  
nameserver_id  
permissions  
ping_subnet  
resolve_dns  
scan_agent_id  
section_id  
show_name  
state_id  
subnet  
tag_id  
threshold  
vlan_id  
vrf_id  

---

__Class ToolsDeviceTypesApi__

__methods:__  
add_tools_devicetype()  
del_tools_devicetype()  
get_tools_devicetype()  
list_tools_devicetype_devices()  
list_tools_devicetypes()  
update_tools_devicetype()  


__available parameters:__  
description  
id  
name  

---

__Class ToolsDevicesApi__

__methods:__  
add_tools_device()  
del_tools_device()  
get_tools_device()  
list_tools_devices()  
update_tools_device()  


__available parameters:__  
description  
hostname  
id  
ip  
ip_addr  
location_id  
model  
rack_id  
rack_size  
rack_start  
sections  
snmp_community  
snmp_port  
snmp_queries  
snmp_timeout  
snmp_v3_auth_pass  
snmp_v3_auth_protocol  
snmp_v3_ctx_engine_id  
snmp_v3_ctx_name  
snmp_v3_priv_pass  
snmp_v3_priv_protocol  
snmp_version  
type_id  
vendor  

---

__Class ToolsLocationsApi__

__methods:__  
add_tools_location()  
del_tools_location()  
get_tools_location()  
list_tools_location_devices()  
list_tools_location_racks()  
list_tools_location_subnets()  
list_tools_locations()  
update_tools_location()  


__available parameters:__  
address  
description  
id  
lat  
long  
name  

---

__Class ToolsNATApi__

__methods:__  
add_tools_nat()  
del_tools_nat()  
get_tools_nat()  
list_tools_nat_objects()  
list_tools_nat_objects_full()  
list_tools_nats()  
update_tools_nat()  


__available parameters:__  
description  
device_id  
dst  
dst_port  
id  
name  
src  
src_port  
type  

---

__Class ToolsNameserversApi__

__methods:__  
add_tools_nameserver()  
del_tools_nameserver()  
get_tools_nameserver()  
list_tools_nameservers()  
update_tools_nameserver()  


__available parameters:__  
description  
id  
name  
namesrv1  
sections  

---

__Class ToolsRacksApi__

__methods:__  
add_tools_rack()  
del_tools_rack()  
get_tools_rack()  
list_tools_rack_devices()  
list_tools_racks()  
update_tools_rack()  


__available parameters:__  
description  
has_back  
id  
location_id  
name  
row  
size  

---

__Class ToolsScanagentsApi__

__methods:__  
add_tools_scanagent()  
del_tools_scanagent()  
get_tools_scanagent()  
list_tools_scanagents()  
update_tools_scanagent()  


__available parameters:__  
code  
description  
id  
name  
type  

---

__Class ToolsTagsApi__

__methods:__  
add_tools_tag()  
del_tools_tag()  
get_tools_tag()  
list_tools_tags()  
update_tools_tag()  


__available parameters:__  
bgcolor  
compress  
fgcolor  
id  
locked  
showtag  
type  
update_tag  

---

__Class ToolsVRFsApi__

__methods:__  
add_tools_vrf()  
del_vrf()  
get_tools_vrf()  
list_tools_vrf_subnets()  
list_tools_vrfs()  
update_tools_vrf()  


__available parameters:__  
description  
id  
name  
rd  
sections  

---

__Class ToolsVlansApi__

__methods:__  
add_tools_vlan()  
del_vlan()  
get_tools_vlan()  
list_tools_vlan_subnets()  
list_tools_vlans()  
update_tools_vlan()  


__available parameters:__  
description  
domain_id  
id  
name  
number  

---

__Class VRFsApi__

__methods:__  
add_vrf()  
del_vrf()  
get_vrf()  
list_vrf_custom_fields()  
list_vrf_subnets()  
list_vrfs()  
update_vrf()  


__available parameters:__  
description  
id  
name  
rd  
sections  

---

__Class VlansApi__

__methods:__  
add_vlan()  
del_vlan()  
get_vlan()  
list_vlan_custom_fields()  
list_vlan_subnets()  
list_vlan_subnets_section()  
list_vlans()  
search_vlans()  
update_vlan()  


__available parameters:__  
description  
domain_id  
id  
name  
number   

---

__Utility Functions:__

get_tools_location_id()  
get_tools_rack_id()  
get_tools_devicetype_id()  
get_tools_device_id()  
get_device_id()  
get_section_id()  
get_l2domain_id()  
get_vlan_id()  
get_subnet_id()  
get_vrf_id()  
get_tag_id()  
get_address_id()  
