import mysql.connector as m


class main:
    db = m.connect(user="user", password="password", host="localhost", autocommit=True)
    def __init__(self):
        self.db = cls.db
        self.curf = lambda: self.db.cursor()
        try:
            cur = self.curf()
            cur.execute("CREATE DATABASE IF NOT EXISTS test")
            cur.execute("USE test")
            cur.execute("CREATE TABLE IF NOT EXISTS test(name VARCHAR(50), no INT(10) PRIMARY KEY)")
        except Exception as e:
            print(e)
        finally:
            cur.close()
        
    def __str__(self):
        return "Database"
    
    def add(self, name, no):
        cur = self.curf()
        try:
            cur.execute("INSERT INTO test VALUES ('%s', %d)"%(name, no))
        except Exception as e:
            print(e)
        finally:
            cur.close()

    @classmethod
    def read(cls, no=None):
        try:
            cur = cls.db.cursor()
            cur.execute("USE test")
            if no:
                cur.execute("SELECT * FROM test WHERE no=%d"%no)
            else:
                cur.execute("SELECT * FROM test")
            return cur.fetchall()
        except Exception as e:
            print(e)
        finally:
            cur.close()
        
    @classmethod
    def delete(cls, no=None):
        try:
            cur = cls.db.cursor()
            cur.execute("USE test")
            if no:
                cur.execute("DELETE FROM test WHERE no=%d"%no)
            else:
                cur.execute("DELETE FROM test")
##    def update(self, roll, name=None):
        

if __name__ == "__main__":
    print(main.read())
    
    
        
