from PIL import Image, ImageDraw
import numpy as np
import cv2

# tworzę figurę
img = Image.new('RGB', (1000,1000))
points1 = np.float32([(300,100), (700,100), (100,900), (900,900)])
points2 = np.float32([(0,0), (1000,0), (0,1000), (1000,1000)])

draw = ImageDraw.Draw(img)
draw.polygon(points1, fill=(100,100,0), outline=(255,255,0))
opencvImage = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
img.show()

# obrót o 45 stopni
img = img.rotate(45)
img.show()

# przekształcenie perspektywistyczne
matrix = cv2.getPerspectiveTransform(points1, points2)
img = cv2.warpPerspective(opencvImage, matrix, (1000,1000))
cv2.imshow("transformed", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
