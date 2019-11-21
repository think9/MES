import cv2
import numpy as np

img = cv2.imread("1.jpg")
img = cv2.GaussianBlur(img, (3, 3), 0)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ml = cv2.imread("./client-book/ml.jpg", 0)
md = cv2.imread("./client-book/md.jpg", 0)
do = cv2.imread("./client-book/do.jpg", 0)
logos = [ml, md, do]

area = (200, 160, 54)
num = 0

for logo in logos:
    w, h = logo.shape[::-1]
    res = cv2.matchTemplate(img_gray, logo, cv2.TM_CCOEFF_NORMED)
    threshold = 0.5525
    loc = np.where(res >= threshold)
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), area, 2)

    mask = cv2.inRange(img, area, area)

    img2, contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    
    title=""
    if logo is ml:
        title = "머신러닝 탐구생활"
    elif logo is md:
        title = "모두의 딥러닝"
    elif logo is do:
        title = "가장 빨리 만나는 Docker"
    
    print(title + " : " + str(len(contours) - num) + "권")
    num = len(contours)

cv2.imshow("result", img)

cv2.waitKey(0)
cv2.destroyAllWindows()