import webview
import uuid
import mysql.connector as sql
import sched, time
from win10toast import ToastNotifier

class api():
    global db,cursor
    db = sql.connect(host="localhost",user="root",password="2005",database="meeting")
    cursor = db.cursor()
    def display(self):
        global db,cursor
        try:
            cursor.execute("select * from meetings group by date")
            results= cursor.fetchall()
            html =""
            if len(results)!=0:
                for i in results:
                    html+='''
                    <div class="meeting">
                        <div class="body">
                            <h3 class="title" id="title-{}" contenteditable="true">{}</h3>
                            <p class="date" id="date-{}"  contenteditable="true">{}</p>
                            <p class="time" id="time-{}"  contenteditable="true">{}</p>
                        </div>

                        <div class="btn">
                            <button onclick="update('{}','{}','{}','{}')">Update</button>
                            <button onclick="deleted('{}')">Cancel</button>
                        </div>
                        <center><hr size="2" style="width: 95%;margin-top: 10px;"></center>
                
                    
                    </div>
                
                '''.format(i[3],i[0],i[3],i[1],i[3],i[2],i[3],i[0],i[1],i[2],i[3])

            return html
        except Exception as e:
            print(e)

    def search(self,title):
        global db,cursor
        print(title)
        try:
            q="select * from meetings where title like '{}%' group by date".format(title)
            print(q)
            cursor.execute(q)
            results= cursor.fetchall()
            print(results)
            html =""
            if len(results)!=0:
                for i in results:
                    html+='''
                    <div class="meeting">
                        <div class="body">
                            <h3 class="title" id="title-{}" contenteditable="true">{}</h3>
                            <p class="date" id="date-{}"  contenteditable="true">{}</p>
                            <p class="time" id="time-{}"  contenteditable="true">{}</p>
                        </div>

                        <div class="btn">
                            <button onclick="update('{}','{}','{}','{}')">Update</button>
                            <button onclick="deleted('{}')">Cancel</button>
                        </div>
                        <center><hr size="2" style="width: 95%;margin-top: 10px;"></center>
                
                    
                    </div>
                
                '''.format(i[3],i[0],i[3],i[1],i[3],i[2],i[3],i[0],i[1],i[2],i[3])

            return html
    
        except Exception as e:
            print(e)
    
        

    def update(self,id,title,date,time):
        global db,cursor
        try:
            print(id,time,date,title)
            cursor.execute("update meetings set title='{}',date='{}',time='{}' where id='{}'".format(title,date,time,id))
            db.commit()
        except Exception as e:
            print(e)

    def delete(self,id):
        global db,cursor
        try:
            print("Meeting Deleted")
            cursor.execute("delete from meetings where id='{}'".format(id))
            db.commit()
            
        except Exception as e:
            print(e)

    def addmeet(title,date,time):
        global db,cursor
        try:
            id = uuid.uuid4()
            cursor.execute("insert into meetings values('{}','{}','{}','{}')".format(title,date,time,id))
            db.commit()
            
        except Exception as e:
            print(e)
    s = sched.scheduler(time.time, time.sleep)
    def check_time(sc): 
        mycursor.execute("select * from meetings")
        d=mycursor.fetchall()
        for i in d:

        sc.enter(60, 1, check_time, (sc,))
    sc.enter(60, 1, check_time, (sc,))

s.enter(60, 1, do_something, (s,))
s.run()
            
        
api = api()
ht = ''
with open('inshal.html', 'r') as f:
    ht = str(f.read())
window = webview.create_window('Computer Project', html=ht, js_api=api)
webview.start(debug=True)
