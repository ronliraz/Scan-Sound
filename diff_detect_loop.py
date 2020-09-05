import cv2

video_capture = cv2.VideoCapture(0)   # 0 -> index of camera

s, old_img = video_capture.read()


while(video_capture.isOpened()):
    s, img = video_capture.read()

    if s:
        diff = cv2.absdiff(old_img, img)
        cv2.imshow("Image", diff)
    else:
       print('no video')
       video_capture.set(cv2.CAP_PROP_POS_FRAMES, 0)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    old_img = img


cap.release()
cv2.destroyAllWindows()
