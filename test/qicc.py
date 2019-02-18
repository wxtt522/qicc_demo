# 企查查工商信息批量查询版

import sys
from urllib import parse

import requests
from pyquery import PyQuery as pq

headers = {

    'accept': 'text / html, application / xhtml + xml, application / xml;q = 0.9, image / webp, image / apng, * / *;q = 0.8',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'dnt': '1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'

}
qicc = 'https://www.qichacha.com'
url = 'https://www.qichacha.com/search?key='
file = sys.argv[1]
print(sys.argv[0].replace('qicc.py', 'out_' + sys.argv[1]))
file2 = open(sys.argv[0].replace('qicc.py', 'out_' + sys.argv[1]), 'w', encoding='utf-8')
print('进入工商信息查询...')
print('数据源文件：' + file + '\n\n')
for company in open(file, encoding='utf-8'):
    key = company.strip()
    print('查询条件:' + key)
    href = url + parse.quote_plus(key)
    response = requests.get(href, headers=headers)

    print('查询状态:' + str(response.status_code))
    d = pq(response.text)
    titil = d.find('head').find('title').text()
    print(titil)

    td = d('tbody').find('tr').eq(0)
    company_name = td.find('a').eq(0).text()
    print('公司名称:' + company_name, file=file2)
    if key in company_name:
        href = td.find('a').eq(0).attr('href')
        if href:
            href = qicc + href
            body = requests.get(href, headers=headers)
            doc = pq(body.text)
            cominfo = doc('#Cominfo')
            table = cominfo.find('table').eq(1)
            if table:
                print(table.find('tr').eq(-1).find('td').eq(0).text() + ':' + table.find('tr').eq(-1).find('td').eq(
                    1).text(), file=file2)
                print(table.find('tr').eq(0).find('td').eq(0).text() + ':' + table.find('tr').eq(0).find('td').eq(
                    1).text(), file=file2)
                print(table.find('tr').eq(2).find('td').eq(0).text() + ':' + table.find('tr').eq(2).find('td').eq(
                    1).text(), file=file2)
                print(table.find('tr').eq(4).find('td').eq(0).text() + ':' + table.find('tr').eq(4).find('td').eq(
                    1).text(), file=file2)
                print(table.find('tr').eq(-2).find('td').eq(0).text() + ':' + table.find('tr').eq(-2).find('td').eq(
                    1).text().replace('查看地图', '').replace('附近公司', '').strip(), file=file2)

            table0 = cominfo.find('table').eq(0)
            if table0:
                print('企业法人:' + table0.find('tr').eq(1).find('h2').text(), file=file2)

            print('\n', file=file2)
            print()
            print()

print('查询完毕,查获数据保留至：' + 'out_' + sys.argv[1])
file2.close()
