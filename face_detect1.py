import cv2
import sys

# cascPath = sys.argv[1]
# faceCascade = cv2.CascadeClassifier(cascPath)
faceCascade = cv2.CascadeClassifier() # NOA

video_capture = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()
    if ret:
        # cv2.namedWindow("cam-test")
        # cv2.imshow("cam-test",frame)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        import pdb; pdb.set_trace()
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

    else:
        print("not ret! ", ret)

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()