import requests
import configuration as config


def getJson(day, next_day) :
    try :
        url = ("https://online.moysklad.ru/api/remap/1.2/entity/customerorder?expand=state&filter=moment>=" + day + ";moment<=" + next_day)

        r = requests.get(url, auth=(config.mlogin, config.mpassword))
        return r.text
    except Exception as ex :
        print('Подключение в moysklad.ru не состоялось!')
        print(ex)


def addTodayOrders(day, next_day) :
    try :
        url = ("https://online.moysklad.ru/api/remap/1.2/entity/customerorder?expand=state&filter=moment>=" + day + ";moment<=" + next_day)

        r = requests.get(url, auth=(config.mlogin, config.mpassword))
        return r.text
    except Exception as ex :
        print('Подключение в moysklad.ru не состоялось!')
        print(ex)
