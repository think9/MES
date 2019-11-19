import cv2
from analysis import Analysis
import cx_Oracle as oracle
import datetime
import os
import time
import math

print "Client start.."

analysis = Analysis()

con = oracle.connect('admin/qwerty123@team.cltj4pcb9vnc.ap-northeast-2.rds.amazonaws.com:1521/DATABASE')
cur = con.cursor()

while True:
    if os.path.exists('./img/frame.png'):
	time.sleep(2)
        print "Image processing.. "
	date_ = datetime.datetime.now() + datetime.timedelta(hours=9)
        date = str(date_).split('.')[0]
        filename = date + '.png'
        os.rename('./img/frame.png', './img/' + filename)

        frame = cv2.imread('./img/' + filename, 0)
        x, y, test,stonetype = analysis.process(frame, 90, 43, 18.2)
	print x, y
	cv2.imwrite('./img/test.png', test)
        cur.execute("insert into info(width, height, volume, img, distance, time,type) values({}, {}, {}, '{}', {}, '{}','{}')".format(x, y, math.pi*(x/2)**2/3, filename, 35, date,stonetype))
        con.commit()
        print "Done!"
    else:
	print "Waiting.."
        time.sleep(1)

con.close()
print "Client close.."
