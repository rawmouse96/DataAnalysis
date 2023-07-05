# World DB를 Access하는 library
import json
import pymysql

with open('./mysql.json') as f:
    config_str = f.read()
config = json.loads(config_str)

# 어떤 국가의 인구수 Top n개 도시 정보
def get_citylist_by_country(countrycode, num):
    conn = pymysql.connect(**config)
    cur = conn.cursor()
    sql = "SELECT * FROM city WHERE countrycode=%s ORDER BY population DESC LIMIT %s;"
    cur.execute(sql, (countrycode, num))
    rows = cur.fetchall()
    cur.close()
    conn.close()
    
    return rows

# 어떤 도시의 정보를 이름으로 불러오기
def get_city_by_name(name):
    conn = pymysql.connect(**config)
    cur = conn.cursor()
    sql = "SELECT * FROM city WHERE name=%s;"
    cur.execute(sql, (name, ))      
    row = cur.fetchone()
    cur.close()
    conn.close()

    return row

# 데이터 삽입
def insert_city(params):
    conn = pymysql.connect(**config)
    cur = conn.cursor()
    sql = "INSERT INTO city VALUES (DEFAULT, %s, %s, %s, %s);" 
    cur.execute(sql, params)      
    conn.commit()
    cur.close()
    conn.close()
    
# 데이터 수정
def update_city(params):
    conn = pymysql.connect(**config)
    cur = conn.cursor()
    sql = "UPDATE city SET name=%s, countrycode=%s, district=%s, population=%s WHERE id=%s;"
    cur.execute(sql, params)      
    conn.commit()
    cur.close()
    conn.close()
    
# 데이터 삭제
def delete_city(id):
    conn = pymysql.connect(**config)
    cur = conn.cursor()
    sql = "DELETE FROM city WHERE id=%s;"
    cur.execute(sql, (id, ))      
    conn.commit()
    cur.close()
    conn.close()