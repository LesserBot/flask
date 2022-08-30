from main import app
import time
import schedule
from flask import Flask, render_template
import pymysql

conn = pymysql.connect(host="localhost", user="root", \
                       password="krg0318",db="data",charset="utf8")
curs = conn.cursor()

topics = [
    {'id':1, 'title':'등록된 운송장 정보','body':''},
    {'id':2, 'title':'분류된 정보','body':''},
    {'id':3, 'title':'현황 전체 보기','body':''},
]

def getContents():
    litag= ''
    for topic in topics:
        litag=litag + f'''<li><a href="/datas/{topic["id"]}">{topic["title"]}</a></li>
        '''
    return litag   

     
def template2(head,contents, content):
    return f'''<!doctype html>
    <html lang="en">
    <head >
        <title>정보 표시 화면</title>
        {head}
    </head>
        <body>
            <ol>
                {contents}              
            </ol>             
            {content}
        </body>
    </html>
    '''
    
def reloads1():
    curs.execute("select * from datas")
    data1= curs.fetchall()
    curs.execute("select * from input")
    data2= curs.fetchall()
    return render_template("id1.html",value=data1)
    
def reloads2():
    curs.execute("select * from datas")
    data1= curs.fetchall()
    curs.execute("select * from input")
    data2= curs.fetchall()
    return render_template("id2.html",value=data1)

def reloads3():
    curs.execute("select * from datas")
    data1= curs.fetchall()
    curs.execute("select * from input")
    data2= curs.fetchall()
    return render_template("id3.html",value=data1,value2= data2)
    
schedule.every(5).seconds.do(reloads1)
schedule.every(5).seconds.do(reloads2)
schedule.every(5).seconds.do(reloads3)

while True:
    schedule.run_pending()
    time.sleep(1)


