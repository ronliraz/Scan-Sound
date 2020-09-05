import numpy as np
import cv2
#from bcolor.py import *

PRINT_DIFF = True
DIFF_TITLE = "right-left difference: "
DIFF_DELTA = 10

from colorama import Fore, Back, Style, init

init()

def print_red(msg):
    print(Fore.RED + str(msg) + Style.RESET_ALL)

def print_green(msg):
    print(Fore.GREEN + str(msg) + Style.RESET_ALL)


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

def main():
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    video_capture = cv2.VideoCapture(0)   # 0 -> index of camera

    s, old_img = video_capture.read()
    old_img = cv2.cvtColor(old_img, cv2.COLOR_BGR2GRAY)


    while(video_capture.isOpened()):
        s, img = video_capture.read()

        if s:

            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            diff = cv2.absdiff(old_img, img)
            ret, thresh = cv2.threshold(diff,30,255,cv2.THRESH_BINARY_INV)

            # out = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
            contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            
            faces = face_cascade.detectMultiScale(img, 1.1, 3)

            cop = img.copy()
            cop = cv2.cvtColor(cop, cv2.COLOR_GRAY2RGB)


            green_contours = []
            for cnt in contours:
                if in_rightside_rectangle(cnt, faces):
                    green_contours += [cnt]

            cv2.drawContours(cop, green_contours, -1, (100,255,100), 3)


            red_contours = []
            for cnt in contours:
                if in_leftside_rectangle(cnt, faces):
                    red_contours += [cnt]

            cv2.drawContours(cop, red_contours, -1, (100,100,255), 3)

            if PRINT_DIFF:
                d = len(green_contours)-len(red_contours)
                if d > DIFF_DELTA:
                    print_green(f"{DIFF_TITLE}{d}")
                elif d < -DIFF_DELTA:
                    print_red(f"{DIFF_TITLE}{d}")
                else:
                    print(f"{DIFF_TITLE}{d}")

            # new_contours = []    
            for (x, y, w, h) in faces:
                cv2.rectangle(cop, (x, y), (x+w, y+h), (255, 0, 0), 2)

                # new_contours += [[[x,y]], [[x,y+h]], [[x+w,y]], [[x+w,y+h]]]

            # cv2.drawContours(cop, np.array(new_contours), -1, (100,100,255), 3)

            cv2.imshow("Image", cop)
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


if __name__ == '__main__':
    main()
    # pass