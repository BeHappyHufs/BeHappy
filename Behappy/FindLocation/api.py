from urllib.parse import urlencode, unquote, quote_plus
import requests
from bs4 import BeautifulSoup

serviceKey="aEwwPiJLOfQLF991Fvvcv6piLOUwnO7uH7qiX6DXVazK8EDb6Yw39Hsq7xA+F4ux1KvKgLNVTx3CP7/IvdpOtQ=="

def showBin():
    data = []
    bean_kind =[]
    url = "https://api.odcloud.kr/api/15087773/v1/uddi:6bcb9ebf-d368-4ac8-9382-a9e82437f74d?page=1&perPage=10&returnType=XML&serviceKey=aEwwPiJLOfQLF991Fvvcv6piLOUwnO7uH7qiX6DXVazK8EDb6Yw39Hsq7xA%2BF4ux1KvKgLNVTx3CP7%2FIvdpOtQ%3D%3D"
    res = requests.get(url)
    xml = res.text
    soup = BeautifulSoup(xml,'html.parser')
    for tag in soup.find_all('소재지지번주소'):
        data.append(tag.text)
    for tag in soup.find_all('쓰레기통형태'):
        bean_kind.append(tag.text)
    res= dict(zip(data,bean_kind))
    return res