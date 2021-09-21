import json
from datetime import date
import requests
import Modules


today = date.today()
day = today.strftime('%Y-%m-%d')
nowDay = today.strftime('%Y-%m-%d')
allOtgruzkaId = []
sklad_almaty = 'https://online.moysklad.ru/api/remap/1.2/entity/store/279b8372-f424-11ea-0a80-03d4000a7c36'
def getOtgruzka(nowDay, login, password) :
    url = ("https://online.moysklad.ru/api/remap/1.2/entity/demand?expand=state&filter=moment>=" + nowDay)
    # url = ("https://online.moysklad.ru/api/remap/1.2/entity/demand?expand=state&filter=moment>=2021-08-16")

    r = requests.get(url, auth=(login, password))
    # r = requests.get(url, auth=(config.mlogin, config.mpassword))
    otgruzka = json.loads(r.text)
    massiv2 = []
    massiv2.append(otgruzka['rows'])
    massiv3 = massiv2[0]
    # print(massiv3)
    all_count = 0
    all_sum = []
    allOtgruzkaIdNew = []
    # print(getOtgruzka())
    for i in massiv3 :
        if i['store']['meta']['href'] == sklad_almaty :
            Modules.addOtgruzka(i['name'], nowDay)
            all_count += 1
            all_sum.append(i['sum'])
    # Записали все суммы в массиве
    new_sum = []
    for j in all_sum :
        new_sum.append('%.f' % j)
    # Убрали все знаки после запятой
    new_all_sum = []
    for k in new_sum :
        new_all_sum.append(int(k) // 100)
    # Убрали последние 2 нуля
    final_sum = sum(new_all_sum)
    # Суммировали массив
    sumOtgruzka = f'{final_sum:,}'
    # Получение общей суммы заказов
    # Получим количество заказов
    # print(getOtgruzka)
    # print(f'{all_count}\n{sumOtgruzka}')
    return all_count, sumOtgruzka
