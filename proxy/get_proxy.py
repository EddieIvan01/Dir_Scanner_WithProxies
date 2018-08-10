import requests
import sys
import random

'''
Decorator for dir_scanner
using ProxyPool from
https://github.com/eddieivan01/ProxyPool
author: EddieIvan
'''

local = "http://127.0.0.1:2333"
proxy_json = requests.get(local + "/proxy?act=get").json()
proxy_list = []
if proxy_json["code"] == 200:
    for i in proxy_json["proxies"]:
        proxy_list.append(
            {
                "http":"http://" + i["ip"] + ":" + i["port"],
                "https":"https://" + i["ip"] + ":" + i["port"]
            }
        )
else:
    print("[*]request for proxy error")

def RequestWithProxy(f):
    try:
        res = requests.get(local, timeout = 3)
    except:
        print("[*]Local server are not listening")
        sys.exit(-1)
    def foo(arg):
        proxy = random.choice(proxy_list)
        f(arg, proxy)
    return foo
