import webview
import uuid
import mysql.connector as sql
db = sql.connect(host="localhost",user="root",password="2005",database="meeting")
cursor = db.cursor()
class api():
    def display(self):
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

    def search(self,title):
        try:
            cursor.execute("select * from meetings where title='{}' group by date".format(title))
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
    
        
    
        

    def update(self,id,title,date,time):
        try:
            print("Meeting updated!")
            cursor.execute("update meetings set title='{}',date='{}',time='{}' where id='{}'".format(title,date,time,id))
            db.commit()
        except Exception as e:
               print(e)

    def delete(self,id):
        try:
            print("Meeting Deleted")
            cursor.execute("delete from meetings where id='{}'".format(id))
            db.commit()
            
        except Exception as e:
               print(e)

    def addmeet(title,date,time):
        try:
            id = uuid.uuid4()
            cursor.execute("insert into meetings values('{}','{}','{}','{}')".format(title,date,time,id))
            db.commit()
            
           except Exception as e:
               print(e)
            
        
api = api()
ht = ''
with open('inshal.html', 'r') as f:
    ht = str(f.read())
window = webview.create_window('Computer Project', html=ht, js_api=api)
webview.start(debug=True)
