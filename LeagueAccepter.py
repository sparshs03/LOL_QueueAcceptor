import cv2
import mss
import numpy
import win32api, win32con #pywin32

#taking a picture of the computer screen
sct = mss.mss()
monitor = {"top": 376, "left": 408, "width": 447, "height": 198}


#TODO
# grab league client values and move accordingly

while True:
        # Taking picture of screen
        img = numpy.array(sct.grab(monitor))
        # changing color to RGB
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


        for x in range(0, monitor["width"] - 1):
            for y in range(0, monitor["height"] - 1):
                #if pixel matches colour
                if numpy.all(img[y][x] == (30, 37, 42)):
                    print("found")
                    #cv2.circle(img,(x, y), 5, (0,255,0), -1)
                    win32api.SetCursorPos((x + monitor["left"], y + monitor["top"]))
                    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x + monitor["left"], y + monitor["top"], 0,0)
                    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x + monitor["left"], y + monitor["top"], 0,0)
                    cv2.destroyAllWindows()
                    exit()

        cv2.imshow("League ScreenShotter", cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        # Press "q" to quit
        if cv2.waitKey(5) & 0xFF == ord("q"):
            cv2.destroyAllWindows()
            break