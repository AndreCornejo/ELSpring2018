import sqlite3
  from bottle import route, run, template



 host = '169.254.173.16'
 db = sqlite3.connect('/home/pi/Desktop/DB/templog.db')
 c = db.cursor()

 @route('/')
 def index():


    response = "<head><meta http-equiv='refresh' content='5'></head>"

    c.execute("SELECT * FROM templog.db")
    data = c.fetchall()
    response += template('/home/pi/Desktop/DB/blind_logs.tpl', rows=data)

    return response
    run(host=host, port=86)
