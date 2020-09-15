import sqlite3


class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS weather (id INTEGER PRIMARY KEY, code text, city text, temp text, speed text, date text, wet text)")
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM weather")
        '''self.cur.execute((
                         "  ORDER BY -AV.avspeed"
                         "  LIMIT 10")'''
        rows = self.cur.fetchall()
        return rows

    def insert(self, code, city, temp, speed, date, wet):
        self.cur.execute("INSERT INTO weather(code, city, temp, speed, date, wet) VALUES (?, ?,?,?,?,?)", (code, city, temp, speed, date, wet))
        self.conn.commit()

    def remove(self, id):
        self.cur.execute("DELETE FROM weather WHERE id=?", (id,))
        self.conn.commit()

    def update(self, id, code, city, temp, speed, date, wet):
        self.cur.execute("UPDATE weather SET code = ?, city = ?, temp = ?, speed = ?, date = ?, wet = ? WHERE id = ?",
                         (code, city, temp, speed, date, wet, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()

