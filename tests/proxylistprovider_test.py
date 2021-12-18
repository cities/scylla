import pytest
import requests
from random import choice
from pyquery import PyQuery
from scylla.database import ProxyIP
from scylla.providers.proxylist_provider import ProxyListProvider

def test_prase():
    provider = ProxyListProvider()
    urls = provider.urls()
    with requests.session() as session:
        response = session.get(choice(urls))
        proxies = provider.parse(PyQuery(response.text))

        assert len(proxies) >= 0

        if len(proxies) > 0:
            assert isinstance(proxies[0], ProxyIP)

