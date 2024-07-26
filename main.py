# there might be some bugs with the latest version of torch
# https://stackoverflow.com/questions/78786306/fbgemm-load-error-trying-to-use-pytorch-on-windows
# uninstall and reinstall all the stuff


#cannot read text properly when it not straight - ex: test2

# try:
import cv2
import easyocr
import matplotlib.pyplot as plt
# import torch

# read img
img_path = "./data/test4.jpg"

img = cv2.imread(img_path)

# instance text detector
reader = easyocr.Reader(['en'], gpu=False)

# detect text on img
text = reader.readtext(img)



for t in text:
    print(t)

    # print(t[0][0],t[0][2])
    bbox, name, per = t
    print(bbox)
    cv2.rectangle(img,bbox[0], bbox[2], (0,255,0),2)
    cv2.putText(img, name, bbox[0], cv2.FONT_HERSHEY_COMPLEX, 0.65, (255,0,0), 2)
print(type(img))

#When use matplotlib, remember to change from BGR to RGB
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img)
plt.show()
# cv2.imshow("img", img)
# cv2.waitKey(0)
# print(text)
# except Exception as error:
#     print("lol")


