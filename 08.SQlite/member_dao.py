# member table에 대한 Data Access Object(DAO)
import sqlite3 as sq

# member table에 있는 데이터 모두 읽기
def get_members():
    conn = sq.connect('testdb.db')
    cur = conn.cursor()

    sql = 'select * from member;'
    cur.execute(sql)
    rows = cur.fetchall()

    cur.close()
    conn.close()
    return rows

# 성별에 해당하는 데이터 가져오기
def get_members_by_gender(gender):
    conn = sq.connect('testdb.db')
    cur = conn.cursor()

    sql = 'select * from member where gender=?;'
    cur.execute(sql, (gender, ))        # 파라미터는 반드시 튜플로 적용, (gender, ) 부분이 파라미터
    rows = cur.fetchall()

    cur.close()
    conn.close()
    return rows

# mid에 해당하는 데이터(1개) 가져오기
def get_member_by_mid(mid):
    conn = sq.connect('testdb.db')
    cur = conn.cursor()

    sql = 'select * from member where mid=?;'
    cur.execute(sql, (mid, ))        # 파라미터는 반드시 튜플로 적용, (gender, ) 부분이 파라미터
    row = cur.fetchone()       # 단일 튜플 선택 시 fetchone 사용

    cur.close()
    conn.close()
    return row

# 데이터 추가
def insert_member(params):
    conn = sq.connect('testdb.db')
    cur = conn.cursor()

    sql = 'insert into member(mname, gender) values (?, ?)'
    cur.execute(sql, params)
    conn.commit()       # DB 내용을 변경하는 경우(CUD)에는 승인(저장) 해줘야 DB에 적용됨

    cur.close()
    conn.close()

# 데이터 수정
def update_member(params):
    conn = sq.connect('testdb.db')
    cur = conn.cursor()

    sql = 'update member set mname=?, gender=? where mid=?;'
    cur.execute(sql, params)
    conn.commit()       # DB 내용을 변경하는 경우(CUD)에는 승인(저장) 해줘야 DB에 적용됨

    cur.close()
    conn.close()

# 데이터 삭제
def delete_member(mid):
    conn = sq.connect('testdb.db')
    cur = conn.cursor()

    sql = 'delete from member where mid=?'
    cur.execute(sql, (mid,))
    conn.commit()       # DB 내용을 변경하는 경우(CUD)에는 승인(저장) 해줘야 DB에 적용됨

    cur.close()
    conn.close()