import pytesseract
import cv2

yol = "C:\\Users\\ASUS\\Desktop\\test5.png"

pytesseract.pytesseract.tesseract_cmd = "C:\\Users\\ASUS\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe"

resim = cv2.imread(yol)

metin = pytesseract.image_to_string(resim)

print(metin)
print("okuma yapıldı")
print("----------------------")
if (metin == ""):
    print("resimde yazı yoktur")
elif (metin == " "):
    print("resimde yazı yoktur 22 ")
else:
    print("metinde yazı var")
cv2.imshow("resim", resim)
cv2.waitKey(0)
