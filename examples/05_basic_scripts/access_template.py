#!/usr/bin/env python3

import sys

vlan = sys.argv[1]

access_template = [
    "switchport mode access",
    "switchport access vlan {}",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

print("\n".join(access_template).format(vlan))
