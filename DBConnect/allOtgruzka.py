import pymysql
import configuration as config


def addOtgruzka(id_otgruzka, date) :
    try :
        connection = pymysql.connect(
            host=config.host, 
            port=3306,
            user=config.user,
            password=config.password,
            database=config.db_name,
            cursorclass=pymysql.cursors.DictCursor
        )
        print('Подключение состоялось addOtgruzka')
        try :
            with connection.cursor() as cursor :
                insert_query = "INSERT INTO `otgruzka_moysklad` (id_otgruzka, date) VALUES (%s, %s);" 
                cursor.execute(insert_query, (id_otgruzka, date))
                connection.commit()
        finally:
            connection.close()
    except Exception as ex :
        print("Не подключилось")
        print(ex)

def getOtgruzkassss() :
    try :
        connection = pymysql.connect(
            host=config.host, 
            port=3306,
            user=config.user,
            password=config.password,
            database=config.db_name,
            cursorclass=pymysql.cursors.DictCursor
        )
        print('Подключение состоялось getOtgruzkassss')
        try :
            with connection.cursor() as cursor :
                select_all_rows = "SELECT * FROM `otgruzka_moysklad`"
                cursor.execute(select_all_rows)
                otgruzka = cursor.fetchall()
                # for row in otgruzkaa :
                #     print(row)
        finally:
            connection.close()
    except Exception as ex :
        print("Не подключилось getWorkers.py")
        print(ex)

    return otgruzka