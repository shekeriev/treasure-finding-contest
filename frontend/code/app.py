import os
import time
import mysql.connector
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
  with open('app.tpl') as f:
    template = f.read()

  result = template.replace('{TITLE}', 'Treasure Finding Contest')

  events = ''

  db_host = os.getenv('DB_HOST', 'con-database')
  db_user = os.getenv('DB_USER', 'root')
  db_pass = os.getenv('DB_PASS', 'ExamPa$$w0rd')
  db_name = os.getenv('DB_NAME', 'game_events')

  try:
    mydb = mysql.connector.connect(
      host = db_host,
      user = db_user,
      password = db_pass,
      database = db_name
    )
    cursor = mydb.cursor()
  
    cursor.execute("SELECT CONCAT('<li>', event, '</li>') html_event FROM events ORDER BY id DESC LIMIT 10")
  
    records = cursor.fetchall()
 
    if cursor.rowcount == 0:
      events = 'No data found yet.'

    for row in records:
      events = events + row[0]
  
    cursor.close()
  except:
    events = 'Error: Something happened while trying to talk to the database.'

  result = result.replace('{EVENTS}', events)

  with open('app.dat') as f:
    build = f.read()

  build = build + ' / Refreshed on: ' + time.strftime("%Y.%m.%d %H:%M:%S")

  result = result.replace('{BUILD}', build)

  return result
