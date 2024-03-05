import mysql.connector

cnx = mysql.connector.connect(user ='root', password= '',port='8800', database='person')
cursor = cnx.cursor()


cursor.execute("""CREATE TABLE doctors (
                    id_nezam INT(12) AUTO_INCREMENT PRIMARY KEY, 
                    age INT, 
                    phone_number INT, 
                    office_name VARCHAR(255), 
                    first_name VARCHAR(255), 
                    last_name VARCHAR(255),
                    address VARCHAR(255), 
                    gender VARCHAR(255))""")


def add_row(table_name, tuple_row):
    sql_add = f"INSERT INTO {table_name} (id_nezam, age, phone_number, office_name, first_name, last_name, address, gender) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    val = tuple_row

    p_id = val[0]
    cursor.execute(f"SELECT id_nezam, COUNT(*) FROM {table_name} WHERE id_nezam = %s",(p_id,))
    results = cursor.fetchall()
    if results[0][1]>0:
        print('کاربر موجود است')
    else:
        cursor.execute(sql_add, val)
        cnx.commit()


def del_row(table_name, tuple_row):
    p_id = tuple_row[0]
    sql_delete = f"DELETE FROM {table_name} WHERE id_nezam = {p_id}"
    cursor.execute(sql_delete)
    cnx.commit()

def update_row(table_name, tuple_row, s_column, new_value):
    p_id = tuple_row[0]
    cursor.execute(f"SHOW columns FROM {table_name}")
    table_columns = [column[0] for column in cursor.fetchall()]
    indexes = list(range(len(table_columns)))
    dict_columns = dict(zip(table_columns,indexes))
    sql = f"UPDATE {table_name} SET {s_column} = '{new_value}' WHERE {s_column} = '{tuple_row[dict_columns[s_column]]}' AND id_nezam = {p_id}"
    cursor.execute(sql)
    cnx.commit()