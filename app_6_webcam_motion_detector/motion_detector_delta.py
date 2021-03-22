# * The tutorial was using opencv 3.1.x
import cv2, time

# 0 : first camera
# Can also pass video file name like "movie.mp4"
video = cv2.VideoCapture(0)

first_frame = None

print('Starting up camera...')
# ! In some case the webcam is switched on right after cv.VideoCapture is called. 
# ! In such case, we might need to wait a little bit time before reading the first_frame. Otherwise the first_frame might not be clear enough to be differentiated by cv2.absdiff.
time.sleep(1)

while True:
    # "ret" is a boolean indicating whether it has a return value.
    ret, frame = video.read()
    if ret == True:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (21, 21), 0)

        if first_frame is None:
            first_frame = gray
            continue

        delta_frame = cv2.absdiff(first_frame, gray)
        thresh_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
        # Smoothen the threshold frame
        # The bigger the "iterations", the smoother the image will be
        thresh_frame = cv2.dilate(thresh_frame, None, iterations=2)

        (cnts, _) = cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for contour in cnts:
            if cv2.contourArea(contour) < 2000:
                # Go to the next contour
                continue
            (x, y, w, h) = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
        
        cv2.imshow("First Frame", first_frame)
        cv2.imshow("Gray Frame", gray)
        cv2.imshow("Delta Frame", delta_frame)
        cv2.imshow("Threshold Frame", thresh_frame)
        cv2.imshow("Color Frame", frame)
        
    # Make it 60 fps
    key = cv2.waitKey(int(1000 / 60))
    # Wait for "q" key to escape
    if key == ord("q"): break

video.release()
cv2.destroyAllWindows()

