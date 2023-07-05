# World database의 song, girl_group을 액세스하는 라이브러리
# Connection Pool 사용
# 설치 : pip install mysql-connector-python

import json
from mysql.connector import pooling
import pymysql

with open('./mysql.json') as f:
    config_str = f.read()
config = json.loads(config_str)
pool = pooling.MySQLConnectionPool(pool_name="mypool", pool_size=3, **config)

def insert_song(params):
    conn = pool.get_connection()
    cur = conn.cursor()
    sql = "INSERT INTO song VALUES (DEFAULT, %s, %s);" 
    cur.execute(sql, params)      
    conn.commit()
    cur.close()
    conn.close()

def insert_girl_group(params):
    conn = pool.get_connection()
    cur = conn.cursor()
    sql = "INSERT INTO girl_group VALUES (DEFAULT, %s, %s, %s);" 
    cur.execute(sql, params)      
    conn.commit()
    cur.close()
    conn.close()

def get_song_list_by_debut(year):
    conn = pool.get_connection()
    cur = conn.cursor()
    sql = "SELECT l.name, debut, title FROM girl_group AS l JOIN song AS r ON l.gid=r.sid WHERE debut BETWEEN DATE('%s-01-01') AND DATE('%s-12-31') ORDER BY debut;"
    cur.execute(sql, (year, year))
    rows = cur.fetchall()
    cur.close()
    conn.close()
    
    return rows