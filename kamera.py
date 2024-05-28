import cv2
Kamera = cv2.VideoCapture(0)
while True:
    Face, POSISI = Kamera.read()
    cv2.imshow('FACE',POSISI)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    Kamera.release()
    cv2.destroyAllWindows()