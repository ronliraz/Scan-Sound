import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
video_capture = cv2.VideoCapture(0)   # 0 -> index of camera

s, old_img = video_capture.read()


while(video_capture.isOpened()):
    s, img = video_capture.read()

    if s:

        diff = cv2.absdiff(old_img, img)
        ret, thresh = cv2.threshold(diff,30,255,cv2.THRESH_BINARY_INV)

        # out = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
        # contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        # faces = face_cascade.detectMultiScale(img, 1.1, 3)
        # for (x, y, w, h) in faces:
        #     cv2.rectangle(diff, (x, y), (x+w, y+h), (255, 200, 200), 2)
        # cv2.drawContours(img, contours, -1, (0,255,0), 3)

        cv2.imshow("Image", thresh)
        # cv2.imshow("Image", img)
        # cv2.imshow("Image", diff)
    else:
       print('no video')
       video_capture.set(cv2.CAP_PROP_POS_FRAMES, 0)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    old_img = img


cap.release()
cv2.destroyAllWindows()
