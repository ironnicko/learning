import mysql.connector as m


class main:
    db = m.connect(user="user", password="password", host="localhost", autocommit=True) # adding auto-commit reduces the burden of committing all the time
    def __init__(self):
        self.db = cls.db
        self.curf = lambda: self.db.cursor() # this make the job of closing cursors
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
        except Exception as e:
            print(e)

        finally:
            cur.close()
            
    def update(self, roll):
        try:
            cur = self.curf()
            cur.execute("UPDATE test SET name=%s)", input("Enter the name to be updated to:"))
        except Exception as e:
            print(e)
        finally:
            cur.close()

if __name__ == "__main__":
    try:
        data = main()
        data.read()
    except Exception as e:
        print(e)
    finally:
        main.db.close()
    
    
    
        
