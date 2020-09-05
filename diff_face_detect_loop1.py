import numpy as np
import cv2
#from bcolor.py import *
import time

PRINT_DIFF = True
DIFF_TITLE = "right-left difference: "
DIFF_DELTA = 10


mouth_cascade = cv2.CascadeClassifier('haarcascade_mcs_mouth.xml')

if mouth_cascade.empty():
  raise IOError('Unable to load the mouth cascade classifier xml file')

from colorama import Fore, Back, Style, init

init()

def print_red(msg):
    print(Fore.BLUE + str(msg) + Style.RESET_ALL)

def print_green(msg):
    print(Fore.CYAN + str(msg) + Style.RESET_ALL)


def in_rectangle(cnt, faces):
    # if len(cnt) > 40:
        # import pdb; pdb.set_trace()
    for (x, y, w, h) in faces:
        for c in cnt:
            if (x <= c[0][0] <= x+w) and (y <= c[0][1] <= y+h):
        #print ([x,y,w,h], cnt)
                return True
    # return True
    return False
        # (x, y), (x+w, y+h)


def in_leftside_rectangle(cnt, faces):
    # if len(cnt) > 40:
        # import pdb; pdb.set_trace()
    for (x, y, w, h) in faces:
        for c in cnt:
            if (x <= c[0][0] <= (x+w//2)) and (y <= c[0][1] <= y+h):
        #print ([x,y,w,h], cnt)
                return True
    # return True
    return False
        # (x, y), (x+w, y+h)

def in_rightside_rectangle(cnt, faces):
    # if len(cnt) > 40:
        # import pdb; pdb.set_trace()
    for (x, y, w, h) in faces:
        for c in cnt:
            if ((x+w//2) <= c[0][0] <= x+w) and (y <= c[0][1] <= y+h):
        #print ([x,y,w,h], cnt)
                return True
    # return True
    return False
        # (x, y), (x+w, y+h)

def in_leftside_mouth(cnt, faces):
    # if len(cnt) > 40:
        # import pdb; pdb.set_trace()
    sum=0
    for (x, y, w, h) in faces:
        for c in cnt:
            if ((x+w//6) <= c[0][0] <= (x+w//2)) and (y +int(h/2) <= c[0][1] <= y+h):
                sum += 1
        #print ([x,y,w,h], cnt)
    return sum

def in_rightside_mouth(cnt, faces):
    # if len(cnt) > 40:
    # import pdb; pdb.set_trace()
    sum=0
    for (x, y, w, h) in faces:
        for c in cnt:
            if ((x+w//2) <= c[0][0] <= (x+2*w//3)) and (y +int(h/2) <= c[0][1] <= y + h):
                sum += 1
                # print ([x,y,w,h], cnt)
    return sum

    # return True
def main():
    import pafy
    import youtube_dl
    import cv2
    """
    url = "https://www.youtube.com/watch?v=BHfqFGj_tTw&feature=youtu.be&t=390"
    vPafy = pafy.new(url)
    play = vPafy.getbest(preftype="mp4")

    # start the video
    cap = cv2.VideoCapture(play.url)
    """
    cap = cv2.VideoCapture(r"C:\Users\Ron\Auto\T2MED\bad\str.mp4")
    #cap = cv2.VideoCapture(r"C:\Users\Ron\Videos\Rec 0003.mp4")
    #cap = cv2.VideoCapture(r"C:\Users\Ron\Auto\T2MED\bad\2.mp4")
    #cap = cv2.VideoCapture(r"C:\Users\Ron\Auto\T2MED\bad\3.mp4")


    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    #video_capture = cv2.VideoCapture(0)   # 0 -> index of camera

    #s, old_img = video_capture.read()
    ret1, old_img = cap.read()
    old_img = old_img#[0:1000, 500:1080]
    old_img = cv2.cvtColor(old_img, cv2.COLOR_BGR2GRAY)


    while(True):
        ret1, frame = cap.read()
        frame = frame#[0:1000, 500:1080]
        #s, img = video_capture.read()
        left_counter = 0
        right_counter = 0

        if ret1:

            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            diff = cv2.absdiff(old_img, frame)
            ret, thresh = cv2.threshold(diff,30,255,cv2.THRESH_BINARY_INV)

            # out = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
            contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            faces = face_cascade.detectMultiScale(frame, 1.1, 3)
            real_face=[]
            for face in faces:
                if face[2] > 150:
                    real_face.append(face)
            faces = real_face
            cop = frame.copy()
            cop = cv2.cvtColor(cop, cv2.COLOR_GRAY2RGB)

            mouth_rects = mouth_cascade.detectMultiScale(frame, 1.7, 11)
            for (x, y, w, h) in mouth_rects:
                y = int(y - 0.15 * h)
                #cv2.rectangle(cop, (x, y), (x + w, y + h), (0, 255, 0), 3)
                #cv2.rectangle(cop, (x + w, y), (x + 2 * w, y + h), (0, 255, 0), 3)
                break

            green_contours = []
            for cnt in contours:
                if in_rightside_rectangle(cnt, faces):
                    green_contours += [cnt]
                    right_counter += in_rightside_mouth(cnt, faces)
                    #try:
                        #if (mouth_rects[0][1] < cnt[0][0][1] < mouth_rects[0][1] + mouth_rects[0][3] and mouth_rects[0][0] < cnt[0][0][0] < mouth_rects[0][0] + mouth_rects[0][2]):
                        #    right_counter += cv2.contourArea(cnt)
                    #except:
                    #    None

            cv2.drawContours(cop, green_contours, -1, (255,100,100), 1)


            red_contours = []
            for cnt in contours:
                if in_leftside_rectangle(cnt, faces):
                    red_contours += [cnt]
                    left_counter += in_leftside_mouth(cnt, faces)
                    #try:

                        #if (mouth_rects[0][1] < cnt[0][0][1] < mouth_rects[0][1] + mouth_rects[0][3] and mouth_rects[0][0] + mouth_rects[0][2] < cnt[0][0][0] < mouth_rects[0][0] + 2 * mouth_rects[0][2]):
                        #    left_counter += cv2.contourArea(cnt)
                    #except:
                    #    None

            cv2.drawContours(cop, red_contours, -1, (255,105,280), 1)



            #cv2.imshow('Mouth Detector', frame)
            if PRINT_DIFF:
                d = len(green_contours)-len(red_contours)
                if d > DIFF_DELTA:
                    print_green(f"{DIFF_TITLE}{d}")
                elif d < -DIFF_DELTA:
                    print_red(f"{DIFF_TITLE}{d}")
                else:
                    print(f"{DIFF_TITLE}{d}")

            # new_contours = []
            try:
                for (x, y, w, h) in faces:
                    try:
                        if (right_counter/(left_counter + right_counter + 0.001) > 0.6 or right_counter/(left_counter + right_counter + 0.001) < 0.4):
                            cv2.rectangle(cop, (x, y), (x + w, y + h), (10, 10, 250), 4)
                            cv2.putText(cop, 'Stroke alert! L={}, R={}'.format(left_counter, right_counter), ((x-50)*((x-50)>0), y+int(1.1*h)) , cv2.FONT_HERSHEY_SIMPLEX , 1, (0, 0, 255) , 2, cv2.LINE_AA)
                        else:
                            cv2.rectangle(cop, (x, y), (x+w, y+h), (0, 0, 0), 2)
                            cv2.putText(cop, '             L={}, R={}'.format(left_counter, right_counter), ((x-50)*((x-50)>0), y+int(1.1*h)) , cv2.FONT_HERSHEY_SIMPLEX , 1, (0, 0, 0) , 2, cv2.LINE_AA)
                    except:
                        cv2.rectangle(cop, (x, y), (x + w, y + h), (0, 0, 0), 2)
            except:
                None
                # new_contours += [[[x,y]], [[x,y+h]], [[x+w,y]], [[x+w,y+h]]]

            # cv2.drawContours(cop, np.array(new_contours), -1, (100,100,255), 3)

            cv2.imshow("Image", cop)
            #time.sleep(1)
            # cv2.imshow("Image", img)
            # cv2.imshow("Image", diff)
        else:
           print('no video')
           video_capture.set(cv2.CAP_PROP_POS_FRAMES, 0)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        old_img = frame
        print("left points = {}, right_points = {}".format(left_counter, right_counter))


    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
    # pass