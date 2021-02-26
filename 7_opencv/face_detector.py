import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

img = cv2.imread("photo.jpg")

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray_img,
    # scaleFactor: 1.05 -> Decrease 5% for the scale of the image for each face search
    #              smaller is more accurate, but might be too sensitive also
    scaleFactor=1.05,
    minNeighbors=5)

print(faces)

# Draw the rectangle to the image for faces
for x, y, w, h in faces:
    img = cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), 3)

resized = cv2.resize(img, (int(img.shape[1] / 2), int(img.shape[0] / 2)))

cv2.imshow("Gray", img)
cv2.waitKey(0)
cv2.destroyAllWindows()