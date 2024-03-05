import mysql.connector

cnx = mysql.connector.connect(user ='root', password= '',port='8800', database='person')
cursor = cnx.cursor()



cursor.execute("""CREATE TABLE services(
                    service VARCHAR(255) AUTO_INCREMENT PRIMARY KEY, 
                    price INT""")


def add_row(table_name, tuple_row):
    sql_add = f"INSERT INTO {table_name} (service, price) VALUES (%s, %s)"
    val = tuple_row

    s_id = val[0]
    cursor.execute(f"SELECT service, COUNT(*) FROM {table_name} WHERE service = %s",(s_id,))
    results = cursor.fetchall()
    if results[0][1]>0:
        print('فعالیت مد نظر موجود است')
    else:
        cursor.execute(sql_add, val)
        cnx.commit()


def del_row(table_name, tuple_row):
    s_id = tuple_row[0]
    sql_delete = f"DELETE FROM {table_name} WHERE service = {s_id}"
    cursor.execute(sql_delete)
    cnx.commit()

def update_row(table_name, tuple_row, s_column, new_value):

    if s_column == 'service':
        sql = f"UPDATE {table_name} SET {s_column} = '{new_value}' WHERE {s_column} = {tuple_row[0]} AND price = {tuple_row[1]}"
    elif s_column == 'price':
        sql = f"UPDATE {table_name} SET {s_column} = '{new_value}' WHERE {s_column} = {tuple_row[1]} AND service = {tuple_row[0]}"
    cursor.execute(sql)
    cnx.commit()