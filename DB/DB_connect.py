import psycopg2

def connect_DB():

    conn = psycopg2.connect(dbname='statick', user='postgres',
                        password='Potok-DU', host='192.168.56.102')
    return conn
def Sel_OPO(guid_opo):
    sql = 'SELECT t.* FROM public.ref_opo t where t.guid = ' + "'" + str(guid_opo) + "'"
    connect = connect_DB()
    cursor = connect.cursor()
    cursor.execute(sql)
    for row in cursor:
     return row
# Выбор объекта для занесения в НСИ
def sel_obj(guid_opo):
    sql = 'SELECT o.* FROM public.ref_obj o where o."idOPO" = (SELECT t."idOPO" FROM public.ref_opo t where t.guid = '\
          + "'" + str(guid_opo) + "')" + 'order by o."idObj" asc  LIMIT 1'
    connect = connect_DB()
    cursor = connect.cursor()
    cursor.execute(sql)
    for row in cursor:
        return row
# Выбор последнего ИП по ОПО
def sel_opo_Roib(guid_opo):
    sql = 'SELECT i.ip_opo, i.date::timestamptz FROM public.calc_ip_opoi i where i.from_opo'\
     '= (SELECT t."idOPO" FROM public.ref_opo t where t.guid = ' \
          + "'" + str(guid_opo) + "')" + 'order by date desc  LIMIT 1'
    connect = connect_DB()
    cursor = connect.cursor()
    cursor.execute(sql)
    for row in cursor:
        return row
# Выбор последнего События С-1 С-2
def sel_AE(guid_opo):
    sql = 'SELECT i.level, i.data::timestamptz, i.name FROM public.jas_1 i where i.from_opo'\
     '= (SELECT t."idOPO" FROM public.ref_opo t where t.guid = ' \
          + "'" + str(guid_opo) + "')" + 'order by i.data desc LIMIT 1'
    connect = connect_DB()
    cursor = connect.cursor()
    cursor.execute(sql)
    for row in cursor:
        return row

# Выбор Технологические блоки
def sel_TB():
    sql = 'select oto."descOTO", oto.guid from public.ref_oto oto'\
    ' order by oto."idOTO"'\
        'limit 1'
    connect = connect_DB()
    cursor = connect.cursor()
    cursor.execute(sql)
    for row in cursor:
        return row

# Выбор Технологические установки
def sel_TU():
    sql = 'select oto."descOTO", oto.guid from public.ref_oto oto'\
    ' order by oto."idOTO"'\
        'limit 1'
    connect = connect_DB()
    cursor = connect.cursor()
    cursor.execute(sql)
    for row in cursor:
        return row