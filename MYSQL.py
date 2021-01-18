import mysql.connector as m


class main:
    db = m.connect(user="user", password="password", host="localhost", autocommit=True)
    try:
        cur = db.cursor()
        cur.execute("CREATE DATABASE IF NOT EXISTS test")
        cur.execute("USE test")
        cur.execute("CREATE TABLE IF NOT EXISTS test(name VARCHAR(50), no INT(10) PRIMARY KEY)")
    except Exception as e:
        print(e)
    finally:
        cur.close()
        
    def __str__():
        return "Database"
    

    def add(cls, name, no):
        cur = cls.db.cursor()
        try:
            cur.execute("INSERT INTO test VALUES ('%s', %d)", (name, no))
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

    @classmethod
    def update(cls, roll, name):
        try:
            cur = cls.db.cursor()
            cur.execute("USE test")
            cur.execute("UPDATE test SET name='%s' WHERE no=%d"%(name, roll))
        except Exception as e:
            print(e)
        finally:
            cur.close()

    @classmethod
    def closedb(cls):
        cls.db.close()
                
if __name__ == "__main__":
    try:
        print(main.read())
    except Exception as e:
        print(e)
    finally:
        main().closedb()