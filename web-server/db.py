import cx_Oracle as oracle
import math

class DB:
    def __init__(self):
        self.con = oracle.connect('admin/qwerty123@team.cltj4pcb9vnc.ap-northeast-2.rds.amazonaws.com:1521/DATABASE')
        self.cur = self.con.cursor()
    
    def volume_insert(self, x, y, filename, date, stonetype)
        self.cur.execute("insert into info(width, height, volume, img, distance, time,type) values({}, {}, {}, '{}', {}, '{}','{}')".format(x, y, math.pi*(x/2)**2/3, filename, 35, date, stonetype))
        self.con.commit()

    def count_insert(self, x, y, date):
        self.cur.execute("insert into info2(width, height, count, time) values({}, {}, {}, '{}')".format(x, y, y/0.3 ,date))
        self.con.commit()

    def close(self):
        self.con.close()