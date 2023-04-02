import requests


def get_bullets_value(stock_code_list):
    id_list_str = ",".join(stock_code_list)
    r = requests.get(
        f'https://push2.eastmoney.com/api/qt/ulist.np/get?fields=f1,f14,f2,f12,f5,f18,f4&secids={id_list_str}')
    stocks = r.json()['data']['diff']
    return stocks


def search_bullets(name):
    r = requests.get(
        f'https://searchapi.eastmoney.com/api/suggest/get?input={name}&type=14&token=D43BF722C8E33BDC906FB84D85E326E8&count=20&_=1678947038546')

    stocks = r.json()['QuotationCodeTable']['Data']
    return stocks
