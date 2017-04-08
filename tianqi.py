#-*-coding:utf-8-*-

import json
from urllib2 import urlopen
import sys

identme_url = 'http://ident.me'
netcn_url = 'http://www.net.cn/static/customercare/yourip.asp'
tianqi_url = 'https://www.baidu.com/home/other/data/weatherInfo'

def get_ip():
    # identme 是境外站点 速度慢
    #globalip = urlopen(identme_url).read()
    html = urlopen(netcn_url).read()

    # net.cn 是国内站点速度快
    ip = html[html.find('<h2>')+4:html.find('</h2>')].split(', ')[0]
    print(ip)
    print("当前IP：%s" % ip)
    return ip

def get_city():
    city = ''
    if len(sys.argv)>2:
        city = sys.argv[1]

    return city


def get_weather(city=None, ip=None):
    param = ""
    if city == "":
        param = "?ip=%s" % ip
    else:
        param = "?city=%s" % city
    res = urlopen(tianqi_url+param)
    jso = json.loads(res.read())
    return jso

def print_w(w):
    fmt = u'''
    {city}
    {0[time]}
    {0[condition]}
    {0[wind]}
    {0[temp]}
    '''
    content = w['data']['weather']['content']
    city = content['city']
    days = ['today','tomorrow','thirdday','fourthday', 'fifthday']
    for day in days:
        print(fmt.format(content[day],city=city))
    pass

def main():
    ip = get_ip()
    city = get_city()
    weather=get_weather(city=city,ip=ip)
    print_w(weather)
    pass

if __name__ == '__main__':
    main()
