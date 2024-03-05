import mysql.connector

cnx = mysql.connector.connect(user ='root', password= '',port='8800', database='person')
cursor = cnx.cursor()

cursor.execute("""CREATE TABLE payment (
                    seller_pnumber INT, 
                    amount INT, 
                    price INT,
                    paid_amount INT,
                    product_name VARCHAR(255), 
                    category VARCHAR(255), 
                    seller VARCHAR(255),
                    Payment_method VARCHAR(255),
                    EXP_DATE DATE,
                    Purchase_Date DATE,
                    Payment_Date DATE
                    )""")


def add_row(table_name, tuple_row):
    sql_add = f"""INSERT INTO {table_name} 
                (seller_pnumber, 
                amount, 
                price,
                paid_amount,
                product_name, 
                category, 
                seller,
                Payment_method,
                EXP_DATE ,
                Purchase_Date ,
                Payment_Date) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    cursor.execute(sql_add, tuple_row)
    cnx.commit()


def del_row(table_name, tuple_row):
    p_id = tuple_row[0]
    sql_delete = f"DELETE FROM {table_name} WHERE product_name = {p_id}"
    cursor.execute(sql_delete)
    cnx.commit()

def update_row(table_name, tuple_row, s_column, new_value):
    p_id = tuple_row[0]
    cursor.execute(f"SHOW columns FROM {table_name}")
    table_columns = [column[0] for column in cursor.fetchall()]
    indexes = list(range(len(table_columns)))
    dict_columns = dict(zip(table_columns,indexes))
    sql = f"UPDATE {table_name} SET {s_column} = '{new_value}' WHERE {s_column} = '{tuple_row[dict_columns[s_column]]}' AND product_name = {p_id}"
    cursor.execute(sql)
    cnx.commit()