import json

import Connect as conn
import DBConnect as db


otmena = 'https://online.moysklad.ru/api/remap/1.2/entity/customerorder/metadata/states/be28cbb9-d114-11e7-7a69-8f550005cfbd'
sklad_almaty = 'https://online.moysklad.ru/api/remap/1.2/entity/store/279b8372-f424-11ea-0a80-03d4000a7c36'
dostavlen = 'https://online.moysklad.ru/api/remap/1.2/entity/customerorder/metadata/states/be28c8eb-d114-11e7-7a69-8f550005cfbb'
def today_otgruzka(day, next_day) :
    try :
        massiv = json.loads(conn.addTodayOrders(day, next_day))
    except Exception as ex :
        print("Не подключилось")
        print(ex)
    if massiv :
        # massiv получаем данные полученные с api
        allorders = massiv['rows']

        # Массив данных
        items_almSklad = []
        # Количество заказов
        count_almSklad = 0
        # Сумма денег в Алматы
        sum_almSklad = []

        # for i in massiv3 :
        #     print(i)
        #     if otmena == i['state']['meta']['href'] :
                
        #         clearElem.append(i)
            # print(i)
        # massiv3.remove(clearElem)
        # Удалить отменненные заказы
        print(len(allorders))
        for i in allorders :
            if 'store' in i :
                if i['store']['meta']['href'] == sklad_almaty :
                    count_almSklad += 1
                    items_almSklad.append(i)
            else :
                print('Store нету в переменной i')
        # Выше я разделил по складам и записал каждый в массив
        # Здесь слежу за изменениями после 15:00 сегодняшнего дня
        for order in range(len(items_almSklad)) :
            db.addTodayOrdersNow(items_almSklad[order]['name'] , day)
        if items_almSklad:
            for j_almSklad in items_almSklad :
                sum_almSklad.append(j_almSklad['sum'])
            # Выше получил суммы заказов по городам
            new_sum_almSklad = []
            for x_sum_almSklad in sum_almSklad :
                new_sum_almSklad.append('%.f' % x_sum_almSklad)
            # Выше удаляем все значения после точки
            l_sum_almSklad = []
            for x_l_sum_almSklad in new_sum_almSklad :
                l_sum_almSklad.append(int(x_l_sum_almSklad) // 100)

            all_sum_almSklad = sum(l_sum_almSklad)
            # Выше начиная с l_sum_alm убираем не нужные последние 2 цифры и суммируем каждый
            otm_almSklad = 0
            otm_almSklad_sum = []

            for otm_almSkad in items_almSklad :
                if otmena == otm_almSkad['state']['meta']['href'] :
                    otm_almSklad += 1
                    otm_almSklad_sum.append(int(otm_almSkad['sum']))
            # Выше находим суммы отмененных заказов, считаем сколько отмененных заказов

            otm_new_sum_almSklad = []
            for otm_sum_almSklad in otm_almSklad_sum :
                otm_new_sum_almSklad.append('%.f' % otm_sum_almSklad)
            # Выше удаляем все значения после точки
            otm_l_sum_almSklad = []
            for x_otm_l_sum_almSklad in otm_new_sum_almSklad :
                otm_l_sum_almSklad.append(int(x_otm_l_sum_almSklad) // 100)
            all_otm_sum_almSklad = sum(otm_l_sum_almSklad)
            # Выше начиная с l_sum_alm убираем не нужные последние 2 цифры и суммируем каждый 
            final_summ_sklad = all_sum_almSklad - all_otm_sum_almSklad
            final_count_sklad = count_almSklad - otm_almSklad
        return final_summ_sklad, final_count_sklad
    else :
        print('Вышло пустое значение! Связь с moysklad.ru оборвана!')
