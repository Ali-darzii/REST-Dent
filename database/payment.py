import mysql.connector

cnx = mysql.connector.connect(user ='root', password= '',port='8800', database='person')
cursor = cnx.cursor()

cursor.execute("""CREATE TABLE payment (
                    person_id INT, 
                    number INT, 
                    amount INT,
                    service VARCHAR(255), 
                    first_name VARCHAR(255), 
                    last_name VARCHAR(255),
                    Payment_method VARCHAR(255),
                    Activity_Date DATE,
                    Payment_Date DATE,
                    Payment_time TIME
                    )""")


def add_row(table_name, tuple_row):
    sql_add = f"INSERT INTO {table_name} (person_id, age, number, service, first_name, last_name, address, gender) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    val = tuple_row

    p_id = val[0]
    cursor.execute(f"SELECT person_id, COUNT(*) FROM {table_name} WHERE person_id = %s",(p_id,))
    results = cursor.fetchall()
    if results[0][1]>0:
        print('کاربر موجود است')
    else:
        cursor.execute(sql_add, val)
        cnx.commit()


def del_row(table_name, tuple_row):
    p_id = tuple_row[0]
    sql_delete = f"DELETE FROM {table_name} WHERE person_id = {p_id}"
    cursor.execute(sql_delete)
    cnx.commit()

def update_row(table_name, tuple_row, s_column, new_value):
    p_id = tuple_row[0]
    cursor.execute(f"SHOW columns FROM {table_name}")
    table_columns = [column[0] for column in cursor.fetchall()]
    indexes = list(range(len(table_columns)))
    dict_columns = dict(zip(table_columns,indexes))
    sql = f"UPDATE {table_name} SET {s_column} = '{new_value}' WHERE {s_column} = '{tuple_row[dict_columns[s_column]]}' AND person_id = {p_id}"
    cursor.execute(sql)
    cnx.commit()