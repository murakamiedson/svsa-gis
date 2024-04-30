"""Módulo responsável pela migração dos dados originais do MySQL, junto com os dados georreferenciados que foram adicionados,
para o banco de dados PostGIS.
 """
import json
import psycopg2

def mysql_to_postgis(mysql_data):
    data_dict = mysql_data.to_dict(orient='records')

    with open("config.json", "r") as file:
        config = json.load(file)

    conn = psycopg2.connect(
        dbname=config["database"],
        user=config["user"],
        password=config["password"],
        host=config["host"]
    )
    cur = conn.cursor()

    columns = ", ".join(mysql_data.columns)
    placeholders = ", ".join(["%s"] * len(mysql_data.columns))
    sql = f"INSERT INTO my_table ({columns}) VALUES ({placeholders});"
    for row in data_dict:
        cur.execute(sql, list(row.values()))

    conn.commit()
    cur.close()
    conn.close()