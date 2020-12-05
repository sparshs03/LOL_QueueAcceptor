import cv2
import mss
import numpy
import win32api, win32con, win32gui #pywin32

#initializing objects and variables
sct = mss.mss()
windowHandle = win32gui.FindWindow(None, "League of Legends")
win32gui.SetForegroundWindow(windowHandle)

while True:
        #getting window dimensions
        dimensions = win32gui.GetWindowRect(windowHandle)
        monitor = {"top": dimensions[1] + 376, "left": dimensions[0] + 408, "width": 447, "height": 198}

        # Taking picture of screen
        img = numpy.array(sct.grab(monitor))

        # changing colour(BGR) to RGB
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


        for x in range(0, monitor["width"] - 1):
            for y in range(0, monitor["height"] - 1):
                #if pixel matches colour
                if numpy.all(img[y][x] == (30, 37, 42)):

                    # Move mouse cursor to matched pixel and left click
                    win32api.SetCursorPos((x + monitor["left"], y + monitor["top"]))
                    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x + monitor["left"], y + monitor["top"], 0,0)
                    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x + monitor["left"], y + monitor["top"], 0,0)

                    #clean up and exit
                    cv2.destroyAllWindows()
                    exit()
                    
        #displaying what the computer "sees"
        cv2.imshow("LOL Auto Acceptor", cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

        # If 'q' is pressed then quit program
        if cv2.waitKey(1) & 0xFF == ord("q"):
            cv2.destroyAllWindows()
            break
