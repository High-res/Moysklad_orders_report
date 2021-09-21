
import aioschedule
import time
import asyncio
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import datetime
from datetime import date
from dateutil import parser as dtparser
import configuration as config
import Modules


office = 'Офис г. Алматы'
sklAlm = 'г. Алматы, Бокейханова 49, склад 11'
sklAst = 'г. Нур-Султан, ул. Пушкина 35'
print('Start')
# print(Modules.getOrders())
# print(Modules.getOtgruzkassss())
loop = asyncio.get_event_loop()
bot = Bot(config.BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher(bot, loop=loop)
message = types.Message
def times() :
    today = date.today()
    day = today.strftime('%Y-%m-%d')
    nowDay = today.strftime('%Y-%m-%d')
    date_obj = dtparser.parse(day)
    date_obj += datetime.timedelta(days=1)
    day = date_obj.strftime('%Y-%m-%d')

    next_day = day
    date_ob = dtparser.parse(day)
    date_ob += datetime.timedelta(days=1)
    next_day = date_ob.strftime('%Y-%m-%d')
    return day, nowDay, next_day


print(times()[0],times()[1],times()[2])
yesterday_orders = []
yesterdayOrd = []
today_orders = []
todayOrd = []
times_0 = '2021-09-14'
times_1 = '2021-09-13'
times_2 = '2021-09-15'
# 

todOrdd = '2021-09-08'
def yesterdayOrders() :
    getOrders = Modules.getOrders()

    for get in getOrders :
        if str(times()[1]) == get['date'] :
        # if str(times_1) == get['date'] :
            yesterday_orders.append(get)
    return yesterday_orders

def yestOrdr() :
    for i in range(len(yesterdayOrders())) :
        yesterdayOrd.append(yesterdayOrders()[i]['id_order'])
    return yesterdayOrd


def todayOrders() :
    getTodayOrders = Modules.getTodayOrders()

    for get in getTodayOrders :
        if str(times()[1]) == get['date'] :
        # if str(times_1) == get['date'] :
            today_orders.append(get)
    return today_orders
def todayOtgr() :
    for i in range(len(todayOrders())) :
        todayOrd.append(todayOrders()[i]['id_order'])
    return todayOrd
# print(yestOrdr())
print(todayOrders())
def notTodayOrders() :
    # yestOrdr().clear()
    # todayOtgr().clear()
   result = list(set(yestOrdr()) ^ set(todayOtgr()))
   return result
# print(notTodayOrders())
async def send_message(channel_id: int, text: int):
    await bot.send_message(channel_id, text)

# def echo():
    # Modules.today_otgruzka(times()[1], times()[0])
#     # counters = Modules.getNeeds(times()[0], times()[2], times()[1])
#     counters = Modules.getNeeds(times_0, times_2, times_1)
#     # otgruzka = Modules.getOtgruzka(times()[1], config.mlogin, config.mpassword)
#     otgruzka = Modules.getOtgruzka(times_1, config.mlogin, config.mpassword)
#     f_s_sklad = f'{counters[0]:,}'
#     # almaty_skald = f"Склад: {sklAlm} \nДата: {times()[0]} \nКоличество заказов: {counters[1]} \nСумма заказов: {f_s_sklad}"
#     almaty_skald = f"Склад: {sklAlm} \nДата: {times_0} \nКоличество заказов: {counters[1]} \nСумма заказов: {f_s_sklad}"
#     # otgruzka_otchet = f'Дата: {times()[1]} \nКоличество отгрузок: {otgruzka[0]} \nСумма отгрузок: {otgruzka[1]} \nНе отгружены: {notTodayOrders()}'
#     otgruzka_otchet = f'Дата: {times_1} \nКоличество отгрузок: {otgruzka[0]} \nСумма отгрузок: {otgruzka[1]} \nНе отгружены: {notTodayOrders()}'
    
#     print(almaty_skald)
#     print(otgruzka_otchet)
#     # for i in config.admin_id:
#     #     await send_message(channel_id=i, text = f"{otgruzka_otchet}")
#     #     await send_message(channel_id=i, text = f"{almaty_skald}")
#     # notTodayOrders().clear()
# echo()
# async def schedulerr():
#     aioschedule.every().day.at('11:17').do(echo)
#     while True:
#         await aioschedule.run_pending()
#         time.sleep(1)

# async def on_startup(_):
# #    asyncio.create_task(scheduler())
#    asyncio.create_task(schedulerr())

# if __name__ == "__main__" :
#     executor.start_polling(dp, loop=loop, on_startup=on_startup)