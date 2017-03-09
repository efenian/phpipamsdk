"""
PhpIpam Api SDK
Eric Donohue <edonohue@brocade.com>
"""

from .controllers import AddressesApi
from .controllers import L2DomainsApi
from .controllers import PrefixesApi
from .controllers import SectionsApi
from .controllers import SubnetsApi
from .controllers import ToolsDevicesApi
from .controllers import ToolsDeviceTypesApi
from .controllers import ToolsLocationsApi
from .controllers import ToolsNameserversApi
from .controllers import ToolsNATApi
from .controllers import ToolsRacksApi
from .controllers import ToolsScanagentsApi
from .controllers import ToolsTagsApi
from .controllers import ToolsVlansApi
from .controllers import ToolsVRFsApi
from .controllers import VlansApi
from .controllers import VRFsApi

from .phpipam import PhpIpamApi
