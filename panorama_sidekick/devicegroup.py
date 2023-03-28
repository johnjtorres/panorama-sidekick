from dataclasses import dataclass
from typing import List

from panorama_sidekick.firewall import Firewall


@dataclass
class DeviceGroup:
    name: str
    firewalls: List[Firewall]
