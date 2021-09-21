import requests
import configuration as config


def getJson(day, next_day) :
    print(day)
    print(next_day)
    url = ("https://online.moysklad.ru/api/remap/1.2/entity/customerorder?expand=state&filter=moment>=" + day + ";moment<=" + next_day)

    r = requests.get(url, auth=(config.mlogin, config.mpassword))
    return r.text


def addTodayOrders(day, next_day) :
    url = ("https://online.moysklad.ru/api/remap/1.2/entity/customerorder?expand=state&filter=moment>=" + day + ";moment<=" + next_day)

    r = requests.get(url, auth=(config.mlogin, config.mpassword))
    return r.text
