import pymysql
import configuration as config


def addOrders(id_order, date) :
    try :
        connection = pymysql.connect(
            host=config.host, 
            port=3306,
            user=config.user,
            password=config.password,
            database=config.db_name,
            cursorclass=pymysql.cursors.DictCursor
        )
        try :
            with connection.cursor() as cursor :
                insert_query = "INSERT INTO `new_orders_moysklad` (id_order, date) VALUES (%s, %s);" 
                cursor.execute(insert_query, (id_order, date))
                connection.commit()
                print('Добавили завтрашние заказы в базу данных')
        finally:
            connection.close()
    except Exception as ex :
        print("Не подключилось")
        print(ex)


def getOrders() :
    try :
        connection = pymysql.connect(
            host=config.host, 
            port=3306,
            user=config.user,
            password=config.password,
            database=config.db_name,
            cursorclass=pymysql.cursors.DictCursor
        )
        print('Подключение состоялось getOrders')
        try :
            with connection.cursor() as cursor :
                select_all_rows = "SELECT * FROM `new_orders_moysklad`"
                cursor.execute(select_all_rows)
                orders = cursor.fetchall()
                # for row in otgruzkaa :
                #     print(row)
        finally:
            connection.close()
    except Exception as ex :
        print("Не подключилось getWorkers.py")
        print(ex)

    return orders

def addTodayOrdersNow(id_order, date) :
    try :
        connection = pymysql.connect(
            host=config.host, 
            port=3306,
            user=config.user,
            password=config.password,
            database=config.db_name,
            cursorclass=pymysql.cursors.DictCursor
        )
        try :
            with connection.cursor() as cursor :
                insert_query = "INSERT INTO `today_orders_moysklad` (id_order, date) VALUES (%s, %s);" 
                cursor.execute(insert_query, (id_order, date))
                connection.commit()
                print('Добавили сегодняшние заказы в базу данных')
        finally:
            connection.close()
    except Exception as ex :
        print("Не подключилось")
        print(ex)


def getTodayOrders() :
    try :
        connection = pymysql.connect(
            host=config.host, 
            port=3306,
            user=config.user,
            password=config.password,
            database=config.db_name,
            cursorclass=pymysql.cursors.DictCursor
        )
        print('Подключение состоялось getTodayOrders')
        try :
            with connection.cursor() as cursor :
                select_all_rows = "SELECT * FROM `today_orders_moysklad`"
                cursor.execute(select_all_rows)
                orders = cursor.fetchall()
                # for row in otgruzkaa :
                #     print(row)
        finally:
            connection.close()
    except Exception as ex :
        print("Не подключилось getWorkers.py")
        print(ex)

    return orders

