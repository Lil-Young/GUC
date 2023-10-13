import flask
import pymysql
from pymongo import mongo_client

def get_cursor():
    # db 변수: mysql에 연결하기 위한 연결 객체
    db = pymysql.connect(
        host=host,
        port=port,
        user=user,
        passwd=pw,
        db='test',
        charset='utf8'
    )
    # cursor 변수: 연결 객체에서 커서를 가져옴. 커서는 sql 쿼리를 실행하고 데이터베이스와 상호작용함
    cursor = db.cursor()
    return cursor