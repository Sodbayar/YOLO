import sys
import os
import cv2
from PIL import Image
#directory name
directory = sys.argv[1]
#images count
imagecount = int(sys.argv[2])
#creating a file
os.makedirs(directory, exist_ok=True)
#In my case, my webcamera is on 0.
video = cv2.VideoCapture(0)
#just for naming the files
filename = len(os.listdir(directory))
count = 0

while count < imagecount:
    filename += 1
    count += 1
    _, frame = video.read()
    im = Image.fromarray(frame, 'RGB')
    im = im.resize((128, 128))
    im.save(os.path.join(directory, '{:4d}.jpg'.format(filename)), 'JPEG')
    #if you press 'q' then it'll get out.
    cv2.imshow("Capturing", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video.release()
cv2.destroyAllWindows()