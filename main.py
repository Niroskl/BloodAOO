import cv2

from google.colab import files
from blood_detector import BloodDetector

uploaded = files.upload()

filename = list(uploaded.keys())[0]

image = cv2.imread(filename)

if image is None:
    raise Exception("Image could not be loaded")

detector = BloodDetector(min_area=200)

stains = detector.detect(image)

print("="*60)
print(f"Detected {len(stains)} bloodstains")
print("="*60)

for stain in stains:

    print(f"\nBloodstain #{stain.id}")

    print(f"Center X      : {stain.center_x:.2f}")
    print(f"Center Y      : {stain.center_y:.2f}")

    print(f"Major Axis    : {stain.major_axis:.2f}")

    print(f"Minor Axis    : {stain.minor_axis:.2f}")

    print(f"Impact Angle  : {stain.impact_angle:.2f}")

    print(f"Area          : {stain.area:.2f}")

    print(f"Perimeter     : {stain.perimeter:.2f}")
