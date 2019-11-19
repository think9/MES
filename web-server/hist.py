import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import cv2
import numpy as np
filename = "./img/2019-11-16 13:31:32.png"
frame = cv2.imread(filename, 0)
#frame = cv2.equalizeHist(frame)
hist = cv2.calcHist(images = [frame], channels = [0], mask = None, histSize = [256], ranges = [0, 256])
hist = hist.flatten()
plt.title(filename)
plt.plot(hist, color = 'r')
binX = np.arange(256)
plt.bar(binX, hist, width = 1, color = 'b')
print np.where(hist == hist.max())
plt.savefig("./img/hist.png")
