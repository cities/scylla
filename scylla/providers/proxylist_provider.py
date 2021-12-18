import re

from pyquery import PyQuery

from scylla.database import ProxyIP
from .base_provider import BaseProvider


class ProxyListProvider(BaseProvider):

    def urls(self) -> [str]:
        return [
            'https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt',
            'https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt',
            'https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt',
            'https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt',
            'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt',
            'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt',
            'https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/proxy.txt',
            'https://raw.githubusercontent.com/monosans/proxy-list/main/proxies_anonymous/http.txt',
            'https://raw.githubusercontent.com/monosans/proxy-list/main/proxies_anonymous/socks5.txt',
            'https://raw.githubusercontent.com/monosans/proxy-list/main/proxies_anonymous/socks4.txt',
            'https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt',
            'https://raw.githubusercontent.com/mmpx12/proxy-list/master/http.txt',
            'https://raw.githubusercontent.com/mmpx12/proxy-list/master/https.txt',
            'https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks4.txt',
            'https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks5.txt',
            'https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies.txt',
            'https://raw.githubusercontent.com/Volodichev/proxy-list/main/http.txt',
            'https://raw.githubusercontent.com/hendrikbgr/Free-Proxy-Repo/master/proxy_list.txt'
        ]

    def parse(self, document: PyQuery) -> [ProxyIP]:
        ip_list: [ProxyIP] = []

        raw_html = document.html()

        ip_port_str_list = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{2,5}', raw_html)

        for ip_port in ip_port_str_list:

            ip = re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', ip_port).group(0)
            port = re.search(r':(\d{2,5})', ip_port).group(1)

            if ip and port:
                p = ProxyIP(ip=ip, port=port)
                ip_list.append(p)

        return ip_list

    @staticmethod
    def should_render_js() -> bool:
        return False
