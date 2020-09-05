import cv2
# import sys
import time

cascPath = "a.xml"
faceCascade = cv2.CascadeClassifier(cascPath)

# video_capture = cv2.VideoCapture(0)


# initialize the camera
video_capture = cv2.VideoCapture(0)   # 0 -> index of camera
s, img = video_capture.read()
if s:    # frame captured without any errors
    cv2.namedWindow("cam-test")
    cv2.imshow("cam-test",img)
    cv2.waitKey(0)
    cv2.destroyWindow("cam-test")
    cv2.imwrite("filename.jpg",img) #save image

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.namedWindow("Video")
    cv2.imshow("Video",frame)
    # cv2.waitKey(0)
    # cv2.destroyWindow("cam-test")
    # Display the resulting frame
    # cv2.imshow('Video', frame)

    # time.sleep(1)
#     break

#     '''
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        # flags=cv2.cv.CV_HAAR_SCALE_IMAGE
    )

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
#     '''

# # When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()