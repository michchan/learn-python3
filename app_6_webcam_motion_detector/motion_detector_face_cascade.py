import cv2, time

# * Remember to include the xml file under the same directory!
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

def get_faces(frame):
    faces = face_cascade.detectMultiScale(frame,
        # scaleFactor: 1.1 -> Decrease 10% for the scale of the image for each face search
        #              smaller is more accurate, but might be too sensitive also
        scaleFactor=1.1,
        minNeighbors=5)
    return faces 

# Draw the rectangle to the image for faces
def draw_faces_rect(frame, faces):
    for x, y, w, h in faces:
        frame = cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 3)

def detect_frame(cap):
    ret, frame = cap.read()
    if ret == True:
        faces = get_faces(frame)
        draw_faces_rect(frame, faces)  
        cv2.imshow("Motion Detector", frame)

def main():
    cap = cv2.VideoCapture(0)
    while True:
        detect_frame(cap)
        # Make it 60 fps
        key = cv2.waitKey(int(1000 / 60))
        # Wait for "q" key to escape
        if key == ord("q"): break
    cap.release()
    cv2.destroyAllWindows()

main()