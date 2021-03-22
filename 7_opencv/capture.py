import cv2, time

# 0 : first camera
# Can also pass video file name like "movie.mp4"
video = cv2.VideoCapture(0)

num_frame = 0

while True:
    num_frame = num_frame + 1
    # "ret" is a boolean indicating whether it has a return value.
    ret, frame = video.read()
    if ret == True:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # time.sleep(3) 
        cv2.imshow("Capturing", gray)
        
    # Make it 60 fps
    key = cv2.waitKey(int(1000 / 60))
    # Wait for "q" key to escape
    if key == ord("q"): break

print(num_frame)

video.release()
cv2.destroyAllWindows()

