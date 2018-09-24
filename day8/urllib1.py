
import urllib.request
url='https://www.baidu.com'
header={
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36'
}

def use_proxy(proxy_addr,url):
    import urllib.request
    proxy=urllib.request.ProxyHandler({'http':proxy_addr})
    request=urllib.request.Request(url,headers=header)
    request=urllib.request.Request(url,headers=header)
    openner=urllib.request.build_opener(proxy,urllib.request.HTTPHandler)
    urllib.request.install_opener(openner)
    data=urllib.request.urlopen(request).read().decode('utf-8')
    return data


proxy_addr='115.159.199.81'
data=use_proxy(proxy_addr,'https://www.baidu.com')
print(data)
