from typing import Union

import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class Panorama:
    def __init__(
        self,
        hostname: str,
        api_key: str,
        timeout: int = 30,
        verify: Union[bool, str] = False,
    ) -> None:
        self.hostname = hostname
        self.api_key = api_key
        self.timeout = timeout
        self.verify = verify

    def get(self, uri: str) -> str:
        url = f"https://{self.hostname}" + uri
        response = requests.get(url, timeout=self.timeout, verify=self.verify)
        response.raise_for_status()
        return response.text

    def op(self, cmd: str) -> str:
        uri = f"/?type=op&cmd={cmd}"
        return self.get(uri)
