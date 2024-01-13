import cv2


def counter_image(filename):
    img = cv2.imread(filename)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    min_threshold = 100
    _, threshold = cv2.threshold(gray, min_threshold, 255, cv2.THRESH_BINARY)
    converted = cv2.bitwise_not(threshold)
    contours, _ = cv2.findContours(converted, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    total = 0
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 100:
            total += 1
            cv2.drawContours(img, [contour], -1, (0, 0, 255), 3)

    cv2.imshow(f'Detected {total} items', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return
