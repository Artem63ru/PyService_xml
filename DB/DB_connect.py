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
 # records = cursor.fetchall()
    for row in cursor:
     return row

def sel_obj(guid_opo):
    sql = 'SELECT o.* FROM public.ref_obj o where o."idOPO" = (SELECT t."idOPO" FROM public.ref_opo t where t.guid = '  + "'" + str(guid_opo) + "')" + 'order by o."idObj" asc  LIMIT 1'
    connect = connect_DB()
    cursor = connect.cursor()
    cursor.execute(sql)
    # records = cursor.fetchall()
    for row in cursor:
        return row
