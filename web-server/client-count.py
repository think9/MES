import cv2
from analysis import Analysis
from db import DB
import datetime
import os
import time
import math

print "Client start.."

analysis = Analysis()
db = DB()

while True:
    if os.path.exists('./img/frame.png'):
	time.sleep(2)
        print "Image processing.. "
	date_ = datetime.datetime.now() + datetime.timedelta(hours=9)
        date = str(date_).split('.')[0]
        filename = date + '.png'
        os.rename('./img/frame.png', './img/' + filename)

        frame = cv2.imread('./img/' + filename, 0)
        x, y, test = analysis.process(frame, 90, 43, 18.2)
	cv2.imwrite('./img/test.png', test)
        db.count_insert(x, y, date)
        print "Done!"
    else:
	print "Waiting.."
        time.sleep(1)


print "Client close.."
