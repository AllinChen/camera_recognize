import dlib
import cv2

detector = dlib.get_frontal_face_detector()
path = "people2.png"
image = cv2.imread(path)
kk = cv2.waitKey(1)
faces = detector(image,2)
print(len(faces))

font = cv2.FONT_ITALIC
if len(faces) != 0:
    for k, d in enumerate(faces):
        print(k)
        height = (d.bottom() - d.top())
        width = (d.right() - d.left())
        hh = int(height/2)
        ww = int(width/2)
        cv2.putText(image, "%d"%k, (d.left() - ww, d.top() - hh), font, 0.8, (255, 255, 255), 1, cv2.LINE_AA)
        color_rectangle = (255, 255, 255)
        cv2.rectangle(image,
                        tuple([d.left() - ww, d.top() - hh]),
                        tuple([d.right() + ww, d.bottom() + hh]),
                        color_rectangle, 2)
cv2.imshow("image2",image)
cv2.waitKey(0)
cv2.destroyAllWindows()
