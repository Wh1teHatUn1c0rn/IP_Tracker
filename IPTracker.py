import json
import requests
from datetime import datetime


class AttackTracker:
    def __init__(self, api_url):
        self.api_url = api_url

    def track(self, src_ip):
        # Get information about the IP address
        ip_info = requests.get(f"{self.api_url}/ip/{src_ip}").json()

        # Check if the IP address is a known attacker
        if "attacker" in ip_info and ip_info["attacker"] is True:
            print(f"{src_ip} is a known attacker")
        else:
            # Check if the IP address is a VPN or a proxy
            if "vpn" in ip_info and ip_info["vpn"] is True:
                print(f"{src_ip} is a VPN or a proxy")
            else:
                # Get the ASN information
                asn_info = requests.get(f"{self.api_url}/asn/{ip_info['asn']}").json()

                # Check if the ASN is associated with a known attacker
                if "attacker" in asn_info and asn_info["attacker"] is True:
                    print(f"{src_ip} is associated with a known attacker ASN: {ip_info['asn']}")
                else:
                    print(f"{src_ip} does not appear to be a known attacker")


tracker = AttackTracker("http://example.com/api")
tracker.track("192.168.1.1")
