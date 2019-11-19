import cv2
import numpy as np
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt

class Analysis:
    def __init__(self):
        print 'Analysis init'

    def process(self, frame, threshold, x_offset, y_offset):
        self.frame = frame
        img_gauss = cv2.GaussianBlur(self.frame, (5, 5), 0)
	hist = cv2.calcHist(images = [img_gauss], channels = [0], mask = None, histSize = [256], ranges = [0, 256])
	hist = hist.flatten()
	if sum(hist[40:60]) >= 100:
		print "stone"
		stonetype="stone"
	else:
		print "sand"
		stonetype="sand"
#	plt.title('brown')
#	plt.plot(hist, color = 'r')
#	binX = np.arange(256)
#	plt.bar(binX, hist, width = 1, color = 'b')
#	plt.savefig("./img/hist.png")

        ret, img_result = cv2.threshold(img_gauss, threshold, 255, cv2.THRESH_BINARY)
        result = cv2.bitwise_not(img_result)
        canny = cv2.Canny(result, 200, 255)
        #cv2.imshow('bitwise', result)

        len_y = self.frame.shape[0]
        len_x = self.frame.shape[1]

        x1, x2, y = getLineX(canny)
        #cv2.line(self.frame, (x1, y), (x2, y), (255, 0, 0), 3)
        x_length = round(x_offset * float(x2 - x1) / len_x, 1)
        #x_text = "x : " + str(x_length) + "cm"
        #cv2.putText(self.frame, x_text , (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

        y1, y2, x = getLineY(canny)
        #cv2.line(self.frame, (x, y1), (x, y2), (0, 0, 255), 3)
        y_length = round(y_offset * float(y2 - y1) / (len_y * 0.54), 1)
        #y_text = "y : " + str(y_length) + "cm"
        #cv2.putText(self.frame, y_text , (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

        return x_length, y_length, result,stonetype


def getLineX(img):
    check = True
    x_start = 0
    x_end = 0
    y_ = 0
    x1 = 0
    x2 = 0
    
    len_y = img.shape[0]
    len_x = img.shape[1]

    for y in range(len_y):
        for x in range(len_x):
            if img[y][x] == 255:
                if check:
                    x_start = x
                    check = False
                else:
                    x_end = x
                    check = True
                    if x_end - x_start > x2 - x1:
                        y_ = y
                        x2 = x_end
                        x1 = x_start
    
    return x1, x2, y_

def getLineY(img):
    check = True
    y_start = 0
    y_end = 0
    x_ = 0
    y1 = 0
    y2 = 0
    
    len_y = img.shape[0]
    len_x = img.shape[1]

    for x in range(len_x):
        for y in range(len_y):
            if img[y][x] == 255:
                if check:
                    y_start = y
                    check = False
                else:
                    y_end = y
                    check = True
                    if y_end - y_start > y2 - y1:
                        x_ = x
                        y2 = y_end
                        y1 = y_start
    
    return y1, y2, x_
