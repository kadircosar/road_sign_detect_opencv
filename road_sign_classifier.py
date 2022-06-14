import cv2
import numpy as np
from scipy.stats import itemfreq


def get_dominant_color(image, n_colors):
    """
    :param image  = The area to be scanned in the image
    :param n_colors = Number of clusters required at end
    :return = dominant color of area
    """
    pixels = np.float32(image).reshape((-1, 3))
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 200, .1)
    flags = cv2.KMEANS_RANDOM_CENTERS
    flags, labels, centroids = cv2.kmeans(
        pixels, n_colors, None, criteria, 10, flags)
    palette = np.uint8(centroids)
    return palette[np.argmax(itemfreq(labels)[:, -1])]


clicked = False


def on_mouse(event, x, y, flags, param):
    """
    :return = Return "clicked = True" when any event detected on mouse
    """
    global clicked
    if event == cv2.EVENT_LBUTTONUP:
        clicked = True


cameraCapture = cv2.VideoCapture(0)
cv2.namedWindow('camera')
cv2.setMouseCallback('camera', on_mouse)

# Read and process frames in loop
success, frame = cameraCapture.read()

# Sing detect continue till the first mouse event
while success and not clicked:
    cv2.waitKey(1)
    success, frame = cameraCapture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    img = cv2.medianBlur(gray, 37)
    circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 50, param1=120, param2=40)

    if circles is not None:
        circles = np.uint16(np.around(circles))
        max_r, max_i = 0, 0
        for i in range(len(circles[:, :, 2][0])):
            if circles[:, :, 2][0][i] > 50 and circles[:, :, 2][0][i] > max_r:
                max_i = i
                max_r = circles[:, :, 2][0][i]
        x, y, r = circles[:, :, :][0][max_i]
        if y > r and x > r:
            square = frame[y-r:y+r, x-r:x+r]

            dominant_color = get_dominant_color(square, 2)
            if dominant_color[2] > 100 and dominant_color[0] < 150 and dominant_color[1] < 150:
                print("STOP")
                cv2.putText(frame, "STOP", (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2,
                            (0, 255, 255), 1)
            elif dominant_color[2] > 100 and dominant_color[0] > 150 and dominant_color[1] > 150:
                cv2.putText(frame, "SPEED_LIMIT", (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2,
                            (0, 255, 255), 1)
                print("SPEED_LIMIT")

            elif dominant_color[0] > 80:
                zone_0 = square[square.shape[0]*3//8:square.shape[0] * 5//8, square.shape[1]*1//8:square.shape[1]*3//8]

                zone_0_color = get_dominant_color(zone_0, 1)

                zone_1 = square[square.shape[0]*1//8:square.shape[0]
                                * 3//8, square.shape[1]*3//8:square.shape[1]*5//8]

                zone_1_color = get_dominant_color(zone_1, 1)

                zone_2 = square[square.shape[0]*3//8:square.shape[0]
                                * 5//8, square.shape[1]*5//8:square.shape[1]*7//8]

                zone_2_color = get_dominant_color(zone_2, 1)

                if sum(zone_1_color) > sum(zone_0_color) and sum(zone_1_color) > sum(zone_2_color):
                    if sum(zone_0_color) > sum(zone_2_color) and zone_1_color[2] < 200:
                        print("RIGHT")
                        cv2.putText(frame, "RIGHT", (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2,
                                    (0, 255, 255), 1)

                    else:
                        cv2.putText(frame, "FORWARD", (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2,
                                    (0, 255, 255), 1)
                        print("FORWARD")

        for i in circles[0, :]:
            cv2.circle(frame, (i[0], i[1]), i[2], (0, 255, 0), 4)
            cv2.circle(frame, (i[0], i[1]), 2, (0, 0, 255), 3)
    else:
        cv2.putText(frame, "YOLYOK", (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2,
                    (0, 255, 255), 1)
    cv2.imshow('camera', frame)

cv2.destroyAllWindows()
cameraCapture.release()
