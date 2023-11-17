import cv2
import numpy as np

def main():
    anlikgoruntu = cv2.VideoCapture(0)
    while True:
        goruntuvarsa, kesit = anlikgoruntu.read()

        hsvhali = cv2.cvtColor(kesit, cv2.COLOR_BGR2HSV)

        tabankirmizi = np.array([0, 100, 100])
        tavankirmizi = np.array([10, 255, 255])

        maskeleme = cv2.inRange(hsvhali, tabankirmizi, tavankirmizi)

        
        sonuc = cv2.bitwise_and(kesit, kesit, mask=maskeleme)

        
        cv2.imshow('Original', kesit) 
        cv2.imshow('Result', sonuc)

        
        if cv2.waitKey(1) & 0xFF == ord('Q'):
            break

    
    anlikgoruntu.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()



