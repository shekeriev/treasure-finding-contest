import os
import mysql.connector
import random
import time

a = ['Fat', 'Slim', 'Fast', 'Slow', 'Tall', 'Short', 'Weak', 'Strong']
b = ['Tigers', 'Lions', 'Crocodiles', 'Horses', 'Donkeys', 'Dogs', 'Cats', 'Bears', 'Pandas', 'Coalas', 'Chameleons', 'Lizards']
c = ['Blue', 'Black', 'Yellow', 'White', 'Green', 'Orange', 'Purple', 'Pink', 'Brown', 'Gray', 'Red']
d = ['Oranges', 'Bananas', 'Tomatoes', 'Potatoes', 'Onions', 'Cucumbers', 'Nuts']

print('Started. Waiting for new events ...')

while True:
    s = a[random.randrange(7)] + ' ' + b[random.randrange(11)] + ' Found ' + str(random.randrange(2,20)) + ' ' + c[random.randrange(10)] + ' ' + d[random.randrange(6)]

    print(f'New event captured: {s}')

    try:
      mydb = mysql.connector.connect(
        host = os.getenv('DB_HOST', 'con-database'),
        user = os.getenv('DB_USER', 'root'),
        password = os.getenv('DB_PASS', 'ExamPa$$w0rd'),
        database = os.getenv('DB_NAME', 'game_events')
      )
      cursor = mydb.cursor()
      cursor.execute("INSERT INTO events (event) VALUES ('" + s + "')")
      cursor.close()
      mydb.commit()
    except:
      print('ERROR: Database communication error.')

    t = random.randrange(60,90)
    print(f'Sleep for {t} seconds')
    time.sleep(t)
