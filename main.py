import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
img = cv2.imread('1.png')
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
#字符的识别
text = pytesseract.image_to_string(img,lang='chi_sim')
#字符的标定
boxes = pytesseract.image_to_boxes(img,lang='chi_sim')
print(boxes)
cv2.imshow("text",img)
cv2.waitkey(0)
