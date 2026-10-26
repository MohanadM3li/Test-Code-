import cv2
import numpy as np

# Blue and Red color ranges in HSV
blue_low = (100, 100, 60)
blue_high = (130, 255, 255)

red_low = (0, 100, 60)
red_high = (10, 255, 255)

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    raise SystemExit("Cannot open the camera")

color = "Blue"
points = []

while True:
    ret, frame = cap.read()

    if not ret:
        break

    frame = cv2.flip(frame, 1)

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Detect selected color
    if color == "Blue":
        mask = cv2.inRange(hsv, blue_low, blue_high)
        line_color = (255, 0, 0)
    else:
        mask = cv2.inRange(hsv, red_low, red_high)
        line_color = (0, 0, 255)

    # Find contours
    contours, _ = cv2.findContours(
        mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )

    if contours:
        contour = max(contours, key=cv2.contourArea)
        moments = cv2.moments(contour)

        if moments["m00"] > 300:
            cx = int(moments["m10"] / moments["m00"])
            cy = int(moments["m01"] / moments["m00"])

            points.append((cx, cy))

            cv2.circle(frame, (cx, cy), 7, line_color, -1)

    # Draw tracking trail
    for i in range(1, len(points)):
        cv2.line(
            frame,
            points[i - 1],
            points[i],
            line_color,
            3
        )

    cv2.imshow("Color Tracking", frame)

    key = cv2.waitKey(1) & 0xFF

    # C: Change between Blue and Red
    if key == ord("c"):
        if color == "Blue":
            color = "Red"
        else:
            color = "Blue"

        points.clear()

    # E: Erase tracking trail
    elif key == ord("e"):
        points.clear()

    # Q: Quit
    elif key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()