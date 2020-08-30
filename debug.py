import sqlite3
conn = sqlite3.connect('football.db')
c = conn.cursor()
c.execute('select id from league where name=? and season=?', ("Premier League",'2018',))
for row in c:
    print(row)
conn.close()