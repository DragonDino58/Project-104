import cv2 

img = cv2.imread("solar-system.jpg")


cv2.putText(img, "Sun.", (20, 300), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 255, 255), 3)

cv2.putText(img, "Mercury.", (100, 200), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1)

cv2.putText(img, "Venus.", (200, 250), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1)

cv2.putText(img, "Earth.", (290, 160), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1)

cv2.putText(img, "Mars.", (380, 250), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1)

cv2.putText(img, "Jupiter.", (500, 250), cv2.FONT_HERSHEY_COMPLEX, 1.4, (255, 255, 255), 2)

cv2.putText(img, "Saturn.", (750, 250), cv2.FONT_HERSHEY_COMPLEX, 1.2, (255, 255, 255), 2)

cv2.putText(img, "Uranus.", (950, 300), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)

cv2.putText(img, "Neptune.", (1100, 150), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)

cv2.imshow("output",img)

cv2.waitKey(0)


