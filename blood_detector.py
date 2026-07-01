import cv2
import numpy as np


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

        mask = cv2.morphologyEx(mask,
                                cv2.MORPH_OPEN,
                                kernel,
                                iterations=2)

        contours, _ = cv2.findContours(
            mask,
            cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE
        )

        stains = []

        for c in contours:

            area = cv2.contourArea(c)

            if area < self.min_area:
                continue

            if len(c) < 5:
                continue

            ellipse = cv2.fitEllipse(c)

            (cx, cy), (MA, ma), angle = ellipse

            major = max(MA, ma)
            minor = min(MA, ma)

            impact = np.degrees(
                np.arcsin(
                    np.clip(minor / major, 0, 1)
                )
            )

            stains.append({

                "center_x": cx,
                "center_y": cy,
                "major": major,
                "minor": minor,
                "impact_angle": impact,
                "ellipse": ellipse

            })

        return stains
