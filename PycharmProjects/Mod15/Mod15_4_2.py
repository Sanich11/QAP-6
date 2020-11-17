"""
Задание на автоматизацию проверки ответа API от сервера.
У вас есть следующие требования к ответу:

timestamp: int
referer: string (url)
location: string (url)
remoteHost: string
partyId: string
sessionId: string
pageViewId: string
eventType: string (itemBuyEvent или itemViewEvent)
item_id: string
item_price: int
item_url: string (url)
basket_price: string
detectedDuplicate: bool
detectedCorruption: bool
firstInSession: bool
userAgentName: string
https://github.com/SkillfactoryCoding/QAP/blob/master/json_example_QAP.json
Здесь можно взять пример json с ответами некоего интернет-магазина,
составленный по этим правилам.

Вам нужно написать простой тест, который проверяет json на правильность полей.
То есть проверяет, что каждый объект в json:

Содержит все перечисленные в требованиях поля.
Не имеет других полей.
Все поля имеют именно тот тип, который указан в требованиях:
int — это значит целое число;
string — произвольная строка;
string (url) — это строка с url. В рамках этого задания проверяем,
что url начинается c http:\\ или https:\\;
string (itemBuyEvent или itemViewEvent) — это строка, в которой может быть
только эти конкретные два значения и никакие другие;
bool — булево значение, то есть True или False.
Тест должен вернуть Pass или список значений, которые тест посчитал
ошибочными, и причину, почему они ошибочные.
"""

import json

with open('json_example_QAP.json', encoding='utf8') as f:
    templates = json.load(f)

def CheckInt(item):
    return isinstance(item, int)

def CheckStr(item):
    return isinstance(item, str)

def CheckBool(item):
    return isinstance(item, bool)

def CheckUrl(item):
    if isinstance(item, str):
        return item.startswith('http://') or item.startswith('https://')
    else:
        return False

def CheckStrValue(item, val):
    if isinstance(item, str):
        return item in val
    else:
        return False

def ErrorLog(item, value, string):
    Error.append({item: f'{value}, {string}'})

listOfItems = {'timestamp': 'int', 'referer': 'url', 'location': 'url',
               'remoteHost': 'str', 'partyId': 'str', 'sessionId': 'str',
               'pageViewId': 'str', 'eventType': 'val', 'item_id': 'str',
               'item_price': 'int', 'item_url': 'url', 'basket_price': 'str',
               'detectedDuplicate': 'bool', 'detectedCorruption': 'bool',
               'firstInSession': 'bool', 'userAgentName': 'str'}

Error = []
for items in templates:
    for item in items:
        if item in listOfItems:
            if listOfItems[item] == 'int':
                if not CheckInt(items[item]):
                    ErrorLog(item, items[item], f'ожидали тип' \
                            '{listOfItems[item]}')
            elif listOfItems[item] == 'str':
                if not CheckStr(items[item]):
                    ErrorLog(item, items[item], f'ожидали тип' \
                            '{listOfItems[item]}')
            elif listOfItems[item] == 'bool':
                if not CheckBool(items[item]):
                    ErrorLog(item, items[item], f'ожидали тип' \
                            '{listOfItems[item]}')
            elif listOfItems[item] == 'url':
                if not CheckUrl(items[item]):
                    ErrorLog(item, items[item], f'ожидали тип' \
                            '{listOfItems[item]}')
            elif listOfItems[item] == 'val':
                if not CheckStrValue(items[item], ['itemBuyEvent',
                                     'itemViewEvent']):
                    ErrorLog(item, items[item], 'ожидали значение'
                            'itemBuyEvent или itemViewEvent')
            else:
                ErrorLog(item, items[item], 'неожиданное значение')
        else:
            ErrorLog(item, items[item], 'неожиданная переменная')

if Error == []:
    print('Pass')
else:
    print('Fail')
    print(Error)
