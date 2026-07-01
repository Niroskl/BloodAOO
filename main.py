import cv2
from google.colab import files
from blood_detector import BloodDetector


# ====================================
# Upload image
# ====================================

uploaded = files.upload()
filename = list(uploaded.keys())[0]

image = cv2.imread(filename)

if image is None:
    raise Exception("Image not loaded")


# ====================================
# Blood Detection
# ====================================

detector = BloodDetector(min_area=200)

stains = detector.detect(image)

print(f"\nDetected {len(stains)} stains\n")

for i, stain in enumerate(stains):

    print(f"Stain {i+1}")

    print(f"Center X      : {stain['center_x']:.1f}")
    print(f"Center Y      : {stain['center_y']:.1f}")

    print(f"Major Axis    : {stain['major']:.2f}")

    print(f"Minor Axis    : {stain['minor']:.2f}")

    print(f"Impact Angle  : {stain['impact_angle']:.2f}")

    print("-"*40)
