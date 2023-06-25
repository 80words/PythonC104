import cv2 

img = cv2.imread("solar-system.jpg") 


cv2.putText(img, "Sun", (20, 300), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0))

cv2.putText(img, "Mercury", (100, 200), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0))

cv2.putText(img, "Venus", (200, 200), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0))

cv2.putText(img, "Earth", (280, 200), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0))

cv2.putText(img, "Mars", (360, 200), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0))

cv2.putText(img, "Jupiter", (600, 200), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0))

cv2.putText(img, "Saturn", (800, 200), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0))

cv2.putText(img, "Uranus", (950, 150), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0))

cv2.putText(img, "Neptune", (1100, 200), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0))

cv2.imshow("Output", img) 
cv2.imwrite("labeled-planets.jpg",img)
cv2.waitKey(4000)