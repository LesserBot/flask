# cd flask 
# cd Scripts
# .\activate

import pymysql
from flask import Flask, render_template
import threading
import time

data1=''
data2=''

app = Flask(__name__)
# DB연동
conn = pymysql.connect(host="localhost", user="root", \
                       password="krg0318",db="data",charset="utf8")
curs = conn.cursor()

topics = [
    {'id':1, 'title':'등록된 운송장 정보','body':''},
    {'id':2, 'title':'분류된 정보','body':''},
    {'id':3, 'title':'현황 전체 보기','body':''},
]
def template(head,content1,contents, content2):
    return f'''<!doctype html>
    <html lang="en">
    <head>
        <title>삑 그리고 다음 팀</title>
        {head}
    </head>
        <body>
            {content1}
            <ol>
                {contents}
            </ol>
            {content2}
        </body>
    </html>
    '''
    
    
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
def getContents():
    litag= ''
    for topic in topics:
        litag=litag + f'''<li><a href="/datas/{topic["id"]}">{topic["title"]}</a></li>
        '''
    return litag   

     
@app.route('/')
def index():
    return template(render_template("home.html"),render_template("homelink.html"),getContents(), render_template("contents.html") )

        
@app.route('/datas/<int:id>/')
def create(id):
    if id == 1:
        site = "id1.html"
        curs.execute("select * from datas")
        data1= curs.fetchall()
        data2= ''

    elif id == 2:
        site = "id2.html"  
        curs.execute("select * from input")
        data1= curs.fetchall()
        data2= ''

    else:
        site = "id3.html"
        curs.execute("select * from datas")
        data2= curs.fetchall()
        curs.execute("select * from input")
        data1= curs.fetchall()

    return template2(render_template("home2.html"),getContents(),render_template(site, value=data1 , value2=data2) )

      
    
# def flask_run():
#     app.run(host='0.0.0.0', port=9900, debug=True)  

######### 쓰레드 제어 
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9900, debug=True)  
    # thread1= threading.Thread(target=flask_run)
    # # #thread= threading.Thread(target=abd)
    # # #thread.start()
    # /thread1.start()


    


    