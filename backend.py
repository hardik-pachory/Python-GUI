import sqlite3
def connect():
    conn = sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS routine(Id INTEGER PRIMARY KEY,date text,earnings integer,exercise text,study text, diet text,python text)")
    conn.commit()
    conn.close()

def insert(date, earings, exercise, study, diet, python):
    conn = sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO routine VALUES(NULL, ?, ?, ?, ?, ?, ?)",(date,earings,exercise,study,diet,python))
    conn.commit()
    conn.close()
#insert("5 Jan 2021",200,'Pullups','Django-SQLITE3','Pani Puri','QT5')
def view():
    conn = sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM routine")
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

def delete(id):
    conn = sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM routine WHERE Id=?",(id,))
    conn.commit()
    conn.close()

def search(date='', earings='', exercise='', study='', diet='', python=''):
    conn = sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM routine WHERE date=? OR earnings=? OR exercise=? OR study=? OR diet=? OR python=?",(date,earings,exercise,study,diet,python))
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows
#print(search("5 Jan 2021",200,'Pushups'))

v =view()
for vie in v:
    print(vie)

delete(4)