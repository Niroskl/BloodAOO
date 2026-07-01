import cv2
import numpy as np

from blood_stain import BloodStain


class BloodDetector:

    def __init__(self, min_area=200):
        self.min_area = min_area

    def detect(self, image):

        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        lower1 = np.array([0, 50, 50])
        upper1 = np.array([10, 255, 255])

        lower2 = np.array([160, 50, 50])
        upper2 = np.array([180, 255, 255])

        mask = cv2.inRange(hsv, lower1, upper1)
        mask += cv2.inRange(hsv, lower2, upper2)

        kernel = np.ones((3,3), np.uint8)

        mask = cv2.morphologyEx(
            mask,
            cv2.MORPH_OPEN,
            kernel,
            iterations=2
        )

        contours, _ = cv2.findContours(
            mask,
            cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE
        )

        stains = []

        for contour in contours:

            area = cv2.contourArea(contour)

            if area < self.min_area:
                continue

            if len(contour) < 5:
                continue

            perimeter = cv2.arcLength(contour, True)

            ellipse = cv2.fitEllipse(contour)

            (cx, cy), (MA, ma), angle = ellipse

            major = max(MA, ma)
            minor = min(MA, ma)

            ratio = np.clip(minor / major, 0, 1)

            impact = np.degrees(np.arcsin(ratio))

            stain = BloodStain(

                id=len(stains)+1,

                center_x=cx,
                center_y=cy,

                major_axis=major,
                minor_axis=minor,

                impact_angle=impact,

                ellipse=ellipse,

                area=area,
                perimeter=perimeter

            )

            stains.append(stain)

        return stains
