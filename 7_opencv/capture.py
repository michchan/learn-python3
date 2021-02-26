import cv2, time

# 0 : first camera
# Can also pass video file name like "movie.mp4"
video = cv2.VideoCapture(0)

num_frame = 0

while True:
    num_frame = num_frame + 1
    check, frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # time.sleep(3) 

    cv2.imshow("Capturing", gray)
    
    # Make it 60 fps
    key = cv2.waitKey(int(1000 / 60))
    if key == ord("q"): break

print(num_frame)

video.release()
cv2.destroyAllWindows()

