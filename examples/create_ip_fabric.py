#!/usr/bin/env python
""" Example """

import warnings
import phpipamsdk

def add_section(ipam=None, **kwargs):
    """ use API to add a section """
    sections_api = phpipamsdk.SectionsApi(phpipam=ipam)

    addresult = sections_api.add_section(
        name=kwargs['name'],
        description=kwargs['description'],
        permissions=kwargs['permissions'],
        show_vlan=kwargs['show_vlan'],
        show_vrf=kwargs['show_vrf'])

    if 'id' in addresult:
        return addresult['id']
    else:
        raise ValueError('Add Section Failed')

def add_location(ipam=None, **kwargs):
    """ use API to add a location """

    locations_api = phpipamsdk.ToolsLocationsApi(phpipam=ipam)

    addresult = locations_api.add_tools_location(
        name=kwargs['name'],
        description=kwargs['description'],
        address=kwargs['address'])

    if 'id' in addresult:
        return addresult['id']
    else:
        raise ValueError('Add Location Failed')

def add_rack(ipam=None, **kwargs):
    """ use API to add a rack """

    racks_api = phpipamsdk.ToolsRacksApi(phpipam=ipam)

    addresult = racks_api.add_tools_rack(
        name=kwargs['name'],
        size=kwargs['size'],
        description=kwargs['description'],
        location_id=kwargs['location_id'])

    if 'id' in addresult:
        return addresult['id']
    else:
        raise ValueError('Add Rack Failed')

def add_device(ipam=None, **kwargs):
    """ use API to add a device """
    devices_api = phpipamsdk.ToolsDevicesApi(phpipam=ipam)

    addresult = devices_api.add_tools_device(
        hostname=kwargs['hostname'],
        ip=kwargs['ip'],
        sections=kwargs['sections'],
        type_id=kwargs['type_id'],
        location_id=kwargs['location_id'],
        rack_id=kwargs['rack_id'],
        rack_size=kwargs['rack_size'],
        rack_start=kwargs['rack_start'],
        snmp_community=kwargs['snmp_community'],
        snmp_version=kwargs['snmp_version'],
        description=kwargs['description'])

    if 'id' in addresult:
        return addresult['id']
    else:
        raise ValueError('Add Device Failed')

def add_subnet(ipam=None, sect_id=None, loc_id=None, **kwargs):
    """ use API to add a subnet """
    subnets_api = phpipamsdk.SubnetsApi(phpipam=ipam)

    addresult = subnets_api.add_subnet(
        subnet=kwargs['subnet'],
        mask=kwargs['mask'],
        description=kwargs['description'],
        section_id=sect_id,
        permissions=kwargs['permissions'],
        location_id=loc_id)

    if 'id' in addresult:
        return addresult['id']
    else:
        raise ValueError('Add Subnet Failed')

def add_first_free_address(ipam=None, subnet_id=None, device_id=None, **kwargs):
    """ use API to add the first free address within a subnet """
    addresses_api = phpipamsdk.AddressesApi(phpipam=ipam)

    addresult = addresses_api.add_address_first_free(
        hostname=kwargs['hostname'],
        subnet_id=subnet_id,
        device_id=device_id,
        description=kwargs['description'])

    if 'id' in addresult:
        return addresult['id']
    else:
        raise ValueError('Add Address Failed')

def add_first_free_subnet(
        ipam=None, subnet_id=None, mask=None, description=None, loc_id=None):
    """ use API to add first available subnet to a parent subnet """
    subnets_api = phpipamsdk.SubnetsApi(phpipam=ipam)

    addresult = subnets_api.add_subnet_first_free(
        subnet_id=subnet_id,
        description=description,
        location_id=loc_id,
        mask=mask)

    if 'id' in addresult:
        return addresult['id']
    else:
        raise ValueError('Add Address Failed')

if __name__ == "__main__":
    warnings.filterwarnings('ignore')
    IPAM = phpipamsdk.PhpIpamApi(
        api_uri='https://192.168.16.30/api/app/', api_verify_ssl=False)
    IPAM.login(auth=('admin', 'password'))

    # Add the secion to house the new IP Fabric

    section_id = add_section(
        ipam=IPAM,
        name='ip_fabric_one',
        description='my new ip fabric',
        permissions='{"3":"1","2":"2"}',
        show_vlan=True,
        show_vrf=True)

    # Add the location of the new IP Fabric

    location_id = add_location(
        ipam=IPAM,
        name='equinix_dc2',
        description='equinix dc2 cage',
        address='21715 Filigree Court, Ashburn, VA 20147')

    # Add the racks for the new IP Fabric

    r1_id = add_rack(
        ipam=IPAM,
        name='R01', size='42', description='Edge Rack',
        location_id=location_id)

    r2_id = add_rack(
        ipam=IPAM,
        name='R02', size='42', description='Edge Rack',
        location_id=location_id)

    r3_id = add_rack(
        ipam=IPAM,
        name='R03', size='42', description='Compute/Storage Rack',
        location_id=location_id)

    r4_id = add_rack(
        ipam=IPAM,
        name='R04', size='42', description='Compute/Storage Rack',
        location_id=location_id)

    r5_id = add_rack(
        ipam=IPAM,
        name='R05', size='42', description='Compute/Storage Rack',
        location_id=location_id)

    r6_id = add_rack(
        ipam=IPAM,
        name='R06', size='42', description='Compute/Storage Rack',
        location_id=location_id)

    # Add the network devices for the new IP Fabric

    bleaf1 = add_device(
        ipam=IPAM,
        hostname='border-leaf1.dc2',
        ip='192.168.10.1',
        sections=section_id,
        type_id='1',
        location_id=location_id,
        rack_id=r1_id,
        rack_size='2',
        rack_start='39',
        snmp_community='public',
        snmp_version='2',
        description='edge services')

    bleaf2 = add_device(
        ipam=IPAM,
        hostname='border-leaf2.dc2',
        ip='192.168.10.2',
        sections=section_id,
        type_id='1',
        location_id=location_id,
        rack_id=r2_id,
        rack_size='2',
        rack_start='39',
        snmp_community='public',
        snmp_version='2',
        description='edge services')

    spine1 = add_device(
        ipam=IPAM,
        hostname='spine1.dc2',
        ip='192.168.10.3',
        sections=section_id,
        type_id='1',
        location_id=location_id,
        rack_id=r3_id,
        rack_size='2',
        rack_start='41',
        snmp_community='public',
        snmp_version='2',
        description='spine layer')

    leaf1 = add_device(
        ipam=IPAM,
        hostname='leaf1.dc2',
        ip='192.168.10.4',
        sections=section_id,
        type_id='1',
        location_id=location_id,
        rack_id=r3_id,
        rack_size='2',
        rack_start='39',
        snmp_community='public',
        snmp_version='2',
        description='leaf layer')

    spine2 = add_device(
        ipam=IPAM,
        hostname='spine2.dc2',
        ip='192.168.10.5',
        sections=section_id,
        type_id='1',
        location_id=location_id,
        rack_id=r4_id,
        rack_size='2',
        rack_start='41',
        snmp_community='public',
        snmp_version='2',
        description='spine layer')

    leaf2 = add_device(
        ipam=IPAM,
        hostname='leaf2.dc2',
        ip='192.168.10.6',
        sections=section_id,
        type_id='1',
        location_id=location_id,
        rack_id=r4_id,
        rack_size='2',
        rack_start='39',
        snmp_community='public',
        snmp_version='2',
        description='leaf layer')

    spine3 = add_device(
        ipam=IPAM,
        hostname='spine3.dc2',
        ip='192.168.10.7',
        sections=section_id,
        type_id='1',
        location_id=location_id,
        rack_id=r5_id,
        rack_size='2',
        rack_start='41',
        snmp_community='public',
        snmp_version='2',
        description='spine layer')

    leaf3 = add_device(
        ipam=IPAM,
        hostname='leaf3.dc2',
        ip='192.168.10.8',
        sections=section_id,
        type_id='1',
        location_id=location_id,
        rack_id=r5_id,
        rack_size='2',
        rack_start='39',
        snmp_community='public',
        snmp_version='2',
        description='leaf layer')

    leaf4 = add_device(
        ipam=IPAM,
        hostname='leaf4.dc2',
        ip='192.168.10.9',
        sections=section_id,
        type_id='1',
        location_id=location_id,
        rack_id=r6_id,
        rack_size='2',
        rack_start='39',
        snmp_community='public',
        snmp_version='2',
        description='leaf layer')

    # Create a subnet that will be used to assign loopback addresses

    loopbacks = add_subnet(
        ipam=IPAM,
        subnet='10.10.10.0',
        mask='24',
        description='Loopbacks',
        sect_id=section_id,
        loc_id=location_id,
        permissions='{"3":"1","2":"2"}')

    # Assign loopback addresses

    bleaf1_loop = add_first_free_address(
        ipam=IPAM,
        hostname='lo1.border-leaf1.dc2',
        subnet_id=loopbacks,
        device_id=bleaf1,
        description='loopback bleaf1')

    bleaf2_loop = add_first_free_address(
        ipam=IPAM,
        hostname='lo1.border-leaf2.dc2',
        subnet_id=loopbacks,
        device_id=bleaf2,
        description='loopback bleaf2')

    spine1_loop = add_first_free_address(
        ipam=IPAM,
        hostname='lo1.spine1.dc2',
        subnet_id=loopbacks,
        device_id=spine1,
        description='loopback spine1')

    leaf1_loop = add_first_free_address(
        ipam=IPAM,
        hostname='lo1.leaf1.dc2',
        subnet_id=loopbacks,
        device_id=leaf1,
        description='loopback leaf1')

    spine2_loop = add_first_free_address(
        ipam=IPAM,
        hostname='lo1.spine2.dc2',
        subnet_id=loopbacks,
        device_id=spine2,
        description='loopback spine2')

    leaf2_loop = add_first_free_address(
        ipam=IPAM,
        hostname='lo1.leaf2.dc2',
        subnet_id=loopbacks,
        device_id=leaf2,
        description='loopback leaf2')

    spine3_loop = add_first_free_address(
        ipam=IPAM,
        hostname='lo1.spine3.dc2',
        subnet_id=loopbacks,
        device_id=spine3,
        description='loopback spine3')

    leaf3_loop = add_first_free_address(
        ipam=IPAM,
        hostname='lo1.leaf3.dc2',
        subnet_id=loopbacks,
        device_id=leaf3,
        description='loopback leaf3')

    leaf4_loop = add_first_free_address(
        ipam=IPAM,
        hostname='lo1.leaf4.dc2',
        subnet_id=loopbacks,
        device_id=leaf4,
        description='loopback leaf4')

    # Create a subnet that will be used to assign point to point subnets

    point2points = add_subnet(
        ipam=IPAM,
        subnet='10.10.128.0',
        mask='17',
        description='Infra Addressing Parent',
        sect_id=section_id,
        loc_id=location_id,
        permissions='{"3":"1","2":"2"}')

    # Create /30 subnets and assign addresses for spine1 to leaf connections

    spine1_bleaf1 = add_first_free_subnet(
        ipam=IPAM,
        subnet_id=point2points,
        mask='30',
        loc_id=location_id,
        description='spine1 --- bleaf1')

    add_first_free_address(
        ipam=IPAM,
        hostname='eth-2/1.spine1.dc2',
        subnet_id=spine1_bleaf1,
        device_id=spine1,
        description='spine1 --- bleaf1')

    add_first_free_address(
        ipam=IPAM,
        hostname='eth-2/1.border-leaf1.dc2',
        subnet_id=spine1_bleaf1,
        device_id=bleaf1,
        description='bleaf1 --- spine1')

    spine1_bleaf2 = add_first_free_subnet(
        ipam=IPAM,
        subnet_id=point2points,
        mask='30',
        loc_id=location_id,
        description='spine1 --- bleaf2')

    add_first_free_address(
        ipam=IPAM,
        hostname='eth-2/2.spine1.dc2',
        subnet_id=spine1_bleaf2,
        device_id=spine1,
        description='spine1 --- bleaf2')

    add_first_free_address(
        ipam=IPAM,
        hostname='eth-2/1.border-leaf2.dc2',
        subnet_id=spine1_bleaf2,
        device_id=bleaf2,
        description='bleaf2 --- spine1')

    spine1_leaf1 = add_first_free_subnet(
        ipam=IPAM,
        subnet_id=point2points,
        mask='30',
        loc_id=location_id,
        description='spine1 --- leaf1')

    add_first_free_address(
        ipam=IPAM,
        hostname='eth-2/3.spine1.dc2',
        subnet_id=spine1_leaf1,
        device_id=spine1,
        description='spine1 --- leaf1')

    add_first_free_address(
        ipam=IPAM,
        hostname='eth-2/1.leaf1.dc2',
        subnet_id=spine1_leaf1,
        device_id=leaf1,
        description='leaf1 --- spine1')

    spine1_leaf2 = add_first_free_subnet(
        ipam=IPAM,
        subnet_id=point2points,
        mask='30',
        loc_id=location_id,
        description='spine1 --- leaf2')

    add_first_free_address(
        ipam=IPAM,
        hostname='eth-2/4.spine1.dc2',
        subnet_id=spine1_leaf2,
        device_id=spine1,
        description='spine1 --- leaf2')

    add_first_free_address(
        ipam=IPAM,
        hostname='eth-2/1.leaf2.dc2',
        subnet_id=spine1_leaf2,
        device_id=leaf2,
        description='leaf2 --- spine1')

    spine1_leaf3 = add_first_free_subnet(
        ipam=IPAM,
        subnet_id=point2points,
        mask='30',
        loc_id=location_id,
        description='spine1 --- leaf3')

    add_first_free_address(
        ipam=IPAM,
        hostname='eth-2/5.spine1.dc2',
        subnet_id=spine1_leaf3,
        device_id=spine1,
        description='spine1 --- leaf3')

    add_first_free_address(
        ipam=IPAM,
        hostname='eth-2/1.leaf3.dc2',
        subnet_id=spine1_leaf3,
        device_id=leaf3,
        description='leaf3 --- spine1')

    spine1_leaf4 = add_first_free_subnet(
        ipam=IPAM,
        subnet_id=point2points,
        mask='30',
        loc_id=location_id,
        description='spine1 --- leaf4')

    add_first_free_address(
        ipam=IPAM,
        hostname='eth-2/6.spine1.dc2',
        subnet_id=spine1_leaf4,
        device_id=spine1,
        description='spine1 --- leaf4')

    add_first_free_address(
        ipam=IPAM,
        hostname='eth-2/1.leaf4.dc2',
        subnet_id=spine1_leaf4,
        device_id=leaf4,
        description='leaf4 --- spine1')

    # Create /30 subnets and assign addresses for spine2 to leaf connections

    spine2_bleaf1 = add_first_free_subnet(
        ipam=IPAM,
        subnet_id=point2points,
        mask='30',
        loc_id=location_id,
        description='spine2 --- bleaf1')

    add_first_free_address(
        ipam=IPAM,
        hostname='eth-2/1.spine2.dc2',
        subnet_id=spine2_bleaf1,
        device_id=spine2,
        description='spine2 --- bleaf1')

    add_first_free_address(
        ipam=IPAM,
        hostname='eth-2/2.border-leaf1.dc2',
        subnet_id=spine2_bleaf1,
        device_id=bleaf1,
        description='bleaf1 --- spine2')

    spine2_bleaf2 = add_first_free_subnet(
        ipam=IPAM,
        subnet_id=point2points,
        mask='30',
        loc_id=location_id,
        description='spine2 --- bleaf2')

    add_first_free_address(
        ipam=IPAM,
        hostname='eth-2/2.spine2.dc2',
        subnet_id=spine2_bleaf2,
        device_id=spine2,
        description='spine2 --- bleaf2')

    add_first_free_address(
        ipam=IPAM,
        hostname='eth-2/2.border-leaf2.dc2',
        subnet_id=spine2_bleaf2,
        device_id=bleaf2,
        description='bleaf2 --- spine2')

    spine2_leaf1 = add_first_free_subnet(
        ipam=IPAM,
        subnet_id=point2points,
        mask='30',
        loc_id=location_id,
        description='spine2 --- leaf1')

    add_first_free_address(
        ipam=IPAM,
        hostname='eth-2/3.spine2.dc2',
        subnet_id=spine2_leaf1,
        device_id=spine2,
        description='spine2 --- leaf1')

    add_first_free_address(
        ipam=IPAM,
        hostname='eth-2/2.leaf1.dc2',
        subnet_id=spine2_leaf1,
        device_id=leaf1,
        description='leaf1 --- spine2')

    spine2_leaf2 = add_first_free_subnet(
        ipam=IPAM,
        subnet_id=point2points,
        mask='30',
        loc_id=location_id,
        description='spine2 --- leaf2')

    add_first_free_address(
        ipam=IPAM,
        hostname='eth-2/4.spine2.dc2',
        subnet_id=spine2_leaf2,
        device_id=spine2,
        description='spine2 --- leaf2')

    add_first_free_address(
        ipam=IPAM,
        hostname='eth-2/2.leaf2.dc2',
        subnet_id=spine2_leaf2,
        device_id=leaf2,
        description='leaf2 --- spine2')

    spine2_leaf3 = add_first_free_subnet(
        ipam=IPAM,
        subnet_id=point2points,
        mask='30',
        loc_id=location_id,
        description='spine2 --- leaf3')

    add_first_free_address(
        ipam=IPAM,
        hostname='eth-2/5.spine2.dc2',
        subnet_id=spine2_leaf3,
        device_id=spine2,
        description='spine2 --- leaf3')

    add_first_free_address(
        ipam=IPAM,
        hostname='eth-2/2.leaf3.dc2',
        subnet_id=spine2_leaf3,
        device_id=leaf3,
        description='leaf3 --- spine2')

    spine2_leaf4 = add_first_free_subnet(
        ipam=IPAM,
        subnet_id=point2points,
        mask='30',
        loc_id=location_id,
        description='spine2 --- leaf4')

    add_first_free_address(
        ipam=IPAM,
        hostname='eth-2/6.spine2.dc2',
        subnet_id=spine2_leaf4,
        device_id=spine2,
        description='spine2 --- leaf4')

    add_first_free_address(
        ipam=IPAM,
        hostname='eth-2/2.leaf4.dc2',
        subnet_id=spine2_leaf4,
        device_id=leaf4,
        description='leaf4 --- spine2')

    # Create /30 subnets and assign addresses for spine3 to leaf connections

    spine3_bleaf1 = add_first_free_subnet(
        ipam=IPAM,
        subnet_id=point2points,
        mask='30',
        loc_id=location_id,
        description='spine3 --- bleaf1')

    add_first_free_address(
        ipam=IPAM,
        hostname='eth-2/1.spine3.dc2',
        subnet_id=spine3_bleaf1,
        device_id=spine3,
        description='spine3 --- bleaf1')

    add_first_free_address(
        ipam=IPAM,
        hostname='eth-2/3.border-leaf1.dc2',
        subnet_id=spine3_bleaf1,
        device_id=bleaf1,
        description='bleaf1 --- spine3')

    spine3_bleaf2 = add_first_free_subnet(
        ipam=IPAM,
        subnet_id=point2points,
        mask='30',
        loc_id=location_id,
        description='spine3 --- bleaf2')

    add_first_free_address(
        ipam=IPAM,
        hostname='eth-2/2.spine3.dc2',
        subnet_id=spine3_bleaf2,
        device_id=spine3,
        description='spine3 --- bleaf2')

    add_first_free_address(
        ipam=IPAM,
        hostname='eth-2/3.border-leaf2.dc2',
        subnet_id=spine3_bleaf2,
        device_id=bleaf2,
        description='bleaf2 --- spine3')

    spine3_leaf1 = add_first_free_subnet(
        ipam=IPAM,
        subnet_id=point2points,
        mask='30',
        loc_id=location_id,
        description='spine3 --- leaf1')

    add_first_free_address(
        ipam=IPAM,
        hostname='eth-2/3.spine3.dc2',
        subnet_id=spine3_leaf1,
        device_id=spine3,
        description='spine3 --- leaf1')

    add_first_free_address(
        ipam=IPAM,
        hostname='eth-2/3.leaf1.dc2',
        subnet_id=spine3_leaf1,
        device_id=leaf1,
        description='leaf1 --- spine3')

    spine3_leaf2 = add_first_free_subnet(
        ipam=IPAM,
        subnet_id=point2points,
        mask='30',
        loc_id=location_id,
        description='spine3 --- leaf2')

    add_first_free_address(
        ipam=IPAM,
        hostname='eth-2/4.spine3.dc2',
        subnet_id=spine3_leaf2,
        device_id=spine3,
        description='spine3 --- leaf2')

    add_first_free_address(
        ipam=IPAM,
        hostname='eth-2/3.leaf2.dc2',
        subnet_id=spine3_leaf2,
        device_id=leaf2,
        description='leaf2 --- spine3')

    spine3_leaf3 = add_first_free_subnet(
        ipam=IPAM,
        subnet_id=point2points,
        mask='30',
        loc_id=location_id,
        description='spine3 --- leaf3')

    add_first_free_address(
        ipam=IPAM,
        hostname='eth-2/5.spine3.dc2',
        subnet_id=spine3_leaf3,
        device_id=spine3,
        description='spine3 --- leaf3')

    add_first_free_address(
        ipam=IPAM,
        hostname='eth-2/3.leaf3.dc2',
        subnet_id=spine3_leaf3,
        device_id=leaf3,
        description='leaf3 --- spine3')

    spine3_leaf4 = add_first_free_subnet(
        ipam=IPAM,
        subnet_id=point2points,
        mask='30',
        loc_id=location_id,
        description='spine3 --- leaf4')

    add_first_free_address(
        ipam=IPAM,
        hostname='eth-2/6.spine3.dc2',
        subnet_id=spine3_leaf4,
        device_id=spine3,
        description='spine3 --- leaf4')

    add_first_free_address(
        ipam=IPAM,
        hostname='eth-2/3.leaf4.dc2',
        subnet_id=spine3_leaf4,
        device_id=leaf4,
        description='leaf4 --- spine3')

    IPAM.logout()
